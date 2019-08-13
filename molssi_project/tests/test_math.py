import molssi_project as mp
import numpy as np

def test_euler(tolerance=0.01):
    e = 2.718281
    assert (mp.math.euler(0) == 0 ), 'Euler function is broken for n=0' 
    assert (mp.math.euler(1) == 1 ), 'Euler function is broken for n=1' 
    assert (np.abs(mp.math.euler(10) - e) < tolerance), f'Calculation of e is outside of tolerance {tolerance}'
