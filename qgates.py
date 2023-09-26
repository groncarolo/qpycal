import numpy as np
from qunitary import get_unitary_gate_10, get_unitary_gate_01, \
    get_generic_swap, get_cnot_actrl_10, get_cnot_actrl_01


class Gate:
    # gate = None
    # is_custom = False
    # label = ""

    def __init__(self, g, label="", is_custom=False):
        self.gate = g
        self.is_custom = is_custom
        self.label = label


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

    def __init__(self):
        super().__init__(np.array([[0, 1.], [1., 0]], dtype=complex),
                         "X")


class YGate(Gate):
    '''
    Pauli Y
    '''

    def __init__(self):
        super().__init__(np.array([[0., -1.j], [1.j, 0.]], dtype=complex),
                         "Y")


class ZGate(Gate):
    '''
    Pauli Z
    '''

    def __init__(self):
        super().__init__(np.array([[1., 0.], [0., -1.]], dtype=complex),
                         "Z")


class GenericXGate(Gate):
    '''
    Generic X Rotation
    '''

    def __init__(self, theta):
        super().__init__(
            np.exp(1j * theta / 2.) * np.array([[np.cos(theta / 2), -1j * np.sin(theta / 2)],
                                                [-1j * np.sin(theta / 2), np.cos(theta / 2)]], dtype=complex),
            "V")


class GenericYGate(Gate):
    '''
    Generic Rotation
    '''

    def __init__(self, th):
        super().__init__(np.exp(1j * th / 2.) * np.array([[np.cos(th / 2), - np.sin(th / 2)],
                                                          [np.sin(th / 2), np.cos(th / 2)]],
                                                         dtype=complex),
                         "B")


class GenericZGate(Gate):
    '''
    Generic Rotation
    '''

    def __init__(self, th):
        super().__init__(np.exp(+1j * th / 2.) * np.array([[np.exp(-1j * th / 2.), 0.],
                                                           [0., np.exp(1j * th / 2.)]],
                                                          dtype=complex),
                         "R")


class SGate(Gate):
    '''
    S Gate S^2 = Z
    '''

    def __init__(self):
        super().__init__(np.array([[1, 0], [0., 1.j]], dtype=complex),
                         "S")


class TGate(Gate):
    '''
    T Gate T^2 = S
    '''

    def __init__(self):
        super().__init__(np.array([[1., 0.], [0., np.exp(1.j * np.pi / 4.)]], dtype=complex),
                         "T")


class HGate(Gate):
    '''
    Hadamard Gate
    '''

    def __init__(self):
        super().__init__(
            np.array([[1. / np.sqrt(2.), 1. / np.sqrt(2.)], [1. / np.sqrt(2.), -1. / np.sqrt(2.)]], dtype=complex),
            "H")


class Identity(Gate):
    '''
    Identity matrix 2x2
    '''

    def __init__(self):
        super().__init__(np.identity(2, dtype=complex),
                         "I")


class Ctrl(Gate):
    '''
    Control
    '''

    def __init__(self):
        super().__init__(np.identity(2, dtype=complex),
                         "C")


class ACtrl(Gate):
    '''
    Anti-control
    '''

    def __init__(self):
        super().__init__(np.identity(2, dtype=complex),
                         "A")


class CNOT10(Gate):
    '''
    CNOT10
    '''

    def __init__(self, how_many_bits, ctrls):
        super().__init__(get_unitary_gate_10(how_many_bits, ctrls, XGate().gate),
                         "CNOT10")


class CNOT01(Gate):
    '''
    CNOT01
    '''

    def __init__(self, how_many_bits, ctrls):
        super().__init__(get_unitary_gate_01(how_many_bits, ctrls, XGate().gate),
                         "CNOT01")


class ACNOT10(Gate):
    '''
    ACNOT10
    '''

    def __init__(self, state_shape):
        super().__init__(get_cnot_actrl_10(state_shape),
                         "ACNOT10")


class ACNOT01(Gate):
    '''
    ACNOT01
    '''

    def __init__(self, state_shape):
        super().__init__(get_cnot_actrl_01(state_shape),
                         "ACNOT01")


class Toffoli10(Gate):
    '''
    Toffoli10
    '''

    def __init__(self, how_many_bits, ctrls):
        super().__init__(get_unitary_gate_10(how_many_bits, ctrls, XGate().gate),
                         "Toffoli10")


class Toffoli01(Gate):
    '''
    Toffoli01
    '''

    def __init__(self, how_many_bits, ctrls):
        super().__init__(get_unitary_gate_01(how_many_bits, ctrls, XGate().gate),
                         "Toffoli01")


class Swap(Gate):
    '''
    Swap gate
    '''
    label = "W"

    def __init__(self, state_shape=-1):
        if state_shape != -1:
            super().__init__(get_generic_swap(state_shape),
                             "SWAP")
        else:
            super().__init__(None,
                             "SWAP")
