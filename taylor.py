import plotly.graph_objects as go 
import numpy as np
from scipy.special import factorial
from dash import Dash, html, dash_table, dcc, callback, Output, Input

class TaylorSeries:
    def __init__ (self, N=10,x_min=-5, x_max=5, num_points=50):
        self.N = N
        self.x_min = x_min
        self.x_max = x_max
        self.num_points = num_points
        self.x_flat = np.linspace(self.x_min, self.x_max, self.num_points)
        self.x = self.x_flat[:, np.newaxis]
        self.k = np.arange(0, self.N + 1)


    def exp_taylor(self):
        powers = np.power(self.x,self.k)
        coef = 1/factorial(self.k)
        return np.cumsum(coef*powers, axis = 1)
    
    def sin_taylor(self):
        powers = np.power(self.x,2*self.k+1)
        coef = ((-1)**self.k) * 1/factorial(2*self.k+1)
        return np.cumsum(coef*powers, axis = 1)

    def cos_taylor(self):
        powers = np.power(self.x,2*self.k)
        coef = ((-1)**self.k) * 1/factorial(2*self.k)
        return np.cumsum(coef*powers, axis = 1)


    def plot_taylor(self, partial_sums, N_values=None, y_min=None, y_max=None, true_function = None):
        fig = go.Figure()
        if N_values is None:
            N_values = [self.N]
        for n in N_values:
            fig.add_trace(go.Scatter(x=self.x_flat, y=partial_sums[:,n], mode='lines', name=f'Taylor approx N={n}'))

        if true_function:
            fig.add_trace(go.Scatter(x=self.x_flat, y=true_function(self.x_flat), mode='lines', name=f'True function'))
        
        if y_min is not None and y_max is not None:
            fig.update_layout(yaxis_range=[y_min, y_max])
        
        fig.update_layout(
        title="Taylor Series Approximation",
        xaxis_title="x",
        yaxis_title="f(x)",
        legend_title="Legend")
        
        return fig

