import plotly.graph_objects as go 
import numpy as np
from scipy.special import factorial
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import taylor
import pandas as pd

N = 10
N+=1
x_min = -5
x_max = 5
num_points = 100

#Generate TaylorSeries object
ts = taylor.TaylorSeries(N=N, x_min=x_min, x_max=x_max, num_points=num_points)

fig = ts.create_fig(ts.cos_taylor())
# fig = go.Figure()

# for n in range(N):
#     fig.add_trace(go.Scatter(x=ts.x_flat, y=df_cos[n], mode='lines', visible = True if n == 0 else False, name=f'N={n}'))

app = Dash()

app.layout = html.Div(children=[
    html.H1(children='Maclauren series intereactive examples'),
    dcc.Graph(id='cos_graph', figure = fig),
    dcc.Slider(0,N-1,1,value = 0, id='order')
    ])
@callback(
    Output('cos_graph','figure'),
    Input('order','value'))
def update_figure(selected_value):

    for i, trace in enumerate(fig.data):
        trace.visible = True if i <= selected_value else False
    return fig

app.run()