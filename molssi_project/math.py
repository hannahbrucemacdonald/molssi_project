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



def stochastic_pi(n=1000):
    inside = 0
    radius = 0.5
    center = (radius,radius) # this defines the center of the space available to np.random()`
    for _ in range(0,n):
        coords = np.random.rand(2)
        distance = np.linalg.norm(coords - center) 
        if distance <= radius:
            inside += 1
    return 4. * float(inside) / float(n)
