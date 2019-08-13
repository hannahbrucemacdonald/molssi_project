import pytest
import molssi_project as mp

@pytest.mark.parametrize('n, answer', [(0,0.), (1, 1.), (2, 2.), (3, 2.5)])
def test_euler(n, answer):
    assert (mp.math.euler(n) == answer), 'Euler function for {n} does not match expected answer {answer}'
