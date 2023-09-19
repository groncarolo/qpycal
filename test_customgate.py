import numpy as np
import pytest

from qparser import parse_and_solve

testdata_calculate = [
    ('''|0>*|1>*|+>*|1> G(sum)*I X*Y*Z*X X*I*I*I''', np.array([[0. + 0.j, 0. + 0.j, 0. + 0.70710678j, 0. + 0.j],
                                                               [0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j],
                                                               [0. - 0.70710678j, 0. + 0.j, 0. + 0.j, 0. + 0.j],
                                                               [0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j]])),
]


@pytest.mark.parametrize("in_str,res", testdata_calculate)
def test_calculate(in_str, res):
    result, in_len = parse_and_solve(in_str)
    assert np.allclose(result, res.flatten())
