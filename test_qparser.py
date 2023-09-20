import pytest
import numpy as np

from qparser import parse_and_solve

testdata_solve = [
    # one bit
    ('''|0> XX''', np.array([1., 0.]), np.array([0.])),
    ('''|+> XX''', np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)]), np.array([0.5])),

    # two bit
    ('''[1.0/sqrt(2.0)|+> + 1.0/sqrt(2.0)|->] XX''', np.array([1., 0.]), np.array([0.])),
    ('''[1.0/sqrt(2.0)|+> - 1.0/sqrt(2.0)|->] XX''', np.array([0., 1.]), np.array([1.])),

    # adjacent actrl
    ('''|1>*|1> X*A''', np.array([0., 0., 0., 1.]), np.array([1., 1.])),
    ('''|+>*|1> X*A''', np.array([0., 1. / np.sqrt(2.), 0., 1. / np.sqrt(2.)]), np.array([1., 0.5])),
    ('''|+>*|i> X*A''', np.array([0.5, 0.5j, 0.5, +0.5j]), np.array([0.5, 0.5])),
    ('''|+>*|1> A*X''', np.array([1. / np.sqrt(2.), 0, 0, 1. / np.sqrt(2.)]), np.array([0.5, 0.5])),
    ('''|i>*|+> A*X''', np.array([0.5, 0.5, 0.5j, 0.5j]), np.array([0.5, 0.5])),

    # adjacent ctrl
    ('''|1>*|1> C*X''', np.array([0., 0., 1., 0.]), np.array([0., 1.])),
    ('''|1>*|1> X*C''', np.array([0., 1., 0., 0.]), np.array([1., 0.])),
    ('''|+>*|1> X*C''', np.array([0., 1. / np.sqrt(2.), 0., 1. / np.sqrt(2.)]), np.array([1., 0.5])),
    ('''|+>*|-> X*C''', np.array([0.5, -0.5, 0.5, -0.5]), np.array([0.5, 0.5])),
    ('''|i>*|-> X*C''', np.array([0.5, -0.5j, 0.5j, -0.5]), np.array([0.5, 0.5])),

    # adjacent swap
    ('''|0>*|-> W*W''', np.array([1. / np.sqrt(2.), 0, -1. / np.sqrt(2.), 0]), np.array([0, 0.5])),

    # non adjacent actrl
    ('''|1>*|1>*|1> A*I*X''', np.array([0., 0., 0., 0., 0., 0., 0., 1.]), np.array([1., 1., 1.])),
    ('''|+>*|1>*|1> A*I*X''', np.array([0., 0., 1. / np.sqrt(2.), 0., 0., 0., 0., 1. / np.sqrt(2.)]),
     np.array([.5, 1., .5])),

    # non adjacent ctrl
    ('''|1>*|1>*|1> C*I*X''', np.array([0., 0., 0., 0., 0., 0., 1., 0.]), np.array([0., 1., 1.])),
    ('''|+>*|1>*|1> C*I*X''', np.array([0., 0., 0., 1. / np.sqrt(2.), 0., 0., 1. / np.sqrt(2.), 0.]),
     np.array([0.5, 1., 0.5])),
]


@pytest.mark.parametrize("in_str,truth, in_prob", testdata_solve)
def test_solve(in_str, truth, in_prob):
    result, prob, in_len = parse_and_solve(in_str)
    assert np.allclose(result, truth), "values"
    assert np.allclose(prob, in_prob), "prob"
