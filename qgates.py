import numpy as np
import qutils


class Gate:
    gate = None

    def __init__(self, g):
        self.gate = g


def apply_gate(g, s):
    '''takes a gate g and a state n
    performs the dot product
    and eventually removes a global phase'''
    r = np.dot(g.gate, s)
    return qutils.remove_global_phase(r)


class XGate:
    label = "X"
    gate = np.array([[0, 1.], [1., 0]])


class YGate:
    label = "Y"
    gate = np.array([[0., -1.j], [1.j, 0.]])


class ZGate:
    label = "Z"
    gate = np.array([[1., 0.], [0., -1.]])


class SGate:
    label = "S"
    gate = np.array([[1, 0], [0., 1.j]])


class TGate:
    label = "T"
    gate = np.array([[1., 0.], [0., np.exp(1.j * np.pi / 4.)]])


class HGate:
    label = "H"
    gate = np.array([[1. / np.sqrt(2.), 1. / np.sqrt(2.)], [1. / np.sqrt(2.), -1. / np.sqrt(2.)]])


class Identity:
    label = "I"
    gate = np.identity(2)

class Ctrl:
    label = "C"
    gate = np.identity(2)

class ACtrl:
    label = "A"
    gate = np.identity(2)
