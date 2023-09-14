import numpy as np
import logging


class State:
    state = None

    def __init__(self, s):
        self.state = s


def is_normalized(state):
    r = np.conjugate(state.state)
    np.multiply(state.state, r, out=r)
    return np.isclose(np.sum(r), 1.0)


class State0:
    label = "|0>"
    state = np.array([1., 0.])


class State1:
    label = "|1>"
    state = np.array([0., 1.])


class StatePlus:
    label = "|+>"
    state = np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])


class StateMinus:
    label = "|->"
    state = np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)])


class StateI:
    label = "|i>"
    state = np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])


class StateMinusI:
    label = "|-i>"
    state = np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)])


# i control j target
# U
# X
def get_U_01(state_shape, gate):
    zero = np.array([1., 0.])
    one = np.array([0., 1.])
    ide2 = np.identity(2)
    idex = np.identity(state_shape // 4)
    out = np.outer(zero, np.conjugate(zero).T)
    a = np.kron(np.kron(ide2, idex), out)
    out2 = np.outer(one, np.conjugate(one).T)
    b = np.kron(np.kron(gate, idex), out2)
    g0 = a + b
    g0.shape
    return g0


# i control j target
# U
# C
def get_U_10(state_shape, gate):
    zero = np.array([1., 0.])
    one = np.array([0., 1.])
    ide2 = np.identity(2)
    idex = np.identity(state_shape // 4)
    out = np.outer(zero, np.conjugate(zero).T)
    a = np.kron(np.kron(out, ide2), idex)
    logging.info(a.shape)
    out2 = np.outer(one, np.conjugate(one).T)
    b = np.kron(np.kron(out2, idex), gate)
    logging.info(b.shape)
    g0 = a + b
    g0.shape
    return g0
