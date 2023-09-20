import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

print('Whuptie')

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# print(random_x)
# print(random_y)

data = [go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker=dict(
        size=12,
        color='pink',
        symbol='star-triangle-down-dot',
        line=dict(
            color='hotpink',
            width=1
        ),
    )
)]
layout = go.Layout(
    title='My first scatter plot',
    xaxis={'title': 'My X AXIS'},
    yaxis=dict(title='My Y AXIS'),
    hovermode='closest',
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter.html')
