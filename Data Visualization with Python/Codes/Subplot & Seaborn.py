import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
from pywaffle import Waffle
import seaborn as sns


#Reading Dataframe
df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')

#Show first five rows of the data
des=df_can.describe(include = "all")
print(df_can)
print(df_can.columns)

#Groupby Continents
df_continents=df_can.groupby('Continent',axis=0).sum()
print(df_continents)

#Subplot
#Synthetic Data
years=np.arange(1980,2014)
immigrants=np.random.randint(2000,10000,size=(34,))

#create fig and axes
fig,ax=plt.subplots()

#scatter
#ax.scatter(years, immigrants)
#plt.show()

#Line
#ax.plot(years, immigrants,marker='s',markersize=5,
#        linestyle="dotted")
#plt.title('Line plot of Immigrants from 1980 to 2014')
#plt.ylabel('Number of immigrants')
#plt.xlabel('Years')
#plt.show()

#bar
#ax.bar(years,immigrants,color='blue')
#plt.title('Box plot of Immigrants from 1980 to 2014')
#plt.ylabel('Number of immigrants')
#plt.xlabel('Years')
#plt.xlim(1975,2015)
#plt.grid(True)
#plt.legend(["Immigrants"],loc="upper center")
#plt.show()

#Histogram
#ax.hist(immigrants,bins=20,edgecolor='black',color='blue')
#plt.title('Histograms on Immigrants')
#plt.ylabel('Count in data')
#plt.xlabel('Important range')
#plt.grid(True)
#plt.legend(["Immigrants"],loc="upper center")
#plt.show()

#Pie Chart
ax.pie(immigrants[0:5],labels=years[0:5],
       colors= ['gold','teal','lightgreen','coral','pink'],
       autopct='%1.1f%%')
plt.title('Distribution of Immigrants Over years')
plt.show()

#Show multiple plots at the same time

fig,axs=plt.subplots(1,3, sharey=True)

axs[0].scatter(years,immigrants)
axs[0].set_title("Scatter plot on Immigrants")

axs[1].bar(years,immigrants)
axs[1].set_title("Bar plot on Immigrants")


axs[2].plot(years,immigrants)
axs[2].set_title("Line plot on Immigrants")

fig.suptitle('Subplotting Example', fontsize=15)

# Adjust spacing between subplots
fig.tight_layout()

plt.show()

#Alternative

fig = plt.figure(figsize=(12,6))

# Add the first subplot (top-left)
axs1 = fig.add_subplot(2, 2, 1)
axs1.plot(years,immigrants,marker='s',markersize=5,
          linestyle="dotted")
axs1.set_title("Line plot on immigrants")

# Add the second subplot (top-right)
axs2 = fig.add_subplot(2, 2, 2)
axs2.scatter(years,immigrants,color='green')
axs2.set_title("scatter plot on immigrants")

# Add the first subplot (top-left)
axs3 = fig.add_subplot(2, 2, 3)
axs3.bar(years,immigrants)
axs3.set_title("Bar plot on immigrants")

# Add the second subplot (top-right)
axs4 = fig.add_subplot(2, 2, 4)
axs4.pie(immigrants[0:5],labels=years[0:5],
       colors= ['gold','teal','lightgreen','coral','pink'],
       autopct='%1.1f%%')
axs4.set_title('Distribution of Immigrants Over years')

#Adding a Title for the Overall Figure
fig.suptitle('Subplotting Example', fontsize=15)

# Adjust spacing between subplots
fig.tight_layout()


# Show the figure
plt.show()



#Waffle Charts
#data=df_continents[['Africa','Asia','Europe','Oceania']]
#data= data.transpose()
#fig=plt.figure(FigureClass=Waffle,rows=20,columns=20,values=data)
#plt.show()




#Seaborn Lib
years = list(map(str, range(1980, 2014)))
df_tot = pd.DataFrame(df_can[years].sum(axis=0))
df_tot.index = map(float, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace=True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
df_tot.head()

sns.regplot(x='year', y='total', data=df_tot)
plt.show()

#Count plot
sns.countplot(x='Continent',data=df_can)
plt.show()

#Bar Plot
sns.barplot(x='Continent',y='Total',data=df_can)
plt.show()
