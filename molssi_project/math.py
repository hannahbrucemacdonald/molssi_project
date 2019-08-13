"""

A file for executing maths.

"""
import numpy as np

def euler( n=10):
    if n < 0:
        raise ValueError("Only positive integers are allowed")
    series = [] 
    for x in range(0,n):
        series.append( 1./(np.math.factorial(x)) )
    return np.sum(series) 
