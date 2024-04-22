"""
>>> s = qstate_0()
>>> s
QState(state=array([1.+0.j, 0.+0.j]), label='|0>', name='')
>>> s.is_normalized()
True
>>> s1 = qstate_1()
>>> s1 == s
False
>>> zero = qstate_0()
>>> one = qstate_1()
>>> type(np.conjugate(zero))
<class 'numpy.ndarray'>
>>> E00 = np.outer(zero, np.conjugate(zero).T)
>>> E00
array([[1.+0.j, 0.+0.j],
       [0.+0.j, 0.+0.j]])
>>> type(E00)
<class 'numpy.ndarray'>
>>> E01 = np.outer(zero, np.conjugate(one).T)
>>> E01
array([[0.+0.j, 1.+0.j],
       [0.+0.j, 0.+0.j]])
>>> E10 = np.outer(one, np.conjugate(zero).T)
>>> E10
array([[0.+0.j, 0.+0.j],
       [1.+0.j, 0.+0.j]])
>>> E11 = np.outer(one, np.conjugate(one).T)
>>> E11
array([[0.+0.j, 0.+0.j],
       [0.+0.j, 1.+0.j]])
"""
from dataclasses import dataclass
import numpy as np

@dataclass(eq=False)
class QState:
    """
    Class Representing a quantum state
    """
    state: np.ndarray
    label: str = str()
    name: str = str()

    def __array__(self):
        return self.state

    #@property
    # def label(self):
    #     return self._label

    # @property
    # def name(self):
    #     return self._name
    # @property
    # def state(self):
    #     return self._state

    def __len__(self):
        return len(self.state)
    def __iter__(self):
        return iter(self.state)

    def __eq__(self, other):
        return (self.state.shape == other.state.shape and
                (self.state == other.state).all())

    def is_normalized(self):
        """
        returns if the state is normalized
        meaning |a|^2+|b|^2 = 1
        :return: if the state is normalized
        """
        r = np.conjugate(self)
        np.multiply(self, r, out=r)
        return np.isclose(np.sum(r), 1.0)


def qstate_0() -> 'QState':
    """ QState |0> """
    return QState(np.array([1., 0.], dtype=complex), "|0>")


def qstate_1() -> 'QState':
    """ QState |1> """
    return QState(np.array([0., 1.], dtype=complex), "|1>")


def qstate_plus() -> 'QState':
    """ QState |+> """
    return QState(np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)], dtype=complex), "|+>")


def qstate_minus() -> 'QState':
    """ QState |-> """
    return QState(np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)], dtype=complex), "|->")


def qstate_i() -> 'QState':
    """ QState |i> """
    return QState(np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)], dtype=complex), "|i>")


def qstate_minus_i() -> 'QState':
    """ QState |-i> """
    return QState(np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)], dtype=complex), "|-i>")
