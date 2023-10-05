import numpy as np
from sympy import assoc_legendre as alp
from sympy.abc import x, theta
import sympy as sp

from sphere_plot import plot

# Define the symbolic variables for phi and theta
phi_sym, theta_sym = sp.symbols('phi theta')

# Define a general function of phi and theta
# For example, let's use f(phi, theta) = sin(phi) * cos(theta)
function_expr = alp(2,0,theta_sym)
N = 100

print(function_expr)   

plot(function_expr, phi_sym, theta_sym, N)