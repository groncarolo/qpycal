'''
test all simple gates against all basic states
'''
import numpy as np
import pytest

from qgates import XGate, YGate, ZGate, SGate, TGate, HGate, apply_gate, GenericZGate, GenericXGate, GenericYGate
from qstates import State0, StatePlus, State1, StateMinus, StateMinusI, StateI

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
    (StateI(), HGate(), np.array([0.5 + 0.5j, 0.5 - 0.5j])),
    (StateMinusI(), HGate(), np.array([0.5 - 0.5j, 0.5 + 0.5j])),

    # GenericXGate
    (State0(), GenericXGate(np.pi), np.array([0., 1.])),
    (State1(), GenericXGate(np.pi), np.array([1., 0.])),
    (StatePlus(), GenericXGate(np.pi), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (StateMinus(), GenericXGate(np.pi), np.array([-1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (StateI(), GenericXGate(np.pi), np.array([1.j / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (StateMinusI(), GenericXGate(np.pi), np.array([-1.j / np.sqrt(2.), 1. / np.sqrt(2.)])),

    (State0(), GenericXGate(np.pi / 2.), np.array([0.5 + 0.5j, 0.5 - 0.5j], dtype=complex)),
    (State1(), GenericXGate(np.pi / 2), np.array([0.5 - 0.5j, 0.5 + 0.5j])),
    (StatePlus(), GenericXGate(np.pi / 2), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (StateMinus(), GenericXGate(np.pi / 2), np.array([1.j / np.sqrt(2.), -1.j / np.sqrt(2.)])),
    (StateI(), GenericXGate(np.pi / 2), np.array([1 / np.sqrt(2.) + 1.j / np.sqrt(2.), 0.])),
    (StateMinusI(), GenericXGate(np.pi / 2), np.array([0., 1. / np.sqrt(2.) - 1.j / np.sqrt(2.)])),

    (State0(), GenericXGate(np.pi / 4), np.array([0.85355339 + 0.35355339j, 0.14644661 - 0.35355339j])),
    (State1(), GenericXGate(np.pi / 4), np.array([0.14644661 - 0.35355339j, 0.85355339 + 0.35355339j])),
    (StatePlus(), GenericXGate(np.pi / 4), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (StateMinus(), GenericXGate(np.pi / 4), np.array([0.5 + 0.5j, -0.5 - 0.5j])),
    (StateI(), GenericXGate(np.pi / 4), np.array([0.85355339 + 0.35355339j, -0.14644661 + 0.35355339j])),
    (StateMinusI(), GenericXGate(np.pi / 4), np.array([0.35355339 + 0.14644661j, 0.35355339 - 0.85355339j])),

    # GenericYGate
    (State0(), GenericYGate(np.pi), np.array([0, 1.j])),
    (State1(), GenericYGate(np.pi), np.array([-1.j, 0.])),
    (StatePlus(), GenericYGate(np.pi), np.array([-1.j / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (StateMinus(), GenericYGate(np.pi), np.array([1.j / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (StateI(), GenericYGate(np.pi), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (StateMinusI(), GenericYGate(np.pi), np.array([-1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),

    (State0(), GenericYGate(np.pi / 2), np.array([0.5 + 0.5j, 0.5 + 0.5j])),
    (State1(), GenericYGate(np.pi / 2), np.array([-0.5 - 0.5j, 0.5 + 0.5j])),
    (StatePlus(), GenericYGate(np.pi / 2), np.array([0, 1. / np.sqrt(2.) + 1.j / np.sqrt(2.)])),
    (StateMinus(), GenericYGate(np.pi / 2), np.array([1. / np.sqrt(2.) + 1.j / np.sqrt(2.), 0])),
    (StateI(), GenericYGate(np.pi / 2), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (StateMinusI(), GenericYGate(np.pi / 2), np.array([1.j / np.sqrt(2.), 1. / np.sqrt(2.)])),

    (State0(), GenericYGate(np.pi / 4), np.array([0.85355339 + 0.35355339j, 0.35355339 + 0.14644661j])),
    (State1(), GenericYGate(np.pi / 4), np.array([-0.35355339 - 0.14644661j, 0.85355339 + 0.35355339j])),
    (StatePlus(), GenericYGate(np.pi / 4), np.array([+0.35355339 + 0.14644661j, 0.85355339 + 0.35355339j])),
    (StateMinus(), GenericYGate(np.pi / 4), np.array([0.85355339 + 0.35355339j, -0.35355339 - 0.14644661j])),
    (StateI(), GenericYGate(np.pi / 4), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (StateMinusI(), GenericYGate(np.pi / 4), np.array([0.5 + 0.5j, 0.5 - 0.5j])),

    # GenericZGate
    (State0(), GenericZGate(np.pi), np.array([1, 0])),
    (State1(), GenericZGate(np.pi), np.array([0, -1.])),
    (StatePlus(), GenericZGate(np.pi), np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)])),
    (StateMinus(), GenericZGate(np.pi), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (StateI(), GenericZGate(np.pi), np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)])),
    (StateMinusI(), GenericZGate(np.pi), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),

    (State0(), GenericZGate(np.pi / 2), np.array([1, 0])),
    (State1(), GenericZGate(np.pi / 2), np.array([0, 1.j])),
    (StatePlus(), GenericZGate(np.pi / 2), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (StateMinus(), GenericZGate(np.pi / 2), np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)])),
    (StateI(), GenericZGate(np.pi / 2), np.array([1. / np.sqrt(2.), -1 / np.sqrt(2.)])),
    (StateMinusI(), GenericZGate(np.pi / 2), np.array([1. / np.sqrt(2.), 1 / np.sqrt(2.)])),

    (State0(), GenericZGate(np.pi / 4), np.array([1, 0])),
    (State1(), GenericZGate(np.pi / 4), np.array([0, np.exp(1.j * np.pi / 4.)])),
    (StatePlus(), GenericZGate(np.pi / 4), np.array([1. / np.sqrt(2.), np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
    (StateMinus(), GenericZGate(np.pi / 4), np.array([1. / np.sqrt(2.), -np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
    (StateI(), GenericZGate(np.pi / 4), np.array([1. / np.sqrt(2.), 1j * np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
    (
        StateMinusI(), GenericZGate(np.pi / 4),
        np.array([1. / np.sqrt(2.), -1j * np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),

]


@pytest.mark.parametrize("state,g,t", testdata_gates)
def test_gates(state, g, t):
    rstate = apply_gate(g, state.state)
    assert np.allclose(rstate, t)
