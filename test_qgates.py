'''
test all simple gates against all basic states
'''
import numpy as np
import pytest

from qgates import XGate, YGate, ZGate, SGate, TGate, HGate, apply_gate, GenericZGate
from qstates import State0, StatePlus, State1, StateMinus, StateMinusI, StateI
from qutils import complex_2_spherical_coordinates, print_spherical_coordinates

testdata_gates = [
    # X_GATE
    (State0(), XGate(), np.array([0., 1.])),
    (State1(), XGate(), np.array([1., 0.])),
    (StatePlus(), XGate(), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (StateMinus(), XGate(), np.array([-1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (StateI(), XGate(), np.array([1.j / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (StateMinusI(), XGate(), np.array([-1.j / np.sqrt(2.), 1. / np.sqrt(2.)])),

    # Y_GATE
    (State0(), YGate(), np.array([0, 1.j])),
    (State1(), YGate(), np.array([-1.j, 0.])),
    (StatePlus(), YGate(), np.array([-1.j / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (StateMinus(), YGate(), np.array([1.j / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (StateI(), YGate(), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (StateMinusI(), YGate(), np.array([-1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),

    # Z_GATE
    (State0(), ZGate(), np.array([1, 0])),
    (State1(), ZGate(), np.array([0, -1.])),
    (StatePlus(), ZGate(), np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)])),
    (StateMinus(), ZGate(), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (StateI(), ZGate(), np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)])),
    (StateMinusI(), ZGate(), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),

    # S_GATE
    (State0(), SGate(), np.array([1, 0])),
    (State1(), SGate(), np.array([0, 1.j])),
    (StatePlus(), SGate(), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (StateMinus(), SGate(), np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)])),
    (StateI(), SGate(), np.array([1. / np.sqrt(2.), -1 / np.sqrt(2.)])),
    (StateMinusI(), SGate(), np.array([1. / np.sqrt(2.), 1 / np.sqrt(2.)])),

    # T_GATE
    (State0(), TGate(), np.array([1, 0])),
    (State1(), TGate(), np.array([0, np.exp(1.j * np.pi / 4.)])),
    (StatePlus(), TGate(), np.array([1. / np.sqrt(2.), np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
    (StateMinus(), TGate(), np.array([1. / np.sqrt(2.), -np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
    (StateI(), TGate(), np.array([1. / np.sqrt(2.), 1j * np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
    (StateMinusI(), TGate(), np.array([1. / np.sqrt(2.), -1j * np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),

    # H_GATE
    (State0(), HGate(), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (State1(), HGate(), np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)])),
    (StatePlus(), HGate(), np.array([1, 0])),
    (StateMinus(), HGate(), np.array([0, 1])),
    (StateI(), HGate(), np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)])),
    (StateMinusI(), HGate(), np.array([1. / np.sqrt(2.), +1.j / np.sqrt(2.)])),

    # GenericZGate
    (StatePlus(), GenericZGate(np.pi), np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)])),
    (StatePlus(), GenericZGate(np.pi / 2.0), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (StatePlus(), GenericZGate(np.pi / 4.0), np.array([1. / np.sqrt(2.), np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),

    (StateI(), GenericZGate(np.pi), np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)])),
    (StateI(), GenericZGate(np.pi / 2.0), np.array([1. / np.sqrt(2.), -1 / np.sqrt(2.)])),
    (StateI(), GenericZGate(np.pi / 4.0), np.array([1. / np.sqrt(2.), 1j * np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),

]


@pytest.mark.parametrize("state,g,t", testdata_gates)
def test_gates(state, g, t):
    r = complex_2_spherical_coordinates(state.state)
    print("")
    print_spherical_coordinates(r)

    rstate = apply_gate(g, state.state)
    c = complex_2_spherical_coordinates(rstate)
    print_spherical_coordinates(c)
    assert np.allclose(rstate, t)
