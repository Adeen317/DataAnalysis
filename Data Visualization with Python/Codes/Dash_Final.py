import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# Read Data
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"

df = pd.read_csv(URL)
df.info()
recession_data = df[df['Recession'] == 1]

# Create a dash application
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Automobile Sales Statistics Dashboard',
            style={'textAlign': 'center',
                   'color': '#503D36',
                   'font-size': 24}),
    dcc.Dropdown(id='dropdown-statistics',
                 options=[
                     {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                     {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
                 ],
                 placeholder='Select Statistics',
                 style={'color': 'black',
                        'font-size': 20}),
    dcc.Dropdown(id='select-year',
                 options=[{'label': i, 'value': i} for i in [i for i in range(1980, 2024, 1)]],
                 placeholder='Select Year',
                 style={'color': 'black',
                        'font-size': 20}),
    
    # Link the output-container with the update_output_container function
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex'})
])#,style={'backgroundColor': 'black'})

@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value')
)
def update_input_container(selected_value):
    if selected_value == 'Yearly Statistics':
        return False
    else:
        return True

@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='select-year', component_property='value'),
     Input(component_id='dropdown-statistics', component_property='value')]
)
def update_output_container(selected_year, selected_statistic):
    if selected_statistic == 'Recession Period Statistics':
        report_data = recession_data   # Use recession data for this option
        #plot 1
        yearly_rec = report_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        graph1 = dcc.Graph(figure=px.line(yearly_rec, x='Year', y='Automobile_Sales', title="Automobile sales fluctuate over Recession Period."))

        #Plot 2 Calculate the average number of vehicles sold by vehicle type and represent as a Bar chart
        sales_per_vehicle = report_data.groupby(['Recession', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        graph2 = dcc.Graph(figure=px.bar(sales_per_vehicle, x='Vehicle_Type', y='Automobile_Sales', title="Average Vehicle Sales by Vehicle Type"),
                           style={'width':'60%'})

        #plot 3
        avg1 = report_data['Advertising_Expenditure'].mean()
        graph3 = dcc.Graph(figure=px.pie(report_data, values='Advertising_Expenditure', names='Vehicle_Type', title="Total expenditure share by vehicle type during recessions"))


        #plot 4
        VT_sales1 = report_data.groupby(['Vehicle_Type', 'Recession', 'unemployment_rate'])['Automobile_Sales'].sum().reset_index()
        graph4 = dcc.Graph(figure=px.bar(VT_sales1, x='Vehicle_Type', y='unemployment_rate', title="Effect of unemployment rate on vehicle type and sales"))
        

    elif selected_statistic == 'Yearly Statistics':
        report_data = df[df['Year'] == selected_year]  # Filter data based on selected year

        # Plot 1 :Yearly Automobile sales using line chart for the whole period.
        yearly_rec = df.groupby('Year')['Automobile_Sales'].mean().reset_index()
        graph1 = dcc.Graph(figure=px.line(yearly_rec, x='Year', y='Automobile_Sales', title="Automobile sales fluctuate over the years."))

        # Plot 2 :Total Monthly Automobile sales using line chart.
        yearly_rec1 = report_data.groupby(['Year','Month'])['Automobile_Sales'].mean().reset_index()
        graph2 = dcc.Graph(figure=px.line(yearly_rec1, x='Month', y='Automobile_Sales', title="Total Monthly Automobile sales of the given year "))

        #Plot 3 :Bar chart for average number of vehicles sold during the given year
        yearly_rec2 = report_data.groupby(['Year','Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        graph3 = dcc.Graph(figure=px.bar(yearly_rec2, x='Vehicle_Type', y='Automobile_Sales', title="Average number of vehicles sold during the given year"))

        # Plot 4 Total Advertisement Expenditure for each vehicle using pie chart
        yearly_rec3 = report_data.groupby(['Year','Advertising_Expenditure','Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        graph4 = dcc.Graph(figure=px.pie(yearly_rec3, values='Advertising_Expenditure', names='Vehicle_Type', title="Total Advertisement Expenditure for each vehicle"))


        
    else:
        return []

   
    
    # Wrap the four graphs within an html.Div
    return  [
            html.Div(className='chart-item', children=[html.Div(children=graph1),html.Div(children=graph2)]),
            html.Div(className='chart-item', children=[html.Div(children=graph3),html.Div(children=graph4)])
            ]

# Run the application
if __name__ == '__main__':
    app.run_server()
