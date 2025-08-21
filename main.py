import plotly.graph_objects as go 
import numpy as np
from scipy.special import factorial
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import taylor

N=5

def main():
    # Create an instance of the TaylorSeries class
    ts = taylor.TaylorSeries(N=N, x_min=-5, x_max=5, num_points=100)
    
    # Generate the Taylor approximation for cos(x)
    partial_sums = ts.cos_taylor()
    

    # Plot the result
    fig = ts.plot_taylor(partial_sums, N_values=[0], y_min=-2, y_max=2,true_function=np.cos)
    fig.update_layout(showlegend=True)
    app = Dash()

    app.layout = html.Div(children=[
        html.H1(children='Dashboard'),

        html.Div(children='''
        Dash: A web application framework for your data.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        ),
        dcc.Slider(0,N,1,value = 0, id='order')
    ])

    
    
    @callback(
        Output('example-graph','figure'),
        Input('order','value'))
    def update_figure(selected_order):
        return ts.plot_taylor(partial_sums, N_values=np.arange(0,selected_order+1), y_min=-2, y_max=2,true_function=np.cos)
    app.run(debug=True)
if __name__ == "__main__":
    main()