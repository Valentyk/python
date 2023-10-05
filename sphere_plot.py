import plotly.graph_objects as go
import numpy as np
from sympy import assoc_legendre as alp
import sympy as sp

def plot(function, phi_sym, theta_sym, N):
    phi_values = np.linspace(-np.pi, np.pi, N)  # Adjust the number of points as needed
    theta_values = np.linspace(-np.pi/2, np.pi/2, int(N/2))  # Adjust the number of points as needed
    phi_mesh, theta_mesh = np.meshgrid(phi_values, theta_values)

    x = np.cos(phi_mesh)
    y = np.sin(phi_mesh)*np.cos(theta_mesh)
    z = np.sin(phi_mesh)*np.sin(theta_mesh)

    # Convert the symbolic function to a callable Python function
    function_lambda = sp.lambdify((phi_sym, theta_sym), function, 'numpy')

    # Calculate the function values for each phi and theta value in the grid
    function_values = function_lambda(phi_mesh, theta_mesh)

    # Create a 3D surface plot with surfacecolor
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, surfacecolor=function_values, colorscale='Viridis')])

    # Set axis labels
    fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

    # Set the title of the plot
    fig.update_layout(title=r'Function $f = f(\varphi, \vartheta)$y on a Sphere')

    # Show the plot
    fig.show()

if __name__ == "__main__":

    phi_sym, theta_sym = sp.symbols('phi theta')
    function_expr = alp(2,0,theta_sym)
    N = 50

    print(function_expr)   

    plot(function_expr, phi_sym, theta_sym)