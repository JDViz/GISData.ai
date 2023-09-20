import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

print('Line Chart 2huptie')

df = pd.read_csv('data/nst-est2017-alldata.csv')
# print(df.head())

df2 = df[df['DIVISION'] == '6']
df2.set_index('NAME', inplace=True)
# df2.set_index('NAME')
list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
print(list_of_pop_col)
df2 = df2[list_of_pop_col]
# df2 = df2[['POPESTIMATE2010', 'POPESTIMATE2011']]
# print(df2)
# print(df2.loc['Mississippi'])

data = [go.Scatter(
    x=df2.columns,
    y=df2.loc[name],
    mode='lines',
    name=name,
) for name in df2.index]

pyo.plot(data)
