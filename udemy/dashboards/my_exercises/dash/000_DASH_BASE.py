import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

app.layout = html.Div()

if __name__ == '__main__':
    app.run_server()
