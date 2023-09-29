#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.subplots import make_subplots


# Create a DataFrame from  "flights" data
df = pd.read_csv('../data/flights.csv')
print(df.columns)

# Define a data variable
data = []

trace = go.Heatmap(
    x=df['year'],
    y=df['month'],
    z=df['passengers'],
    colorscale='Pinkyl',
)
data.append(trace)

# Define the layout
layout = go.Layout(
    title='Flight passenger density',
)

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
