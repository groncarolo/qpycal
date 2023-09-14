''' Module testing qutils '''
import numpy as np
import pytest

from qutils import spherical_2_cartesian_coordinates, complex_2_cartesian_coordinates, \
    cartesian_2_spherical_coordinates, complex_2_spherical_coordinates

testdata_cartesian_coord = [
    ("|0>", np.array([0., 0.]), np.array([0., 0., 1.])),
    ("|1>", np.array([0., 180.]), np.array([0., 0., -1.])),
    ("|+>", np.array([0., 90]), np.array([1., 0., 0.])),
    ("|->", np.array([180., 90.]), np.array([-1., 0., 0.])),
    ("|i>", np.array([90., 90.]), np.array([0., 1., 0.])),
    ("|-i>", np.array([-90., 90.]), np.array([0., -1., 0.]))
]


@pytest.mark.parametrize("label,angles,xyz", testdata_cartesian_coord)
def test_spherical_2_cartesian_coordinates(label, angles, xyz):
    '''
    test spherical to cartesian coordinates
    :param label:
    :param angles:
    :param xyz:
    :return:
    '''
    ret_xyz = spherical_2_cartesian_coordinates(angles)
    assert np.allclose(ret_xyz, xyz), label


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
    '''
    test complex to cartesian coordinates
    :param label:
    :param c:
    :param xyz:
    :return:
    '''
    ret_xyz = complex_2_cartesian_coordinates(c)
    assert np.allclose(ret_xyz, xyz), label


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
    '''
    test cartesian to spherical coordinates
    :param label:
    :param xyz:
    :param r_phi_theta:
    :return:
    '''
    ret_r_phi_theta = cartesian_2_spherical_coordinates(xyz)
    assert np.allclose(ret_r_phi_theta, r_phi_theta), label


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
    '''
    test complex to spherical coordinates
    :param label:
    :param c:
    :param r_phi_theta:
    :return:
    '''
    ret_r_phi_theta = complex_2_spherical_coordinates(c)
    assert np.allclose(ret_r_phi_theta, r_phi_theta), label
