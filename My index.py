from dash import html, dcc  
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc 
import pandas as pd 
import plotly.express as px 


from app import *
from componentes import sidebar, dashboards, extratos

#-------------Layout-------------#

content = html.Div(id="Finanças")


app.loyout = dbc.Container(children=[

    dbc.Row( [
        dbc.Col( [
            dcc.Location(id="url"),
            sidebar.layout 
        ], md=2),
        dbc.Col( [
            content
        ], md=10)     

    ])

], fluid=True,)


@app.callbacks(Output("page-content", "children") [Input("url", "pathname")])
def render_page(pathname):
    if pathname == "/" or pathname == "/dashboards":
        return dashboards.loyout
    
    if pathname == "/extratos":
        return extratos.layout


if __name__=='__main__':
    app.run_server(port=8051, debug=True)

