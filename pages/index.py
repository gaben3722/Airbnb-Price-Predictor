# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            #### Pay to Stay: AirBnB Price Predictions
            
            
            This app was built to help hosts and renters predict the price of their daily rental from AirBnB. Your selections in the "Make a Prediction" tab will compare similar properties and
            will provide you with the best estimate for the daily rental price. 
            """,
            style={'fontFamily':'Verdana', 'fontWeight': 'normal', 'fontSize': 'smaller'}
        ),
        dcc.Link(dbc.Button('Make a Prediction', color='primary'), href='/predictions'),

    ],
    md=6,
)

column2 = dbc.Col(
    [
        html.Img(src='https://images.unsplash.com/photo-1621963262756-6836c6c86d27?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=728&q=80', style={'width': '100%'})
    ]
)

layout = dbc.Row([column1, column2])