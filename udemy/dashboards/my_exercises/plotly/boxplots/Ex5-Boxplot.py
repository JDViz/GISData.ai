#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go




# create a DataFrame from the .csv file:
df = pd.read_csv('../data/abalone.csv')

# take two random samples of different sizes:
sample1 = np.random.choice(df['rings'],10, replace=False)
sample2 = np.random.choice(df['rings'],10, replace=False)

print(sample1)
print(sample2)


# create a data variable with two Box plots:
data = [
    go.Box(
        y=sample1,
        name='Sample 1',
        boxpoints='all',
        jitter=0.1,
        pointpos=0,
    ),
    go.Box(
        y=sample2,
        name='Sample 2',
        boxpoints='all',
        jitter=0.1,
        pointpos=0,
    ),
]

# add a layout
layout = go.Layout(
    title='My Box Plot Samples',
    yaxis=dict(title='Sample Range'),
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='mybox.html')
