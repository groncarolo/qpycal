"""
test all simple gates against all basic states
"""
import numpy as np
import pytest

from qgates import xgate, generic_xgate, ygate, zgate, sgate, tgate, hgate, generic_zgate, generic_ygate
from qstates import qstate_0, qstate_1, qstate_plus, qstate_minus, qstate_i, qstate_minus_i

testdata_gates = [
    # X_GATE
    (qstate_0(), xgate(), np.array([0., 1.])),
    (qstate_1(), xgate(), np.array([1., 0.])),
    (qstate_plus(), xgate(), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (qstate_minus(), xgate(), np.array([-1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (qstate_i(), xgate(), np.array([1.j / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (qstate_minus_i(), xgate(), np.array([-1.j / np.sqrt(2.), 1. / np.sqrt(2.)])),

    # Y_GATE
    (qstate_0(), ygate(), np.array([0, 1.j])),
    (qstate_1(), ygate(), np.array([-1.j, 0.])),
    (qstate_plus(), ygate(), np.array([-1.j / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (qstate_minus(), ygate(), np.array([1.j / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (qstate_i(), ygate(), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (qstate_minus_i(), ygate(), np.array([-1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),

    # Z_GATE
    (qstate_0(), zgate(), np.array([1, 0])),
    (qstate_1(), zgate(), np.array([0, -1.])),
    (qstate_plus(), zgate(), np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)])),
    (qstate_minus(), zgate(), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (qstate_i(), zgate(), np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)])),
    (qstate_minus_i(), zgate(), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),

    # S_GATE
    (qstate_0(), sgate(), np.array([1, 0])),
    (qstate_1(), sgate(), np.array([0, 1.j])),
    (qstate_plus(), sgate(), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (qstate_minus(), sgate(), np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)])),
    (qstate_i(), sgate(), np.array([1. / np.sqrt(2.), -1 / np.sqrt(2.)])),
    (qstate_minus_i(), sgate(), np.array([1. / np.sqrt(2.), 1 / np.sqrt(2.)])),

    # T_GATE
    (qstate_0(), tgate(), np.array([1, 0])),
    (qstate_1(), tgate(), np.array([0, np.exp(1.j * np.pi / 4.)])),
    (qstate_plus(), tgate(), np.array([1. / np.sqrt(2.), np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
    (qstate_minus(), tgate(), np.array([1. / np.sqrt(2.), -np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
    (qstate_i(), tgate(), np.array([1. / np.sqrt(2.), 1j * np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
    (qstate_minus_i(), tgate(), np.array([1. / np.sqrt(2.), -1j * np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),

    # H_GATE
    (qstate_0(), hgate(), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (qstate_1(), hgate(), np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)])),
    (qstate_plus(), hgate(), np.array([1, 0])),
    (qstate_minus(), hgate(), np.array([0, 1])),
    (qstate_i(), hgate(), np.array([0.5 + 0.5j, 0.5 - 0.5j])),
    (qstate_minus_i(), hgate(), np.array([0.5 - 0.5j, 0.5 + 0.5j])),

    # generic_xgate
    (qstate_0(), generic_xgate(np.pi), np.array([0., 1.])),
    (qstate_1(), generic_xgate(np.pi), np.array([1., 0.])),
    (qstate_plus(), generic_xgate(np.pi), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (qstate_minus(), generic_xgate(np.pi), np.array([-1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (qstate_i(), generic_xgate(np.pi), np.array([1.j / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (qstate_minus_i(), generic_xgate(np.pi), np.array([-1.j / np.sqrt(2.), 1. / np.sqrt(2.)])),

    (qstate_0(), generic_xgate(np.pi / 2.), np.array([0.5 + 0.5j, 0.5 - 0.5j], dtype=complex)),
    (qstate_1(), generic_xgate(np.pi / 2), np.array([0.5 - 0.5j, 0.5 + 0.5j])),
    (qstate_plus(), generic_xgate(np.pi / 2), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (qstate_minus(), generic_xgate(np.pi / 2), np.array([1.j / np.sqrt(2.), -1.j / np.sqrt(2.)])),
    (qstate_i(), generic_xgate(np.pi / 2), np.array([1 / np.sqrt(2.) + 1.j / np.sqrt(2.), 0.])),
    (qstate_minus_i(), generic_xgate(np.pi / 2), np.array([0., 1. / np.sqrt(2.) - 1.j / np.sqrt(2.)])),

    (qstate_0(), generic_xgate(np.pi / 4), np.array([0.85355339 + 0.35355339j, 0.14644661 - 0.35355339j])),
    (qstate_1(), generic_xgate(np.pi / 4), np.array([0.14644661 - 0.35355339j, 0.85355339 + 0.35355339j])),
    (qstate_plus(), generic_xgate(np.pi / 4), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (qstate_minus(), generic_xgate(np.pi / 4), np.array([0.5 + 0.5j, -0.5 - 0.5j])),
    (qstate_i(), generic_xgate(np.pi / 4), np.array([0.85355339 + 0.35355339j, -0.14644661 + 0.35355339j])),
    (qstate_minus_i(), generic_xgate(np.pi / 4), np.array([0.35355339 + 0.14644661j, 0.35355339 - 0.85355339j])),

    # generic_ygate
    (qstate_0(), generic_ygate(np.pi), np.array([0, 1.j])),
    (qstate_1(), generic_ygate(np.pi), np.array([-1.j, 0.])),
    (qstate_plus(), generic_ygate(np.pi), np.array([-1.j / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (qstate_minus(), generic_ygate(np.pi), np.array([1.j / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (qstate_i(), generic_ygate(np.pi), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (qstate_minus_i(), generic_ygate(np.pi), np.array([-1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),

    (qstate_0(), generic_ygate(np.pi / 2), np.array([0.5 + 0.5j, 0.5 + 0.5j])),
    (qstate_1(), generic_ygate(np.pi / 2), np.array([-0.5 - 0.5j, 0.5 + 0.5j])),
    (qstate_plus(), generic_ygate(np.pi / 2), np.array([0, 1. / np.sqrt(2.) + 1.j / np.sqrt(2.)])),
    (qstate_minus(), generic_ygate(np.pi / 2), np.array([1. / np.sqrt(2.) + 1.j / np.sqrt(2.), 0])),
    (qstate_i(), generic_ygate(np.pi / 2), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (qstate_minus_i(), generic_ygate(np.pi / 2), np.array([1.j / np.sqrt(2.), 1. / np.sqrt(2.)])),

    (qstate_0(), generic_ygate(np.pi / 4), np.array([0.85355339 + 0.35355339j, 0.35355339 + 0.14644661j])),
    (qstate_1(), generic_ygate(np.pi / 4), np.array([-0.35355339 - 0.14644661j, 0.85355339 + 0.35355339j])),
    (qstate_plus(), generic_ygate(np.pi / 4), np.array([+0.35355339 + 0.14644661j, 0.85355339 + 0.35355339j])),
    (qstate_minus(), generic_ygate(np.pi / 4), np.array([0.85355339 + 0.35355339j, -0.35355339 - 0.14644661j])),
    (qstate_i(), generic_ygate(np.pi / 4), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (qstate_minus_i(), generic_ygate(np.pi / 4), np.array([0.5 + 0.5j, 0.5 - 0.5j])),

    # generic_zgate
    (qstate_0(), generic_zgate(np.pi), np.array([1, 0])),
    (qstate_1(), generic_zgate(np.pi), np.array([0, -1.])),
    (qstate_plus(), generic_zgate(np.pi), np.array([1. / np.sqrt(2.), -1. / np.sqrt(2.)])),
    (qstate_minus(), generic_zgate(np.pi), np.array([1. / np.sqrt(2.), 1. / np.sqrt(2.)])),
    (qstate_i(), generic_zgate(np.pi), np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)])),
    (qstate_minus_i(), generic_zgate(np.pi), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),

    (qstate_0(), generic_zgate(np.pi / 2), np.array([1, 0])),
    (qstate_1(), generic_zgate(np.pi / 2), np.array([0, 1.j])),
    (qstate_plus(), generic_zgate(np.pi / 2), np.array([1. / np.sqrt(2.), 1.j / np.sqrt(2.)])),
    (qstate_minus(), generic_zgate(np.pi / 2), np.array([1. / np.sqrt(2.), -1.j / np.sqrt(2.)])),
    (qstate_i(), generic_zgate(np.pi / 2), np.array([1. / np.sqrt(2.), -1 / np.sqrt(2.)])),
    (qstate_minus_i(), generic_zgate(np.pi / 2), np.array([1. / np.sqrt(2.), 1 / np.sqrt(2.)])),

    (qstate_0(), generic_zgate(np.pi / 4), np.array([1, 0])),
    (qstate_1(), generic_zgate(np.pi / 4), np.array([0, np.exp(1.j * np.pi / 4.)])),
    (qstate_plus(), generic_zgate(np.pi / 4), np.array([1. / np.sqrt(2.), np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
    (qstate_minus(), generic_zgate(np.pi / 4), np.array([1. / np.sqrt(2.), -np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
    (qstate_i(), generic_zgate(np.pi / 4), np.array([1. / np.sqrt(2.), 1j * np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
    (qstate_minus_i(), generic_zgate(np.pi / 4), np.array([1. / np.sqrt(2.), -1j * np.exp(1.j * np.pi / 4.) / np.sqrt(2.)])),
]


@pytest.mark.parametrize("state,gate,result", testdata_gates)
def test_gates(state, gate, result):
    ret = gate.apply(state)
    assert np.allclose(ret, result)
