import numpy as np
from qunitary import get_unitary_gate_10, get_unitary_gate_01, get_generic_swap, get_cnot_actrl_10, get_cnot_actrl_01


class Gate:
    gate = None
    is_custom = False
    label = ""

    def __init__(self, g):
        self.gate = g


def apply_gate(g: Gate, s):
    '''
    performs the dot product between
    gate g and state s
    :rtype: np.array
    :param g: gate
    :param s: state matrix
    :return: result matrix
    '''
    return np.dot(g.gate, s)


class XGate(Gate):
    '''
    Pauli X
    '''
    label = "X"
    gate = np.array([[0, 1.], [1., 0]], dtype=complex)

    def __init__(self):
        pass


class YGate(Gate):
    '''
    Pauli Y
    '''
    label = "Y"
    gate = np.array([[0., -1.j], [1.j, 0.]], dtype=complex)

    def __init__(self):
        pass


class ZGate(Gate):
    '''
    Pauli Z
    '''
    label = "Z"
    gate = np.array([[1., 0.], [0., -1.]], dtype=complex)

    def __init__(self):
        pass


class GenericXGate(Gate):
    '''
    Generic Rotation
    '''
    label = "V"
    gate = None

    def __init__(self, theta):
        self.gate = np.exp(1j * theta / 2.) * np.array([[np.cos(theta / 2), -1j * np.sin(theta / 2)],
                                                        [-1j * np.sin(theta / 2), np.cos(theta / 2)]], dtype=complex)
        print(self.gate)


class GenericYGate(Gate):
    '''
    Generic Rotation
    '''
    label = "B"
    gate = None

    def __init__(self, th):
        self.gate = np.exp(1j * th / 2.) * np.array([[np.cos(th / 2), - np.sin(th / 2)],
                                                     [np.sin(th / 2), np.cos(th / 2)]], dtype=complex)


class GenericZGate(Gate):
    '''
    Generic Rotation
    '''
    label = "R"
    gate = None

    def __init__(self, th):
        self.gate = np.exp(+1j * th / 2.) * np.array([[np.exp(-1j * th / 2.), 0.],
                                                      [0., np.exp(1j * th / 2.)]], dtype=complex)


class SGate(Gate):
    '''
    S Gate S^2 = Z
    '''
    label = "S"
    gate = np.array([[1, 0], [0., 1.j]], dtype=complex)

    def __init__(self):
        pass


class TGate(Gate):
    '''
    T Gate T^2 = S
    '''
    label = "T"
    gate = np.array([[1., 0.], [0., np.exp(1.j * np.pi / 4.)]], dtype=complex)

    def __init__(self):
        pass


class HGate(Gate):
    '''
    Hadamard Gate
    '''
    label = "H"
    gate = np.array([[1. / np.sqrt(2.), 1. / np.sqrt(2.)], [1. / np.sqrt(2.), -1. / np.sqrt(2.)]], dtype=complex)

    def __init__(self):
        pass


class Identity(Gate):
    '''
    Identity matrix 2x2
    '''
    label = "I"
    gate = np.identity(2, dtype=complex)

    def __init__(self):
        pass


class Ctrl(Gate):
    '''
    Control
    '''
    label = "C"
    gate = np.identity(2, dtype=complex)

    def __init__(self):
        pass


class ACtrl(Gate):
    '''
    Anti-control
    '''
    label = "A"
    gate = np.identity(2, dtype=complex)

    def __init__(self):
        pass


class CNOT10(Gate):
    '''
    CNOT10
    '''

    def __init__(self, state_shape):
        self.gate = get_unitary_gate_10(state_shape, XGate.gate)
        self.label = "CNOT10"


class CNOT01(Gate):
    '''
    CNOT01
    '''

    def __init__(self, state_shape):
        self.gate = get_unitary_gate_01(state_shape, XGate.gate)
        self.label = "CNOT01"


class ACNOT10(Gate):
    '''
    ACNOT10
    '''

    def __init__(self, state_shape):
        self.gate = get_cnot_actrl_10(state_shape)
        self.label = "ACNOT10"


class ACNOT01(Gate):
    '''
    ACNOT01
    '''

    def __init__(self, state_shape):
        self.gate = get_cnot_actrl_01(state_shape)
        self.label = "ACNOT01"


class Swap(Gate):
    '''
    Swap gate
    '''
    label = "W"

    def __init__(self, state_shape=-1):
        if state_shape != -1:
            self.gate = get_generic_swap(state_shape)
            self.label = "SWAP"
