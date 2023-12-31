import pandas as pd
import numpy as np
import matplotlib.pyplot as pylab
import matplotlib.pyplot as plt
from matplotlib import pyplot
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'

df = pd.read_csv(url)

#Datatypes of each Column
print(df.dtypes)


#Dropping Column "id" and "Unnamed: 0"
drop=df.drop(['Unnamed: 0','id'], axis=1,inplace=True)
print(df.describe())


#Count Unique Floor value
count=df["floors"].value_counts()
print("Unique Floor",count)
a=count.to_frame()
print(a)


#Boxplot
sns.boxplot(x="waterfront",y="price", data=df)
plt.show()

#Regplot
sns.regplot(x="sqft_above",y="price", data=df)
plt.ylim(0,)
plt.show()

#Linear regression and r-square value
lm=LinearRegression()
X = df[['sqft_living']]
Y = df['price']
lm.fit(X,Y)
Yhat=lm.predict(X)
print("Linear Regression (Y=bo + b1(x))",Yhat)
R_sq=lm.score(X,Y)
print("R-Squared",R_sq)



#Linear Regression
from sklearn.linear_model import LinearRegression

lm=LinearRegression()

miss=df.dropna(subset=["bedrooms"],axis=0,inplace=True)
miss1=df.dropna(subset=["bathrooms"],axis=0,inplace=True)

B=df[['floors','waterfront','lat','bedrooms','bathrooms','sqft_basement','view','sqft_living15','sqft_above','grade','sqft_living']]
Y = df['price']
lm.fit(B,Y)
Yhat=lm.predict(B)
print("Linear Regression (Y=bo + b1(x))",Yhat)
R_sq=lm.score(B,Y)
print("R-Squared",R_sq)


#Pipeline
miss=df.dropna(subset=["bedrooms"],axis=0,inplace=True)
miss1=df.dropna(subset=["bathrooms"],axis=0,inplace=True)

Input=[('scale',StandardScaler()),('polynomial',PolynomialFeatures(degree=2)),('mode',LinearRegression())]
pipe=Pipeline(Input)
B=df[['floors','waterfront','lat','bedrooms','bathrooms','sqft_basement','view','sqft_living15','sqft_above','grade','sqft_living']]
Y = df['price']
pipe.fit(B,Y)
Yhat3=pipe.predict(B)
R_sq=pipe.score(B,Y)
print("R-Squared",R_sq)


#Ridge Regression
miss=df.dropna(subset=["bedrooms"],axis=0,inplace=True)
miss1=df.dropna(subset=["bathrooms"],axis=0,inplace=True)

x_data=df[['floors','waterfront','lat','bedrooms','bathrooms','sqft_basement','view','sqft_living15','sqft_above','grade','sqft_living']]
y_data = df['price']
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.3,random_state=0)
RidgeModel=Ridge(alpha=0.1)
RidgeModel.fit(x_train,y_train)
rig=RidgeModel.predict(x_train)
r_square=RidgeModel.score(x_test,y_test)
print("Ridge Regression",rig)
print("R-Squared value of Test Data is",r_square)


#Polynomial transform and ridge regression
miss=df.dropna(subset=["bedrooms"],axis=0,inplace=True)
miss1=df.dropna(subset=["bathrooms"],axis=0,inplace=True)

x_data=df[['floors','waterfront','lat','bedrooms','bathrooms','sqft_basement','view','sqft_living15','sqft_above','grade','sqft_living']]
y_data = df['price']
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.3,random_state=0)
RidgeModel=Ridge(alpha=0.1)

Rsqu_test=[]
order=[1,2]
for n in order:
    pr=PolynomialFeatures(degree=n)
    x_train_pr=pr.fit_transform(x_train)
    x_test_pr=pr.fit_transform(x_test)
    RidgeModel.fit(x_test_pr,y_test)
    rsq=RidgeModel.score(x_test_pr,y_test)
    print("R squared value of test data",rsq)



