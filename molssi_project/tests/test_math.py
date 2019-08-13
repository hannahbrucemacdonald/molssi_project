import pytest
import molssi_project as mp

@pytest.mark.parametrize('n, answer', [(0,0.), (1, 1.), (2, 2.), (3, 2.5),(4,2.667)])
def test_euler(n, answer):
    assert (mp.math.euler(n) == pytest.approx(answer, abs=2)), 'Euler function for {n} does not match expected answer {answer}'


def test_euler_failures():
    with pytest.raises(ValueError):
        mp.math.euler(-1)
