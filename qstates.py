import numpy as np


class State:
    '''
    Class Representing a quantum state
    '''
    state = None
    name = ""

    def __init__(self, s):
        self.state = s


def is_state_normalized(state):
    '''
    returns if the state is normalized
    meaning |a|^2+|b|^2 = 1
    :param state: state to be checked
    :return: if the state is normalized
    '''
    r = np.conjugate(state.state)
    np.multiply(state.state, r, out=r)
    return np.isclose(np.sum(r), 1.0)


class State0(State):
    '''
    State |0>
    '''
    label = "|0>"
    state = np.array([1., 0.])

    def __init__(self):
        pass


class State1(State):
    '''
    State |1>
    '''
    label = "|1>"
    state = np.array([0., 1.])

    def __init__(self):
        pass


class StatePlus(State):
    '''
    State |+>
    '''
    label = "|+>"
    state = np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])

    def __init__(self):
        pass


class StateMinus(State):
    '''
    State |->
    '''
    label = "|->"
    state = np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)])

    def __init__(self):
        pass


class StateI(State):
    '''
    State |i>
    '''
    label = "|i>"
    state = np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])

    def __init__(self):
        pass


class StateMinusI(State):
    '''
    State |-i>
    '''
    label = "|-i>"
    state = np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)])

    def __init__(self):
        pass
