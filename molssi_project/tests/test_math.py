import pytest
import molssi_project as mp
import numpy as np


@pytest.mark.parametrize('n, answer', [(0, 0.), (1, 1.), (2, 2.), (3, 2.5), (4, 2.667)])
def test_euler(n, answer):
    assert (mp.math.euler(n) == pytest.approx(answer,
                                              abs=2)), 'Euler function for {n} does not match expected answer {answer}'


def test_euler_failures():
    with pytest.raises(ValueError):
        mp.math.euler(-1)


def test_pi(n=10000):
    np.random.seed(0)
    assert (mp.math.pi(n) == pytest.approx(np.pi,
                                           abs=2)), 'Calculated value of pi is not within tolerance of right answer'
    assert (mp.math.pi(n) == pytest.approx(
        3.1544, abs=1.e-4)), 'Calculated value of pi is not within tolerance of right answer'
