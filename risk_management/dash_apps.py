import dash
from dash import html, dcc
from django_plotly_dash import DjangoDash
import plotly.express as px
import pandas as pd
from .models import Response, Meeting, Question
from dash.dependencies import Input, Output

app = DjangoDash('RiskManagementDashboard')


@app.callback(
    Output('output-container', 'children'),
    [Input('dropdown', 'value')]
)
def update_output(value):
    # Your logic to update the dashboard based on dropdown value
    return 'You have selected "{}"'.format(value)


app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Total Responses', 'value': 'TOTAL'},
            {'label': 'Responses by Meeting', 'value': 'MEETING'},
            {'label': 'Responses by Question', 'value': 'QUESTION'},
        ],
        value='TOTAL'
    ),
    html.Div(id='output-container')
])
