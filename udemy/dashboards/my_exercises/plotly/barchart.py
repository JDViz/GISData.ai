import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

cc = 'cuckie'
print(f"Oh, Hai {cc}")

df = pd.read_csv('data/2018WinterOlympics.csv')
print(df.head())

# data = [go.Bar(
#     x=df['NOC'],
#     y=df['Total'],
# )]

trace0 = go.Bar(
    x=df['NOC'],
    y=df['Total'],
    name='Total',
    marker=dict(
        color='IndianRed'
    )
)
trace1 = go.Bar(
    x=df['NOC'],
    y=df['Gold'],
    name='Gold',
    marker=dict(
        color='gold'
    )
)
trace2 = go.Bar(
    x=df['NOC'],
    y=df['Silver'],
    name='Silver',
    marker=dict(
        color='lavender'
    )
)
trace3 = go.Bar(
    x=df['NOC'],
    y=df['Bronze'],
    name='Bronze',
    marker=dict(
        color='goldenrod'
    ),
)

# data = [trace0, trace1, trace2, trace3]
data = [trace1, trace2, trace3]
layout = go.Layout(
    title='Medals',
    barmode='stack',
)
fig = go.Figure(data=data, layout=layout)
fig.update_layout(
    plot_bgcolor='white',
)
fig.update_xaxes(
    showline=True,
    linewidth=2,
    linecolor='darkorange',
)
fig.update_yaxes(
    showline=True,
    linewidth=2,
    linecolor='darkorange',
    gridcolor='moccasin',
)

pyo.plot(fig)
