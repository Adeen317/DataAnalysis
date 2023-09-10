import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

np.random.seed(10)
x=np.arange(12)

y=np.random.randint(50,500,size=12)


#Line/Scatter Plot

#For plotly.graph
fig=go.Figure(data=go.Scatter(x=x,y=y))

fig.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(color='blue')))
fig.show()

#For plotly.express
fig=px.line(x=x,y=y,title='Simple Line Plot',labels=dict(x='Month',y='Sales'))
fig.show()


#Bar Plot
scores=[85,92,65,72,98,54,91]
subjects=['Maths','Physics','Chemistry','English','Social Studies','Geography','Computer Science']

fig = px.bar( x=subjects, y=scores, title='Marks Obtained in different subjects') 
fig.show()

#Histogram
heights = np.random.normal(170, 11, 200)
#Use plotly express histogram chart function
fig = px.histogram(x=heights,title="Distribution of Heights")
fig.show()


#Bubble Plot
crime_details = {
    'City' : ['Chicago', 'Chicago', 'Austin', 'Austin','Seattle','Seattle'],
    'Numberofcrimes' : [1000, 1200, 400, 700,350,1500],
    'Year' : ['2007', '2008', '2007', '2008','2007','2008'],
}
  
df = pd.DataFrame(crime_details)
print(df)

# Group the number of crimes by city and find the total number of crimes per city
bub_data = df.groupby('City')['Numberofcrimes'].sum().reset_index()
print(bub_data)

# Bubble chart using px.scatter function with x ,y and size varibles defined
fig = px.scatter(bub_data, x="City", y="Numberofcrimes", size="Numberofcrimes",
                 hover_name="City", title='Crime Statistics', size_max=60)
fig.show()


#Pie Chart
immigrants=[85,92,65,72,98,54,91]
subjects=['Pakistan','India','Bangladesh','China','Japan','South Korea','Afghanistan']

fig = px.pie(values=scores, names=subjects, title='Marks Obtained in different subjects') 
fig.show()

#Sunburst plot

data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig = px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
    title="Family chart"
)
fig.show()
