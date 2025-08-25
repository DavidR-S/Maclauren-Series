import plotly.graph_objects as go 
import numpy as np
from scipy.special import factorial
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import taylor
import pandas as pd
import sympy as sp


N = 10
N+=1
x_min = -5
x_max = 5
num_points = 100

#Generate TaylorSeries object
ts = taylor.TaylorSeries(N=N, x_min=x_min, x_max=x_max, num_points=num_points)

#Create figures for selected functions
fig_cos = ts.create_fig(ts.cos_taylor())
fig_cos.update_layout(title='Taylor Series approximation for cos(x)')
fig_sin = ts.create_fig(ts.sin_taylor())
fig_exp = ts.create_fig(ts.exp_taylor())
#fig_custom = ts.create_fig(ts.calc_taylor(sp.sympify('sin(x)')))

app = Dash()

app.layout = html.Div(children=[
    html.H1(children='Maclauren series intereactive examples'),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),

    dcc.Graph(id='custom_graph', figure = go.Figure()),
    dcc.Slider(0,N-1,1,value = 0, id='custom_slider'),

    dcc.Graph(id='cos_graph', figure = fig_cos),
    dcc.Slider(0,N-1,1,value = 0, id='cos_slider'),

    dcc.Graph(id='sin_graph', figure = fig_sin),
    dcc.Slider(0,N-1,1,value = 0, id='sin_slider'),

    dcc.Graph(id='exp_graph', figure = fig_exp),
    dcc.Slider(0,N-1,1,value = 0, id='exp_slider')


    ])
#set up custome figure
@callback(
    Output('custom_graph', 'figure',allow_duplicate=True),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'),
    prevent_initial_call=True
)
def update_output(n_clicks,value):
    fx = sp.sympify(value)
    df = ts.calc_taylor(fx)
    fig_custom = ts.create_fig(df)
    return fig_custom

#call back for custom graph
@callback(
    Output('custom_graph','figure',allow_duplicate=True),
    Input('custom_slider','value'),
    State('custom_graph','figure'),#pretty sure slider will break when graph is empty
    prevent_initial_call = True
)
def update_figure(selected_value,current_fig):
    current_fig = go.Figure(current_fig)
    for i, trace in enumerate(current_fig.data):
        trace.visible = True if i <= selected_value else False
    return current_fig

#call back for cos graph
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

app.run(debug=True)