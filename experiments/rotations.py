import sys

import numpy as np

from qgates import XGate, YGate, ZGate


#np.set_printoptions(precision=3)
#np.set_printoptions(suppress=True)


def rotationX(theta):
    return np.exp(1j * theta / 2.) * np.array([[np.cos(theta / 2), -1j * np.sin(theta / 2)],
                                               [-1j * np.sin(theta / 2), np.cos(theta / 2)]], dtype=complex)

def rotation_deg_X(theta):
    return rotationX(np.deg2rad(theta))

rx = rotationX(np.pi)
print(rx)
assert np.allclose(rx, XGate().gate)

rx = rotationX(np.pi / 2.)
print(rx.reshape(2, 2))
assert np.allclose(rx, np.array([[0.5 + 0.5j, 0.5 - 0.5j],
                                 [0.5 - 0.5j, 0.5 + 0.5j]]))

rx = rotationX(np.pi / 4.)
print(rx.reshape(2, 2))
assert np.allclose(rx, np.array(
    [[0.85355339 + 0.35355339j, 0.14644661 - 0.35355339j],
     [0.14644661 - 0.35355339j, 0.85355339 + 0.35355339j]]))

rx = rotation_deg_X(180)
print(rx)
assert np.allclose(rx, XGate().gate)

rx = rotation_deg_X(90)
print(rx.reshape(2, 2))
assert np.allclose(rx, np.array([[0.5 + 0.5j, 0.5 - 0.5j],
                                 [0.5 - 0.5j, 0.5 + 0.5j]]))

rx = rotation_deg_X(45)
print(rx.reshape(2, 2))
assert np.allclose(rx, np.array(
    [[0.85355339 + 0.35355339j, 0.14644661 - 0.35355339j],
     [0.14644661 - 0.35355339j, 0.85355339 + 0.35355339j]]))

def rotationY(phi):
    return np.exp(1j * phi / 2.) * np.array([[np.cos(phi / 2), - np.sin(phi / 2)],
                                             [np.sin(phi / 2), np.cos(phi / 2)]], dtype=complex)


ry = rotationY(np.pi)
print(ry)
assert np.allclose(ry, YGate().gate)


ry = rotationY(np.pi / 2.)
print(ry.reshape(2, 2))
assert np.allclose(ry, np.array([[0.5 + 0.5j, -0.5 - 0.5j],
                                 [+0.5 + 0.5j, 0.5 + 0.5j]]))

ry = rotationY(np.pi/4.)
print(ry.reshape(2,2))
assert np.allclose(ry, np.array([[0.85355339+0.35355339j, -0.35355339-0.14644661j],
                                 [0.35355339+0.14644661j, 0.85355339+0.35355339j]]))

def rotationZ(lam):
    return np.exp(+1j * lam / 2.) * np.array([[np.exp(-1j*lam/2.), 0.],
                                                   [0., np.exp(1j*lam/2.)]], dtype=complex)

rz = rotationZ(np.pi)
print(rz)
assert np.allclose(rz, ZGate().gate)


rz = rotationZ(np.pi / 2.)
print(rz.reshape(2, 2))
assert np.allclose(rz, np.array([[1, 0],
                                 [0., 1.j]], dtype=complex))

rz = rotationZ(np.pi/4.)
print(rz.reshape(2,2))
assert np.allclose(rz, np.array([[1., 0.],
                                 [0., 0.70710678+7.07106781e-01j]], dtype=complex))
