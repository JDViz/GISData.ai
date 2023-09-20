import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)

x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)
# print(y_values)

trace0 = go.Scatter(
    x=x_values,
    y=y_values,
    mode='markers',
    name='markers',
)
trace1 = go.Scatter(
    x=x_values,
    y=y_values+5,
    mode='lines',
    name='lines',
)
trace2 = go.Scatter(
    x=x_values,
    y=y_values-5,
    mode='lines+markers',
    name='lines+markers',
)

data = [trace0, trace1, trace2]

layout = go.Layout(
    title='Line Charts',
    xaxis={'title': 'My X AXIS'},
    yaxis=dict(title='My Y AXIS'),
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linecharts.html')
