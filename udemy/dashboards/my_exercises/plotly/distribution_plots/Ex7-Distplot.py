#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff

# create a DataFrame from the .csv file:
df = pd.read_csv('../data/iris.csv')
classes = df['class'].unique()

hist_data = []
for classname in classes:
    trace = df[df['class'] == classname]['petal_length']
    hist_data.append(trace)

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data, classes)
pyo.plot(fig, filename='MyDistExercise.html')