import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# Creating Data
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

np.random.seed(7)
random_x2 = np.random.randint(1, 101, 100)
random_y2 = np.random.randint(1, 101, 100)

app.layout = html.Div(
    [
        dcc.Graph(
            id='scatterplot',
            figure={
                'data': [
                    go.Scatter(
                        x=random_x,
                        y=random_y,
                        mode='markers',
                        marker={
                            'size': 12,
                            'color': 'rgb(51, 204, 153)',
                            'symbol': 'star-triangle-down-dot',
                            'line': {
                                'width': 2,
                            }
                        }
                    )
                ],
                'layout': go.Layout(
                    title='My ScatterPlot',
                    xaxis={
                        'title': 'Some X Title',
                    }
                ),
            }
        ),
        dcc.Graph(
            id='scatterplot2',
            figure={
                'data': [
                    go.Scatter(
                        x=random_x2,
                        y=random_y2,
                        mode='markers',
                        marker={
                            'size': 5,
                            'color': 'rgb(200, 204, 53)',
                            'symbol': 'star-triangle-down-dot',
                            'line': {
                                'width': 2,
                            }
                        }
                    )
                ],
                'layout': go.Layout(
                    title='My Second Plot',
                    xaxis={
                        'title': 'Some X Title',
                    }
                ),
            }
        ),
    ]
)

if __name__ == '__main__':
    app.run_server()
