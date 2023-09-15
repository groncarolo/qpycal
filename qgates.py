import numpy as np
import qutils
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
    and eventually removes a global phase
    :rtype: np.array
    :param g: gate
    :param s: state matrix
    :return: result matrix
    '''
    r = np.dot(g.gate, s)
    return qutils.remove_global_phase(r)


class XGate(Gate):
    '''
    Pauli X
    '''
    label = "X"
    gate = np.array([[0, 1.], [1., 0]])

    def __init__(self):
        pass


class YGate(Gate):
    '''
    Pauli Y
    '''
    label = "Y"
    gate = np.array([[0., -1.j], [1.j, 0.]])

    def __init__(self):
        pass


class ZGate(Gate):
    '''
    Pauli Z
    '''
    label = "Z"
    gate = np.array([[1., 0.], [0., -1.]])

    def __init__(self):
        pass


class SGate(Gate):
    '''
    S Gate S^2 = Z
    '''
    label = "S"
    gate = np.array([[1, 0], [0., 1.j]])

    def __init__(self):
        pass


class TGate(Gate):
    '''
    T Gate T^2 = S
    '''
    label = "T"
    gate = np.array([[1., 0.], [0., np.exp(1.j * np.pi / 4.)]])

    def __init__(self):
        pass


class HGate(Gate):
    '''
    Hadamard Gate
    '''
    label = "H"
    gate = np.array([[1. / np.sqrt(2.), 1. / np.sqrt(2.)], [1. / np.sqrt(2.), -1. / np.sqrt(2.)]])

    def __init__(self):
        pass


class Identity(Gate):
    '''
    Identity matrix 2x2
    '''
    label = "I"
    gate = np.identity(2)

    def __init__(self):
        pass


class Ctrl(Gate):
    '''
    Control
    '''
    label = "C"
    gate = np.identity(2)

    def __init__(self):
        pass


class ACtrl(Gate):
    '''
    Anti-control
    '''
    label = "A"
    gate = np.identity(2)

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


class SwapPlaceHolder(Gate):
    '''

    '''
    gate = None
    label = "SwapPlaceHolder"

    def __init__(self):
        pass


class Swap(Gate):
    '''
    Swap
    '''

    def __init__(self, state_shape):
        self.gate = get_generic_swap(state_shape)
        self.label = "SWAP"
