import pytest
import numpy as np

from qparser import parse_and_solve

testdata_calculate = [
    ('''|0>*|0>*|1>*|1> C * I * C * X ''', np.array([0., 0., 0., 1.,
                                                     0., 0., 0., 0.,
                                                     0., 0., 0., 0.,
                                                     0., 0., 0., 0.
                                                     ])),
    ('''|0>*|0>*|1>*|0>*|1> C * I * C *I * X ''', np.array([0., 0., 0., 0.,
                                                            0., 1., 0., 0.,
                                                            0., 0., 0., 0.,
                                                            0., 0., 0., 0.,
                                                            0., 0., 0., 0.,
                                                            0., 0., 0., 0.,
                                                            0., 0., 0., 0.,
                                                            0., 0., 0., 0.
                                                            ])),
]


@pytest.mark.parametrize("in_str,truth", testdata_calculate)
def test_calculate(in_str, truth):
    result, prob, in_len = parse_and_solve(in_str)
    assert np.allclose(result, truth)
