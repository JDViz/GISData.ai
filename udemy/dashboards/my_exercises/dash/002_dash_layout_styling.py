import dash
from dash import dcc
from dash import html

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
}
# colors['text']

app.layout = html.Div(
    children=[
        html.H1(
            'Hello Dash!',
            style={
                'textAlign': 'center',
                'color': colors['text'],
            },
        ),
        html.Div('Dash: Web Dashboards with Python'),
        dcc.Graph(
            id='example',
            figure={
                'data': [
                    {
                        'x': [1, 2, 3],
                        'y': [4, 1, 2],
                        'type': 'bar',
                        'name': 'Southaven',
                    },
                    {
                        'x': [1, 2, 3],
                        'y': [2, 4, 5],
                        'type': 'bar',
                        'name': 'Memphis',
                    },
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font':{
                        'color': colors['text'],
                    },
                    'title': 'Bar Plots!'
                }
            }
        )
    ],
    style={
        'backgroundColor': colors['background']
    },

)

if __name__ == '__main__': # if you're calling this script directly...
    app.run_server()
