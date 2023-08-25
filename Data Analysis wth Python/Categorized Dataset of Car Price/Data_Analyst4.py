import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import pyplot
from scipy import stats
from scipy.stats import chi2
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline


#Reading the Dataset
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'

df = pd.read_csv(url)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers
des=df.describe(include = "all")
print(des)
df.info()


#Convert Data Types
df['price'] = df['price'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['price'].astype(float)
df['drive-wheels'] = df['drive-wheels'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['drive-wheels'].astype(float)
df['peak-rpm'] = df['peak-rpm'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['peak-rpm'].astype(float)
df['horsepower'] = df['horsepower'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['horsepower'].astype(float)

#Steps To Get Prediction
#Normailization--->Polynomial_Transform--->Linear_Regression


#Regression Plot
sns.regplot(x="highway-mpg",y="price", data=df)       #Negatively Correlation
plt.ylim(0,)
plt.show()

#Residual plot
sns.residplot(x="highway-mpg",y="price", data=df)
plt.show()


#Linear Regression (Y=bo + b1(x))
#bo=intercept , b1 = Slope

lm=LinearRegression()
X = df[['highway-mpg']]
Y = df['price']
lm.fit(X,Y)
Yhat=lm.predict(X)
#Yhat=lm.predict(np.array(30.0).reshape(-1,1))
print("Linear Regression (Y=bo + b1(x))",Yhat)
intercept=lm.intercept_
slope=lm.coef_
print("Intercept is B0=",intercept,"& Slope is B1=",slope)

#Final Price
df['price']=lm.intercept_+lm.coef_*df['highway-mpg']
#print(df['price'])

#Distribution Plot
a=[Yhat,df['price']]
ax1=sns.kdeplot(df['price'], color="r", label="Actual Value")
#sns.kdeplot(a, color="b", label="Fitted Value")
plt.show()


#df = df.reindex(sorted(df.columns), axis = 1)

#Multiple Linear Regression (Y=bo + b1(x1)+b2(x2)+....)
Z = df[['curb-weight','engine-size','horsepower','highway-mpg']]
lm.fit(Z,Y)
Yhat1=lm.predict(Z)
print("Multiple Linear Regression (Y=bo + b1(x1)+b2(x2)+....)",Yhat1)
intercept1=lm.intercept_
slope1=lm.coef_
print("Intercept is B0=",intercept1,"& Slope is B1=",slope1)


#Preprocessing


#Polynomial Regression with more than one dimension

#from sklearn.preprocessing import PolynomialFeatures
pr=PolynomialFeatures(degree=2,include_bias=False)
x_polly=pr.fit_transform(df[['horsepower','curb-weight']])
print("Polynomial Regression",x_polly)

#Normalizing Data
scale=StandardScaler()
scale.fit(df[['horsepower','highway-mpg']])
x_scale=scale.transform(df[['horsepower','highway-mpg']])
print("Normalization",x_scale)


#Pipeline for more simplificatiion
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

Input=[('scale',StandardScaler()),('polynomial',PolynomialFeatures(degree=2)),('mode',LinearRegression())]
pipe=Pipeline(Input)
pipe.fit(df[['curb-weight','engine-size','horsepower','highway-mpg']],Y)
Yhat3=pipe.predict(df[['curb-weight','engine-size','horsepower','highway-mpg']])
print("Pipeline for simplication",Yhat3)


#Measure for In-Sample Evaluaton
#Mean Squared Error (MSE)
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(df['price'],Yhat3)
print("Mean Squared Error",mse)


#R-Squared
R_sq=lm.score(Z,Y)
print("R-Squared",R_sq)







