import logging
import numpy as np


# i control j target
# U
# X
def get_unitary_gate_01(state_shape, gate):
    zero = np.array([1., 0.])
    one = np.array([0., 1.])
    ide2 = np.identity(2)
    iden = np.identity(state_shape // 4)
    out = np.outer(zero, np.conjugate(zero).T)
    a = np.kron(np.kron(ide2, iden), out)
    out2 = np.outer(one, np.conjugate(one).T)
    b = np.kron(np.kron(gate, iden), out2)
    result_gate = a + b
    return result_gate


# i control j target
# U
# C
def get_unitary_gate_10(state_shape, gate):
    zero = np.array([1., 0.])
    one = np.array([0., 1.])
    ide2 = np.identity(2)
    iden = np.identity(state_shape // 4)
    out = np.outer(zero, np.conjugate(zero).T)
    a = np.kron(np.kron(out, ide2), iden)
    logging.info(a.shape)
    out2 = np.outer(one, np.conjugate(one).T)
    b = np.kron(np.kron(out2, iden), gate)
    logging.info(b.shape)
    result_gate = a + b
    return result_gate
