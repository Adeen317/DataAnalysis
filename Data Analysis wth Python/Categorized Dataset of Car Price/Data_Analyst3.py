import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import pyplot
from scipy import stats
from scipy.stats import chi2

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'

df = pd.read_csv(url)#, header=None)

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

#Showing Boxplot of Two Columns
drive_wheels_count=df["drive-wheels"].value_counts().to_frame()
drive_wheels_count.rename(columns={'drive-wheels':'value_counts'}, inplace=True)
print(drive_wheels_count)


sns.boxplot(x="drive-wheels",y="price", data=df, whis=5, showmeans=True, meanline=True)
plt.show()


#Showing Scatterplot
y=df["price"]
x=df["engine-size"]
plt.scatter(x,y)
plt.xlabel("Engine")
plt.ylabel("Price")
plt.title("Scatterplot of Engine vs Price")
plt.show()

#GroupBy
df_test = df[['drive-wheels','body-style','price']]
df_grp = df_test.groupby(['drive-wheels','body-style'],as_index=False).mean()
df_pivot=df_grp.pivot(index='drive-wheels',columns='body-style')
df_pivot=df_pivot.fillna(0)
#d=df.head(df_pivot)
#print(d)

#Heat Map
plt.pcolor(df_pivot,cmap='RdBu')
plt.colorbar()
plt.show()

fig, ax = plt.subplots()
im = ax.pcolor(df_pivot, cmap='RdBu')

#label names
row_labels = df_pivot.columns.levels[1]
col_labels = df_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(df_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(df_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=45)

fig.colorbar(im)
plt.show()


#Regression Plot
#Correlation
sns.regplot(x="highway-mpg",y="price", data=df)   #Negatively Correlated
#sns.regplot(x="engine-size",y="price", data=df)   #Positively Correlated
#sns.regplot(x="peak-rpm",y="price", data=df)       #Weak Correlation
plt.ylim(0,)
plt.show()


#Correlation - Statistics

#Pearson correlation Calculaton
pearson_coef, p_value = stats.pearsonr(df['horsepower'],df['price'])
print("Pearson Coffecient=",pearson_coef)
print("P value=", p_value)
sns.jointplot(data=df, kind="kde", color='r')
plt.show()


#Chi Square Value
a=stats.chi2_contingency(df, correction=True)
print(a)


              
