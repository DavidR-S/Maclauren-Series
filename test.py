import plotly.graph_objects as go 
import numpy as np
from scipy.special import factorial
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import sympy as sp
import taylor


ts = taylor.TaylorSeries(N=10)
fx = sp.sympify('sin(x)')
df = ts.calc_taylor(fx)

print(type(df[0][0]))

# fig = go.Figure()
# fig.add_trace(go.Scatter(x = ts.x_flat, y = df[0], mode = 'lines'))
# fig.show()