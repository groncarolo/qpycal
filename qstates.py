import numpy as np


class State:
    state = None


def is_normalized(state):
    r = np.conjugate(state.state)
    np.multiply(state.state, r, out=r)
    return np.isclose(np.sum(r), 1.0)


class State0:
    state = np.array([1., 0.])


class State1:
    state = np.array([0., 1.])


class StatePlus:
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


