import numpy as np

def f(x):
    return np.exp((x**4 + 2*x**3 -5*x +6)/5) + np.cosh(1/(-15*x**3 + 10*x + 5*np.sqrt(10))) - 3
