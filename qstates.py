import numpy as np


class State:
    '''
    Class Representing a quantum state
    '''

    def __init__(self, state, label="", name=""):
        self.state = state
        self.label = label
        self.name = name


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

    def __init__(self, name=""):
        super().__init__(np.array([1., 0.], dtype=complex),
                         "|0>", name)


class State1(State):
    '''
    State |1>
    '''

    def __init__(self, name=""):
        super().__init__(np.array([0., 1.], dtype=complex),
                         "|1>", name)


class StatePlus(State):
    '''
    State |+>
    '''

    def __init__(self, name=""):
        super().__init__(np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)], dtype=complex),
                         "|+>", name)


class StateMinus(State):
    '''
    State |->
    '''

    def __init__(self, name=""):
        super().__init__(np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)], dtype=complex),
                         "|->", name)


class StateI(State):
    '''
    State |i>
    '''

    def __init__(self, name=""):
        super().__init__(np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)], dtype=complex),
                         "|i>", name)


class StateMinusI(State):
    '''
    State |-i>
    '''

    def __init__(self, name=""):
        super().__init__(np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)], dtype=complex),
                         "|-i>", name)
