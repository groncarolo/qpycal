import numpy as np
import qutils


class Gate:
    gate = None


def apply(g, s):
    r = np.dot(g.gate, s)
    return qutils.remove_global_phase(r)


class XGate:
    gate = np.array([[0, 1.], [1., 0]])


class YGate:
    gate = np.array([[0., -1.j], [1.j, 0.]])


class ZGate:
    gate = np.array([[1., 0.], [0., -1.]])


class SGate:
    gate = np.array([[1, 0], [0., 1.j]])


class TGate:
    gate = np.array([[1., 0.], [0., np.exp(1.j * np.pi / 4.)]])


class HGate:
    gate = np.array([[1. / np.sqrt(2.), 1. / np.sqrt(2.)], [1. / np.sqrt(2.), -1. / np.sqrt(2.)]])


class Identity:
    gate = np.identity(2)


class CNot10:
    gate = np.array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 0., 1.], [0., 0., 1., 0.]])


class CNot01:
    gate = np.array([[1., 0., 0., 0.], [0., 0., 0., 1.], [0., 0., 1., 0.], [0., 1., 0., 0.]])
