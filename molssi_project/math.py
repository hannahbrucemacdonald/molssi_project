"""

A file for executing maths.

"""
import numpy as np

def euler( n=10):
    if n < 0:
        raise ValueError("Only positive integers are allowed")
    val = 0. 
    for x in range(0,n):
        val += 1./(np.math.factorial(x)) 
    return val


def pi(n=1000):
    inside = 0
    radius = 0.5
    center = (radius,radius) # this defines the center of the space available to np.random()`
    for _ in range(0,n):
        coords = np.random.rand(2)
        distance = np.linalg.norm(coords - center) 
        if distance <= radius:
            inside += 1
    return 4. * float(inside) / float(n)
