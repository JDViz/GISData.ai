import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


cc = 'cuckie'
print(f"Hi {cc}, show me your box!")

# set up an array of 20 data points,  with 20 as the median value
y = [1, 14, 14, 15, 16, 18, 18, 19, 19, 20, 20, 23, 24, 26, 27, 27, 28, 29, 33, 54]

# author word count ratios
snodgrass = [.209, .205, .196, .210, .202, .207, .224, .223, .220, .201]
twain = [.225, .262, .217, .240, .230, .229, .235, .217]

def findQuantiles(name, data):
    df = pd.DataFrame(data)
    quartiles = df[0].quantile([0.25, 0.75])
    iqr = quartiles[0.75] - quartiles[0.25]
    q3 = quartiles[0.75]
    q1 = quartiles[0.25]
    print("-----------------------")
    print(name)
    print(f"Q3: {q3}")
    print(f"Q1: {q1}")
    print(f"IQR: {iqr} (Q3 - Q1)")


findQuantiles('y', y)
findQuantiles('Twain', twain)
findQuantiles('Snodgrass', snodgrass)


# data = [go.Box(
#     y=y,
#     boxpoints='all',
#     jitter=0.1,
#     pointpos=0,
# )]

# data = [go.Box(
#     y=y,
#     boxpoints='outliers',
# )]

data = [
    go.Box(
        y=snodgrass,
        name='Snodgrass',
        boxpoints='all',
        jitter=0.1,
        pointpos=0,
    ),
    go.Box(
        y=twain,
        name='Twain',
        boxpoints='all',
        jitter=0.1,
        pointpos=0,
    ),
]


pyo.plot(data)