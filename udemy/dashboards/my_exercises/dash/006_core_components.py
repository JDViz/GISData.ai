import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

app.layout = html.Div(
    [
        html.P(
            html.Label('Dropdown'),
            className='dashDrop',
            id='dashDropID',
        ),
        dcc.Dropdown([
            {
                'label': 'New York City',
                'value': 'NYC',
            },
            {
                'label': 'Montréal',
                'value': 'MNT',
            },
            {
                'label': 'San Francisco',
                'value': 'SF',
            },
        ],
            'SF',
            multi=True,
        ),
        html.P(html.Label('Slider')),
        dcc.Slider(
            -10,
            10,
            0.5,
            value=-3,
            marks={i: i for i in range(-10, 11)}
        ),
        html.P(html.Label('Some Radio Items')),
        dcc.RadioItems(
            [
                {
                    'label': 'New York City',
                    'value': 'NYC',
                },
                {
                    'label': 'Montréal',
                    'value': 'MNT',
                },
                {
                    'label': 'San Francisco',
                    'value': 'SF',
                },
            ],
            'NYC',
            inline=True
        )
    ]
)

if __name__ == '__main__':
    app.run_server()
