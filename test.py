import plotly.graph_objects as go 
import numpy as np
from scipy.special import factorial
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import sympy as sp
import taylor


ts = taylor.TaylorSeries()
fx = sp.sympify('sin(x)')

powers = np.power(ts.x,ts.k)

x_sym = sp.symbols('x')
coef = np.array([(1/factorial(i))*sp.diff(fx,x_sym, i).evalf(5,subs={x_sym:0}) for i in range(ts.N*2)])

print(coef)
print(ts.sin_taylor())
#print(ts.calc_taylor(fx))