import numpy as np
from sympy import assoc_legendre as alp
from sympy.abc import x, theta
import sympy as sp
import scipy.integrate as spi
import math

from sphere_plot import plot

N = 200
phi_values = np.linspace(0, np.pi, int(N/2))  # Adjust the number of points as needed
theta_values = np.linspace(0, 2*np.pi, int(N))  # Adjust the number of points as needed
phi_mesh, theta_mesh = np.meshgrid(phi_values, theta_values)

x = np.cos(phi_mesh)
y = np.sin(phi_mesh)*np.cos(theta_mesh)
z = np.sin(phi_mesh)*np.sin(theta_mesh)

jacobian = np.sin(phi_mesh)

phi_sym, theta_sym = sp.symbols('phi theta')    # Define the symbolic variables for phi and theta


function_expr = alp(1,0,sp.cos(phi_sym))   # Define a function of phi and theta


function_lambda = sp.lambdify((phi_sym, theta_sym), function_expr, 'numpy')  # Convert the symbolic function to a callable Python function
function_values = function_lambda(phi_mesh, theta_mesh) # Calculate the function values for each phi and theta value in the grid

def int(func):
    spi.simps(spi.simps(func * jacobian, dx=phi_values[1] - phi_values[0], axis=1), dx=theta_values[1] - theta_values[0])

#def eigen_func(l,m):
    #return(alp(l,m,sp.cos(phi_sym))*sp.exp(m*theta_sym))

#result = spi.simps(spi.simps(function_values * jacobian, dx=phi_values[1] - phi_values[0], axis=1), dx=theta_values[1] - theta_values[0]) # Integrate over the sphere
#print("Integral result:", result)

l_max = 5

#for l in range(l_max+1):
    #for m in range(-l,l+1):
        
        
plot(function_values, phi_sym, theta_sym, x, y, z)