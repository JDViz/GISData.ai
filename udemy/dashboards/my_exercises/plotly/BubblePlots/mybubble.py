import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

cc = 'cuckie'
print(f"Hi bubble-{cc}")

df = pd.read_csv('../data/mpg.csv')
# df = df.astype({'horsepower': 'int64'})
# print(df)
# print(df.columns)
# print(df['horsepower'][4])
print(df.dtypes)

data = [go.Scatter(
    x=df['horsepower'],
    y=df['mpg'],
    text=df['name'],
    mode='markers',
    marker=dict(
        # size=2*df['cylinders'],
        size=df['weight']/100,
        color=df['cylinders'],
        showscale=True,
    )
)]
layout = go.Layout(
    title='Bubble Chart',
    xaxis=dict(
        title='Horsepower',
        categoryorder='category ascending',
    ),
    yaxis=dict(title='MPG'),
    hovermode='closest',
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
