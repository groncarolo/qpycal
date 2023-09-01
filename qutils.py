import numpy as np


# angles in deg
def angles_2_cartesian_coordinates(angles):
    angles = deg_2_rad(angles)
    phi = angles[0]
    theta = angles[1]
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.array([x, y, z])


def complex_2_cartesian_coordinates(c):
    if np.isclose(c[0], 0.):
        return 0., 0., -1.
    alpha = c[1] / c[0]

    s = np.real(alpha)
    t = np.imag(alpha)

    moda2 = np.abs(alpha)
    moda2 **= 2
    return np.array([2 * s / (moda2 + 1), 2 * t / (moda2 + 1), (1 - moda2) / (moda2 + 1)])


def cartesian_2_polar_coordinates(x):
    return abs(x), np.angle(x)


def polar_2_cartesian_coordinates(radii, angles):
    return radii * np.exp(1j * angles)


def rad_2_deg(v):
    return v * 360. / (2. * np.pi)


def deg_2_rad(v):
    return v * (2. * np.pi) / 360.


def cartesian_2_spherical_coordinates(xyz):
    r = np.linalg.norm(xyz)
    x, y, z = xyz
    ph = np.arctan2(y, x)
    th = max(0., np.pi / 2.0 - np.arctan2(z, np.sqrt(y * y + x * x)))
    return np.array([r, rad_2_deg(ph), rad_2_deg(th)])


def complex_2_spherical_coordinates(c):
    xyz = complex_2_cartesian_coordinates(c)
    return cartesian_2_spherical_coordinates(xyz)


def print_cartesian_coordinates(xyz):
    print("x y z: ", end="")
    print(xyz)


def print_spherical_coordinates(r_ph_th):
    print("r ph th: ", end="")
    print(r_ph_th)


def remove_global_phase(c):
    mag, ang = cartesian_2_polar_coordinates(c)
    if np.isclose(ang[0] / (np.pi / 4), -1.0) or np.isclose(ang[0] / (np.pi / 4), 1.0):
        c[0] = polar_2_cartesian_coordinates(mag[0], 0)
        c[1] = polar_2_cartesian_coordinates(mag[1], ang[1] - ang[0])
    return c


def tensor_prod(a, b):
    return np.kron(a, b)
