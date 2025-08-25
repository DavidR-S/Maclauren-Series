import plotly.graph_objects as go 
import numpy as np
from scipy.special import factorial
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import sympy as sp

class TaylorSeries:
    def __init__ (self, N=10,x_min=-5, x_max=5, num_points=50):
        self.N = N
        self.x_min = x_min
        self.x_max = x_max
        self.num_points = num_points
        self.x_flat = np.linspace(self.x_min, self.x_max, self.num_points)
        self.x = self.x_flat[:, np.newaxis]
        self.k = np.arange(0, self.N + 1)

    def calc_taylor(self, fx):
        powers = np.power(self.x,self.k)

        #calculate f^(n) (0) for 0<=n<=N
        x_sym = sp.symbols('x')
        coef = np.array([sp.diff(fx,x_sym, i).evalf(5,subs={x_sym:0}) for i in range(self.N+1)])
        return pd.DataFrame(np.cumsum(coef*powers, axis = 1))
        
    def exp_taylor(self):
        powers = np.power(self.x,self.k)
        coef = 1/factorial(self.k)
        return pd.DataFrame(np.cumsum(coef*powers, axis = 1))
    
    def sin_taylor(self):
        powers = np.power(self.x,2*self.k+1)
        coef = ((-1)**self.k) * 1/factorial(2*self.k+1)
        print(coef)
        return pd.DataFrame(np.cumsum(coef*powers, axis = 1))

    def cos_taylor(self):
        powers = np.power(self.x,2*self.k)
        coef = ((-1)**self.k) * 1/factorial(2*self.k)
        return pd.DataFrame(np.cumsum(coef*powers, axis = 1))
    
    def create_fig(self,df):
        fig = go.Figure()
        for n in range(self.N):
            fig.add_trace(go.Scatter(x = self.x_flat, y = df[n], mode='lines', 
                            visible = True if n == 0 else False, name=f'N={n}'))
        return fig
