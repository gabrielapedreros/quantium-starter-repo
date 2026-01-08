"""
Task 3

Pandas: data preparation tool
- read the csv: read_csv
- convert txt into real dates: to_datetime
- sort rows by date: sort_values

HTML: structure and text

DCC: Dash Core Components - data and interactive components 
- dcc.Graph(): renders Plotly charts, displays it in the browser

Plotly
- creates the figure object (fig) (chart)
- handles axes, labels, lines, dates

Dash: web app framework for data visualization - displays the figure inside a webpage
- 2 layers
- 1. Layout layer: appears on page
- 2. Logic layer: component behavior

"""
import pandas as pd 
import plotly.express as px #plotly
import dash
from dash import dcc, html #write html using python

df = pd.read_csv('output_file.csv') #pandas read dataframe?
df['Date'] = pd.to_datetime(df['Date']) #make in date format
df = df.sort_values("Date") #sorted by date

#line chart and labels
fig = px.line(df, x='Date', y='Sales', title='How The Pink Morsel Price Change Affected Sales', labels={"Date": "Date (Month, Year)", "Sales": "Sales($)"})

app = dash.Dash(__name__)

#header title
app.layout = html.Div([html.H1("Sales Over Time of Pink Morsels", style={'text-align': 'center'}), dcc.Graph(figure=fig)]) 

if __name__ == '__main__':
    app.run(debug=True)