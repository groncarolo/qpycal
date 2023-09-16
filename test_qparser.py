import pytest
import numpy as np

from qparser import parse_and_calculate

testdata_calculate = [
    ('''|0> XX''', np.array([1., 0.])),
    ('''|+> XX''', np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    ('''[1.0/sqrt(2.0)|+> + 1.0/sqrt(2.0)|->] XX''', np.array([1., 0.])),
    ('''[1.0/sqrt(2.0)|+> - 1.0/sqrt(2.0)|->] XX''', np.array([0., 1.])),
    ('''|1>*|1>*|1> A*I*X''', np.array([0., 0., 0., 0., 0., 0., 0., 1.])),
    ('''|1>*|1> X*A''', np.array([0., 0., 0., 1.])),
    ('''aaa |1>*bbbbb|1> X*A''', np.array([0., 0., 0., 1.])),
    ('''vv [1.0/sqrt(2.0)|0> - 1.0/sqrt(2.0)|1>]*|1>*|+>*|1>*aaa|0>
    G(sum)*I*I X*Y*Z*X*I X*I*I*I*X X*Y*Z*X*I X*Y*Z*X*I X*Y*Z*X*I
    G(sum)*I*I X*Y*Z*X*I  X*Y*Z*X*I  X*Y*Z*X*I  X*Y*Z*X*I  X*Y*Z*X*I''',
     np.array([0. + 0.j, 0. - 0.5j, 0. + 0.j, 0. + 0.j,
               0. + 0.j, 0. + 0.5j, 0. + 0.j, 0. + 0.j,
               0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j,
               0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j,
               0. + 0.j, 0. + 0.5j, 0. + 0.j, 0. + 0.j,
               0. + 0.j, 0. - 0.5j, 0. + 0.j, 0. + 0.j,
               0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j,
               0. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j, ])),
    ('''aaa 1.0/1.0 |1>*|1> X*A''', np.array([0., 0., 0., 1.]))
]


@pytest.mark.parametrize("in_str,truth", testdata_calculate)
def test_calculate(in_str, truth):
    result, in_len = parse_and_calculate(in_str)
    assert np.allclose(result, truth)
