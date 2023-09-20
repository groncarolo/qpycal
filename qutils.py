''' qutils module: various coordinates conversion utility
complex to spherical or cartesian coordinates'''
import numpy as np


# angles in deg
def spherical_2_cartesian_coordinates(angles):
    '''
    converts phi and theta into
    cartesian coordinates x,y,z
    :param angles: angles
    :rtype: np.typing.NDArray
    :return: resulting cartesian coordinates x,y,z
    '''
    angles = deg_2_rad(angles)
    phi = angles[0]
    theta = angles[1]
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.array([x, y, z])


def cartesian_2_spherical_coordinates(xyz):
    '''
    converts xyz into phi and theta
    :param xyz: cartesian coordinates
    :return: spherical coordinates
    '''
    r = np.linalg.norm(xyz)
    x, y, z = xyz
    ph = np.arctan2(y, x)
    th = max(0., np.pi / 2.0 - np.arctan2(z, np.sqrt(y * y + x * x)))
    return np.array([r, rad_2_deg(ph), rad_2_deg(th)])


def complex_2_cartesian_coordinates(c):
    '''
    converts a complex number into cartesian coordinates
    :param c: complex number
    :return: resulting cartesian coordinates x,y,z
    '''
    if np.isclose(c[0], 0.):
        return 0., 0., -1.
    alpha = c[1] / c[0]

    s = np.real(alpha)
    t = np.imag(alpha)

    moda2 = np.abs(alpha)
    moda2 **= 2
    return np.array([2 * s / (moda2 + 1), 2 * t / (moda2 + 1), (1 - moda2) / (moda2 + 1)])


def complex_2_polar_coordinates(c):
    '''
    converts complex number
    into polar ones
    :param c: complex number
    :return: polar coordinates
    '''
    return abs(c), np.angle(c)


def polar_coordinates_2_complex(radii, angles):
    '''
    converts polar coordinates into complex number
    :param radii: radii
    :param angles: angles
    :return: complex number
    '''
    return radii * np.exp(1j * angles)


def rad_2_deg(rad):
    '''
    converts radiant to degrees
    :param rad: radiant
    :return: degrees
    '''
    return rad * 360. / (2. * np.pi)


def deg_2_rad(deg):
    '''
    converts degrees into radiant
    :param deg: degrees
    :return: radiant
    '''
    return deg * (2. * np.pi) / 360.


def complex_2_spherical_coordinates(c):
    '''
    get the spherical coordinates of a complex number
    :param c:
    :return:
    '''
    xyz = complex_2_cartesian_coordinates(c)
    return cartesian_2_spherical_coordinates(xyz)


def print_cartesian_coordinates(xyz):
    '''
    prints cartesian coordinates
    :param xyz:
    :return:
    '''
    print("x y z: ", end="")
    print(xyz)


def print_spherical_coordinates(r_ph_th):
    '''
    prints spherical coordinates
    :param r_ph_th:
    :return:
    '''
    print("r ph th: ", end="")
    print(r_ph_th)


def remove_global_phase(c):
    '''
    remove global phase from a complex number
    :param c:
    :return:
    '''
    mag, ang = complex_2_polar_coordinates(c)
    if np.isclose(ang[0] / (np.pi / 4), -1.0) or np.isclose(ang[0] / (np.pi / 4), 1.0):
        c[0] = polar_coordinates_2_complex(mag[0], 0)
        c[1] = polar_coordinates_2_complex(mag[1], ang[1] - ang[0])
    return c


def get_probability(c):
    return np.multiply(c, np.conjugate(c))
