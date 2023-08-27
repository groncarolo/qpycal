import numpy as np
from qutils import *
import pytest

testdata_cartesian_coord = [
    ("|0>", np.array([0., 0.]), np.array([0., 0., 1.])),
    ("|1>", np.array([0., 180.]), np.array([0., 0., -1.])),
    ("|+>", np.array([0., 90]), np.array([1., 0., 0.])),
    ("|->", np.array([180., 90.]), np.array([-1., 0., 0.])),
    ("|i>", np.array([90., 90.]), np.array([0., 1., 0.])),
    ("|-i>", np.array([-90., 90.]), np.array([0., -1., 0.]))
]


@pytest.mark.parametrize("label,angles,xyz", testdata_cartesian_coord)
def test_angles_2_cartesian_coordinates(label, angles, xyz):
    ret_xyz = angles_2_cartesian_coordinates(angles)
    assert np.allclose(ret_xyz, xyz)


testdata_cartesian_coord_a_b = [
    ("|0>", np.array([1., 0.]), np.array([0., 0., 1.])),
    ("|1>", np.array([0., 1.]), np.array([0., 0., -1.])),
    ("|+>", np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)]), np.array([1., 0., 0.])),
    ("|->", np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)]), np.array([-1., 0., 0.])),
    ("|i>", np.array([1. / np.sqrt(2.), 1j / np.sqrt(2.)]), np.array([0., 1., 0.])),
    ("|-i>", np.array([1. / np.sqrt(2.), -1j / np.sqrt(2.)]), np.array([0., -1., 0.]))
]


@pytest.mark.parametrize("label,c,xyz", testdata_cartesian_coord_a_b)
def test_complex_2_cartesian_coordinates(label, c, xyz):
    ret_xyz = complex_2_cartesian_coordinates(c)
    assert np.allclose(ret_xyz, xyz)


testdata_spherical_coord = [
    ("|0>", np.array([0., 0., 1.]), np.array([1., 0., 0.])),
    ("|1>", np.array([0., 0., -1.]), np.array([1., 0., 180.])),
    ("|+>", np.array([1., 0., 0.]), np.array([1., 0., 90.])),
    ("|->", np.array([-1., 0., 0.]), np.array([1., 180., 90.])),
    ("|i>", np.array([0., 1., 0.]), np.array([1., 90., 90.])),
    ("|-i>", np.array([0., -1., 0.]), np.array([1., -90., 90.]))
]


@pytest.mark.parametrize("label, xyz,r_phi_theta", testdata_spherical_coord)
def test_cartesian_2_spherical_coordinates(label, xyz, r_phi_theta):
    ret_r_phi_theta = cartesian_2_spherical_coordinates(xyz)
    assert np.allclose(ret_r_phi_theta, r_phi_theta)


testdata_spherical_coord_a_b = [
    ("|0>", np.array([1., 0.]), np.array([1, 0., 0.])),
    ("|1>", np.array([0., 1.]), np.array([1, 0., 180.])),
    ("|+>", np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)]), np.array([1, 0., 90.])),
    ("|->", np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)]), np.array([1, 180., 90.])),
    ("|i>", np.array([1. / np.sqrt(2.), 1j / np.sqrt(2.)]), np.array([1, 90., 90.])),
    ("|-i>", np.array([1. / np.sqrt(2.), -1j / np.sqrt(2.)]), np.array([1, -90., 90.]))
]


@pytest.mark.parametrize("label,c,r_phi_theta", testdata_spherical_coord_a_b)
def test_complex_2_spherical_coordinates(label, c, r_phi_theta):
    ret_r_phi_theta = complex_2_spherical_coordinates(c)
    assert np.allclose(ret_r_phi_theta, r_phi_theta)
