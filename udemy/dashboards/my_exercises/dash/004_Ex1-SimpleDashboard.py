#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd

# Launch the application:
app = dash.Dash()


# Create a DataFrame from the .csv file:
df = pd.read_csv('../data/OldFaithful.csv')

# Create a Dash layout that contains a Graph component:
app.layout = html.Div(
    [
        dcc.Graph(  # Plot 1
            id='faithfulScatter',
            figure={
                'data': [
                    go.Scatter(
                        x=df['X'],
                        y=df['Y'],
                        mode='markers',
                        marker=dict(
                            size=5,
                            color='pink',
                            # symbol='star-triangle-down-dot',
                            symbol='diamond-wide-dot',
                            line=dict(
                                color='hotpink',
                                width=1
                            ),
                        )
                    )
                ],
                'layout': go.Layout(
                    title='Old Faithful Timings',
                    xaxis={
                        'title': 'Duration of eruption',
                    },
                    yaxis={
                        'title': 'Time to next eruption',
                    }
                )
            }
        )  # end plot 1
    ]
)

# Add the server clause:
if __name__ == '__main__':
    app.run_server()

