import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import seaborn as sns


#historical_automobile sales data during recession and non-recession period.
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"


df = pd.read_csv(URL)
df.info()

#Line PLot

df_Mline = df.groupby(['Year','Vehicle_Type'], as_index=False)['Automobile_Sales'].sum()
df_Mline.set_index('Year', inplace=True)
df_Mline = df_Mline.groupby(['Vehicle_Type'])['Automobile_Sales']
df_Mline.plot(kind='line')
plt.xlabel('Year')
plt.ylabel('Prices')
plt.title('Sales Trend according to Vehicle Types during Recession')
plt.legend()
plt.show()

#Bar Chart
recession_data = df[df['Recession'] == 1]


dd=df.groupby(['Recession','Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
print(dd)
sns.barplot(x='Recession', y='Automobile_Sales', hue='Vehicle_Type', data=dd)
plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
plt.xlabel('Recession Period')
plt.ylabel('Average Sales')
plt.title('According to Vehicle Types Sales during Recession and Non-Recession Period')

plt.show()

#Subplotting
recession_data = df[df['Recession'] == 1]
non_recession_data = df[df['Recession'] == 0]

#subplot 1
plt.subplot(1, 2, 1)
sns.lineplot(x='Year', y='GDP', data=recession_data, label='Recession')
plt.xlabel('Years')
plt.ylabel('GDP')
plt.legend()
#subplot 1
plt.subplot(1, 2, 2)
sns.lineplot(x='Year', y='GDP', data=non_recession_data, label='Non Recession')
plt.xlabel('Years')
plt.ylabel('GDP')
plt.legend()

plt.suptitle('Variations in GDP during recession and non-recession period', fontsize=15)

plt.tight_layout()
plt.show()


#Bubble plot
non_rec_data = df[df['Recession'] == 0]
    
size=non_rec_data['Seasonality_Weight'] #for bubble effect
    
sns.scatterplot(data=non_rec_data, x='Month', y='Automobile_Sales', size=size)
    
#you can further include hue='Seasonality_Weight', legend=False)

plt.xlabel('Month')
plt.ylabel('Automobile_Sales')
plt.title('Seasonality impact on Automobile Sales')

plt.show()

#Scatterplot
recession_data = df[df['Recession'] == 1]
dd=df.groupby(['Recession'])#['Price'].mean()

sns.scatterplot(data=recession_data, y='Automobile_Sales', x='Price')
plt.xlabel('Price')
plt.ylabel('Sales Volume')
plt.title('Correlation between Average Vehicle Price and Sales during Recessions')
plt.show()

#Alternative
rec_data = df[df['Recession'] == 1]
plt.scatter(recession_data['Consumer_Confidence'], recession_data['Automobile_Sales'])
    
plt.xlabel('.....')
plt.ylabel('.......')
plt.title('..........')
plt.show()


#Pie Chart
recession_data = df[df['Recession'] == 1]
non_recession_data = df[df['Recession'] == 0]

avg1=recession_data['Advertising_Expenditure'].mean()
print(avg1)
avg2=non_recession_data['Advertising_Expenditure'].mean()
print(avg2)
sizes=[avg1,avg2]
plt.pie(sizes,labels=['Recession', 'Non-Recession'], autopct='%1.1f%%',startangle=90)
plt.title('Advertising Expenditure during Recession and Non-Recession Periods')
plt.show()

#2
recession_data = df[df['Recession'] == 1]

# Calculate the sales volume by vehicle type during recessions
VT_sales = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()

# Create a pie chart for the share of each vehicle type in total sales during recessions
plt.figure(figsize=(8, 6))

labels = VT_sales.index
plt.pie(VT_sales, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title('Share of Each Vehicle Type in Total Sales during Recessions')

plt.show()

#Count plot
recession_data = df[df['Recession'] == 1]
VT_sales1 = recession_data.groupby(['Vehicle_Type','Recession','unemployment_rate'])['Automobile_Sales'].sum()
print(VT_sales1)
sns.countplot(x='unemployment_rate',data=recession_data,hue='Vehicle_Type')
plt.xlabel('Unemployment Rate')
plt.ylabel('Count')
plt.title('Effect of Unemployment Rate on Vehicle Type and Sales')
plt.legend(loc='upper right')
plt.show()
