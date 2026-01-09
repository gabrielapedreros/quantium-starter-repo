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
- 1. Layout layer: appears on page (ex: title, radio, graph)
- 2. Logic layer: component behavior (ex: update logic)
"""

"""
Task 4 UI Components

"""
import pandas as pd 
import plotly.express as px #plotly
import dash
from dash import dcc, html, Input, Output #write html using python

df = pd.read_csv('output_file.csv') #pandas read dataframe?
df['Date'] = pd.to_datetime(df['Date']) #make in date format
df = df.sort_values("Date") #sorted by date

#line chart and labels
#fig = px.line(df, x='Date', y='Sales', title='How The Pink Morsel Price Change Affected Sales', labels={"Date": "Date (Month, Year)", "Sales": "Sales($)"})

app = dash.Dash(__name__)

#header title
app.layout = html.Div([
    html.H1("Sales Over Time of Pink Morsels", style={'text-align': 'center'}), 

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True
    ),
    dcc.Graph(id="sales-graph")
    ]) 

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"]== selected_region]
    fig =px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        color_discrete_map={
            "north": "#b4261f",
            "east": "#1fb426",
            "south": "#1f2eb4",
            "west": "#821fb4",
            },
        title="How The Pink Morsel Price Change Affected Sales",
        labels={"Date": "Date (Month, Year)", "Sales": "Sales($)"}
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)