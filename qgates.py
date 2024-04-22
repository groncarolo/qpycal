"""
>>> g = xgate()
>>> g
QGate(_gate=array([[0.+0.j, 1.+0.j],
       [1.+0.j, 0.+0.j]]), _label='X', _is_custom=False)

"""

from dataclasses import dataclass
import numpy as np
from qstates import QState
from qunitary import get_cnot_ctrl_10, get_cnot_ctrl_01, get_generic_swap, get_cnot_actrl_10, get_cnot_actrl_01, \
    get_unitary_gate_10, get_unitary_gate_01, get_unitary_agate_01, get_unitary_agate_10


@dataclass(eq=False)
class QGate:
    """ Quantum Gate class """
    gate: np.ndarray
    label: str = str()
    is_custom: bool = False

    def __eq__(self, other):
        return (self.gate.shape == other.gate.shape and
                (self.gate == other.gate).all())

    def __array__(self):
        return self.gate

    def apply(self, state: QState) -> 'QState':
        """
        performs the dot product between
        gate g and state s
        :param state
        :return: resulting QState
        """
        return QState(np.squeeze(np.dot(self.gate, state.state)))


def xgate() -> 'QGate':
    """ Pauli X """
    arr = np.array([[0, 1.], [1., 0]], dtype=complex)
    return QGate(arr, "X")


def ygate() -> 'QGate':
    """ Pauli Y """
    arr = np.array([[0., -1.j], [1.j, 0.]], dtype=complex)
    return QGate(arr, "Y")


def zgate() -> 'QGate':
    """ Pauli Z """
    arr = np.array([[1., 0.], [0., -1.]], dtype=complex)
    return QGate(arr, "Z")


def generic_xgate(theta: float) -> 'QGate':
    """ Generic X Rotation """
    arr = np.array([[np.cos(theta / 2), -1j * np.sin(theta / 2)],
                    [-1j * np.sin(theta / 2), np.cos(theta / 2)]], dtype=complex)
    return QGate(np.exp(1j * theta / 2.) * arr, "V")


def generic_ygate(theta: float) -> 'QGate':
    """ Generic Y Rotation """
    arr = np.array([[np.cos(theta / 2), - np.sin(theta / 2)],
                    [np.sin(theta / 2), np.cos(theta / 2)]],
                   dtype=complex)
    return QGate(np.exp(1j * theta / 2.) * arr, "B")


def generic_zgate(theta: float) -> 'QGate':
    """ Generic Z Rotation """
    arr = np.array([[np.exp(-1j * theta / 2.), 0.],
                    [0., np.exp(1j * theta / 2.)]],
                   dtype=complex)
    return QGate(np.exp(+1j * theta / 2.) * arr, "R")


def sgate() -> 'QGate':
    """ S Gate S^2 = Z """
    arr = np.array([[1, 0], [0., 1.j]], dtype=complex)
    return QGate(arr, "S")


def tgate() -> 'QGate':
    """ T Gate T^2 = S """
    arr = np.array([[1., 0.], [0., np.exp(1.j * np.pi / 4.)]], dtype=complex)
    return QGate(arr, "T")


def hgate() -> 'QGate':
    """ Hadamard Gate """
    arr = np.array([[1. / np.sqrt(2.), 1. / np.sqrt(2.)],
                    [1. / np.sqrt(2.), -1. / np.sqrt(2.)]], dtype=complex)
    return QGate(arr, "H")


def identity_gate(n=2) -> 'QGate':
    """ Identity matrix 2x2 """
    arr = np.identity(n, dtype=complex)
    return QGate(arr, "I")


def ctrl_gate() -> 'QGate':
    """ Control """
    return QGate(np.identity(2, dtype=complex), "C")


def actrl_gate() -> 'QGate':
    """ Anti-Control """
    return QGate(np.identity(2, dtype=complex), "A")


def cnot10_gate(n, ctrls) -> 'QGate':
    """ CNOT10 """
    arr = get_cnot_ctrl_10(n, ctrls, xgate())
    return QGate(arr, "CNOT10")


def cnot01_gate(n, ctrls) -> 'QGate':
    """ CNOT01 """
    arr = get_cnot_ctrl_01(n, ctrls, xgate())
    return QGate(arr, "CNOT01")


# TODO: why different signature????
def acnot10_gate(n) -> 'QGate':
    """ ACNOT10 """
    arr = get_cnot_actrl_10(n)
    return QGate(arr, "ACNOT10")


# TODO: why different signature????
def acnot01_gate(n) -> 'QGate':
    """ CNOT01 """
    arr = get_cnot_actrl_01(n)
    return QGate(arr, "CNOT01")


def toffoli10_gate(n, ctrls) -> 'QGate':
    """ Toffoli10 """
    arr = get_unitary_gate_10(n, ctrls, xgate()),
    return QGate(arr, "Toffoli10")


def toffoli01_gate(n, ctrls) -> 'QGate':
    """ Toffoli01 """
    arr = get_unitary_gate_01(n, ctrls, xgate()),
    return QGate(arr, "Toffoli01")


def atoffoli10_gate(n, ctrls) -> 'QGate':
    """ AToffoli10 """
    arr = get_unitary_agate_10(n, ctrls, xgate()),
    return QGate(arr, "AToffoli10")


def atoffoli01_gate(n, ctrls) -> 'QGate':
    """ AToffoli01 """
    arr = get_unitary_agate_01(n, ctrls, xgate()),
    return QGate(arr, "AToffoli01")


def swap_gate(n=None) -> 'QGate':
    """ Swap """
    arr = get_generic_swap(n) if n is not None else None;
    return QGate(arr, "W")
