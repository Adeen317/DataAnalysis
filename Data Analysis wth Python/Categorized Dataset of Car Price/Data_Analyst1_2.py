import pandas as pd
import numpy as np
import matplotlib.pyplot as pylab
from matplotlib import pyplot

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'

df = pd.read_csv(url)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers
des=df.describe(include = "all")
print(des)

#To print Concise Summary of the Data
df.info()


#Dealing With missing Values
miss=df.dropna(subset=["price"],axis=0,inplace=True) #use inplace to make modification in the retrieved data 
print(miss)


#Replacing the missing values
mean = df["symboling"].mean()
#rep=df["symboling"].replace(np.nan, mean)
#print(df["symboling"])
print("Mean of Symboling",mean)

#Count missing values in each column
missing_data = df.isnull()
missing_data.head(5)
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data["normalized-losses"].value_counts())
   # print("")    




#Renaming a column 
#applying calculations to entire column
df["city-mpg"]=235/df["city-mpg"]
df.rename(columns={"city-mpg":"city-L/100km"},inplace=True)
print(df["city-L/100km"])




#understand data format

#To check datatypes for each column
types=type(df.columns)
print("Data types of Each Column",df.dtypes)
print("DataTypes of Each Column",types)




#To convert datatypes for each column

df['price'] = df['price'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['price'].astype(float)
print("price", df['price'])
types=type(df.price[0])
print(types)








#Normalization

#df["length"] = print("Simple Feature Scaling",df["length"]/df["length"].max())   #Simple Feature Scaling
df["length"]=print("Min Max Value",(df["length"]-df["length"].min())/df["length"].max()-df["length"].min()) #min max value
#df["length"]=print("Z-score value",(df["length"]-df["length"].mean())/df["length"].std()) #z-score






#Plotting Histogram
#Binning
bins=np.linspace(min(df["highway-mpg"]),max(df["highway-mpg"]),4)
group_names=["Low","Medium","High"]
df["highway-mpg-binned"]=pd.cut(df["highway-mpg"],bins,labels=group_names,include_lowest=True)

pyplot.bar(group_names, df["highway-mpg-binned"].value_counts())



# set x/y labels and plot title
pylab.xlabel("highway-mpg")
pylab.ylabel("count")
pylab.title("highway-mpg bins")
pylab.hist("",bins=206)
pylab.show()






#To generate dummy variables for a column
dummy=pd.get_dummies(df["fuel-system"])
print(df["fuel-system"])
print(dummy)





#Final Output Data Full
print("Final Output",df)

