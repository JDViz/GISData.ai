import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.subplots import make_subplots


# # df = pd.read_csv('../data/2010SantaBarbaraCA.csv')
# df = pd.read_csv('../data/2010YumaAZ.csv')
#
# data = [
#     go.Heatmap(
#         x=df['DAY'],
#         y=df['LST_TIME'],
#         z=df['T_HR_AVG'].values.tolist(),
#         colorscale='Jet',
#         # colorscale='Bluered',
#     )
# ]
#
# layout = go.Layout(
#     title='Santa Barbara, CA: Avg Temps, First week of June 2010',
# )
# fig = go.Figure(data=data, layout=layout)
#
# pyo.plot(fig)

# Multiple Heat Maps

df1 = pd.read_csv('../data/2010SitkaAK.csv')
df2 = pd.read_csv('../data/2010SantaBarbaraCA.csv')
df3 = pd.read_csv('../data/2010YumaAZ.csv')

trace1 = go.Heatmap(
    x=df1['DAY'],
    y=df1['LST_TIME'],
    z=df1['T_HR_AVG'].values.tolist(),
    colorscale='Jet',
    zmin=5,
    zmax=40,
        # colorscale='Bluered',
)
trace2 = go.Heatmap(
    x=df2['DAY'],
    y=df2['LST_TIME'],
    z=df2['T_HR_AVG'].values.tolist(),
    colorscale='Jet',
    zmin=5,
    zmax=40,
    # colorscale='Bluered',
)
trace3 = go.Heatmap(
    x=df3['DAY'],
    y=df3['LST_TIME'],
    z=df3['T_HR_AVG'].values.tolist(),
    colorscale='Jet',
    zmin=5,
    zmax=40,
    # colorscale='Bluered',
)

data = [trace1, trace2, trace3]


fig = make_subplots(
    rows=1,
    cols=3,
    subplot_titles=[
        'Sitka, AK',
        'Santa Barbara, CA',
        'Yuma, AZ',
    ],
    shared_yaxes=True,
)
fig.add_trace(trace1, 1, 1)
fig.add_trace(trace2, 1, 2)
fig.add_trace(trace3, 1, 3)

fig['layout'].update(title='Temps for 3 Cities.')

pyo.plot(fig)
