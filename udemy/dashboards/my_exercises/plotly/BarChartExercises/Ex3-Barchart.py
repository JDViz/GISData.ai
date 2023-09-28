#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:
df = pd.read_csv('../data/mocksurvey.csv', index_col=[0])
cols = df.columns
questions = df.index
print(cols)
print(questions)


# Define a data variable
data = []

# create traces using a list comprehension:
for col in cols:
    # print(f"{question} :: {col}")
    trace = go.Bar(
        x=df.index,
        y=df[col],
        name=col,
    )
    data.append(trace)

layout = go.Layout(
    title='Survey',
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
