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
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV


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
#print(df['price'])

#Convert Data Types
df['price'] = df['price'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['price'].astype(float)
df['drive-wheels'] = df['drive-wheels'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['drive-wheels'].astype(float)
df['peak-rpm'] = df['peak-rpm'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['peak-rpm'].astype(float)
df['horsepower'] = df['horsepower'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['horsepower'].astype(float)

#For Splitting datasets
X = df[['highway-mpg']]
x_data = df[['curb-weight','engine-size','horsepower','highway-mpg']]
y_data = df['price']

x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.3,random_state=0)
print("Value of x_data training",x_train,"Value of x_data testing",x_test,"Value of y_data training",y_train,"Value of y_data testing",y_test)

#Cross Validation provides test value
lr=LinearRegression()
scores=cross_val_score(lr,x_data,y_data,cv=3)
print("Cross Validation Test",scores)
mean=np.mean(scores)
print("Mean of Cross Validation Test",mean)

#Cross Validation provides Predicted value
predict=cross_val_predict(lr,x_data,y_data,cv=3)
print("Cross Validation Predict",predict)
mean1=np.mean(predict)
print("Mean of Cross Validation Predict",mean1)


#R-Squared Value
Rsqu_test=[]
order=[1,2,3,4]
for n in order:
    pr=PolynomialFeatures(degree=n)
    x_train_pr=pr.fit_transform(x_train[['horsepower']])
    x_test_pr=pr.fit_transform(x_test[['horsepower']])
    lr.fit(x_train_pr,y_train)
    rsq=Rsqu_test.append(lr.score(x_train_pr,y_train))
    print("R squared value",rsq)

#Ridge Regression
RidgeModel=Ridge(alpha=0.1)
RidgeModel.fit(X,y_data)
rig=RidgeModel.predict(X)
print("Ridge Regression",rig)

#Distribution Plot
a=[rig,df['price']]
sns.kdeplot(a, color="b", label="Fitted Value")       #Negatively Correlation
#plt.ylim(0,)
plt.show()


#Grid Search
#For selecting hyperparameter=alpha we split dataset into 3 parts
#Training--->Validation(For slecting hyperparameter imp)--->Test

parameters=({'alpha':[0.001,0.1,1,10,100,1000,10000,1000000]})
rr=Ridge()
Grid=GridSearchCV(rr,parameters,cv=4)
Grid.fit(x_data,y_data)
Grid.best_estimator_
scores1=Grid.cv_results_
grs=scores1['mean_test_score']
print("Final mean result after grid search",grs)
