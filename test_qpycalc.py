import numpy as np
import pytest
from qgates import *
from qpycalc import calculate
from qstates import *
from qutils import *

testdata_calculate = [
    #                       [r, ph, th],             [x,y,z]
    ('''|0> XX''', np.array([1., 0., 0.]), np.array([0., 0., 1.])),
    ('''|+> XX''', np.array([1., 0., 90.]), np.array([1., 0., 0.])),
    ('''1.0/sqrt(2.0)|+> + 1.0/sqrt(2.0)|-> XX''', np.array([1., 0., 0.]), np.array([0., 0., 1.])),
    ('''1.0/sqrt(2.0)|+> + 1.0/sqrt(2.0)|-> XX''', np.array([1., 0., 0.]), np.array([0., 0., 1.])),
    ('''1.0/sqrt(2.0)|+> - 1.0/sqrt(2.0)|-> XX''', np.array([1., 0., 180.]), np.array([0., 0., -1.]))
]


@pytest.mark.parametrize("str,r_ph_th, xyz", testdata_calculate)
def test_calculate(str, r_ph_th, xyz):
    result = calculate(str)
    ret_r_ph_th = complex_2_spherical_coordinates(result)
    ret_xyz = complex_2_cartesian_coordinates(result)
    assert (np.allclose(ret_r_ph_th, r_ph_th))
    assert (np.allclose(ret_xyz, xyz))
