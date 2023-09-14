import numpy as np
import qutils
from qunitary import get_unitary_gate_10, get_unitary_gate_01, get_generic_swap


class Gate:
    gate = None

    def __init__(self, g):
        self.gate = g


def apply_gate(g: Gate, s):
    '''
    performs the dot product between
    gate g and state s
    and eventually removes a global phase
    :rtype: np.array
    :param g: gate
    :param s: state matrix
    :return: result matrix
    '''
    r = np.dot(g.gate, s)
    return qutils.remove_global_phase(r)


class XGate:
    '''
    Pauli X
    '''
    label = "X"
    gate = np.array([[0, 1.], [1., 0]])


class YGate:
    '''
    Pauli Y
    '''
    label = "Y"
    gate = np.array([[0., -1.j], [1.j, 0.]])


class ZGate:
    '''
    Pauli Z
    '''
    label = "Z"
    gate = np.array([[1., 0.], [0., -1.]])


class SGate:
    '''
    S Gate S^2 = Z
    '''
    label = "S"
    gate = np.array([[1, 0], [0., 1.j]])


class TGate:
    '''
    T Gate T^2 = S
    '''
    label = "T"
    gate = np.array([[1., 0.], [0., np.exp(1.j * np.pi / 4.)]])


class HGate:
    '''
    Hadamard Gate
    '''
    label = "H"
    gate = np.array([[1. / np.sqrt(2.), 1. / np.sqrt(2.)], [1. / np.sqrt(2.), -1. / np.sqrt(2.)]])


class Identity:
    '''
    Identity matrix 2x2
    '''
    label = "I"
    gate = np.identity(2)


class Ctrl:
    '''
    Control
    '''
    label = "C"
    gate = np.identity(2)


class ACtrl:
    '''
    Anti-control
    '''
    label = "A"
    gate = np.identity(2)


class CNOT10:
    '''
    CNOT10
    '''
    label = "CNOT10"
    gate = None

    def __init__(self, state_shape):
        self.gate = get_unitary_gate_10(state_shape, XGate.gate)


class CNOT01:
    '''
    CNOT01
    '''
    label = "CNOT01"
    gate = None

    def __init__(self, state_shape):
        self.gate = get_unitary_gate_01(state_shape, XGate.gate)


class SwapPlaceHolder:
    '''

    '''


class Swap:
    '''
    Swap
    '''
    label = "SWAP"
    gate = None

    def __init__(self, state_shape):
        self.gate = get_generic_swap(state_shape)
