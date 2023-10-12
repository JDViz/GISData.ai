import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd


app = dash.Dash()

app.layout = html.Div(
    [
        'This is the outermost DIV!',
        html.Div(
            ['This is an inner div!'],
            style={
                'color': 'DeepPink',
                'border': '1px solid DeepPink',
            },
        ),
        html.Div(
            ['Another inner DIV!'],
            style={
                'color': 'hotpink',
                'border': '1px solid hotpink',
            },
        ),
        html.Div(
            ['Another inner DIV!'],
            style={
                'color': 'lightpink',
                'border': '1px solid lightpink',
            },
        ),
    ],
    style={
        'color': 'MediumVioletRed',
        'border': '4px solid MediumVioletRed',
    },

)

if __name__ == '__main__':
    app.run_server()
