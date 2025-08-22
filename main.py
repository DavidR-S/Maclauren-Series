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

#Create figures for selected functions
fig_cos = ts.create_fig(ts.cos_taylor())
fig_sin = ts.create_fig(ts.sin_taylor())
fig_exp = ts.create_fig(ts.exp_taylor())

app = Dash()

app.layout = html.Div(children=[
    html.H1(children='Maclauren series intereactive examples'),
    dcc.Graph(id='cos_graph', figure = fig_cos),
    dcc.Slider(0,N-1,1,value = 0, id='cos_slider'),

    dcc.Graph(id='sin_graph', figure = fig_sin),
    dcc.Slider(0,N-1,1,value = 0, id='sin_slider'),

    dcc.Graph(id='exp_graph', figure = fig_exp),
    dcc.Slider(0,N-1,1,value = 0, id='exp_slider')


    ])

@callback(
    Output('cos_graph','figure'),
    Input('cos_slider','value'))
def update_figure(selected_value):

    for i, trace in enumerate(fig_cos.data):
        trace.visible = True if i <= selected_value else False
    return fig_cos

@callback(
    Output('sin_graph','figure'),
    Input('sin_slider','value'))
def update_figure(selected_value):

    for i, trace in enumerate(fig_sin.data):
        trace.visible = True if i <= selected_value else False
    return fig_sin

@callback(
    Output('exp_graph','figure'),
    Input('exp_slider','value'))
def update_figure(selected_value):

    for i, trace in enumerate(fig_exp.data):
        trace.visible = True if i <= selected_value else False
    return fig_exp

app.run()