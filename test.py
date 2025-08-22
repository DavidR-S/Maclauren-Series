import plotly.graph_objects as go 
import numpy as np
from scipy.special import factorial
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import taylor
N=10
N+=1
ts = taylor.TaylorSeries(N=N, x_min=-5, x_max=5, num_points=100)
df = ts.cos_taylor()
print(type(df))
print(df)
df = pd.DataFrame(df)

print(type(df))

print(df)

fig = go.Figure()
for n in range(N):
    fig.add_trace(go.Scatter(x = ts.x_flat, y = df[n], mode = 'lines'))
fig.show()