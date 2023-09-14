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


# SWAP1,3=|0⟩⟨0|⊗I⊗|0⟩⟨0|+E01⊗I⊗E10+E10⊗I⊗E01+|1⟩⟨1|⊗I⊗|1⟩⟨1|
def get_generic_swap(state_shape):
    zero = np.array([1., 0.])
    one = np.array([0., 1.])
    ide2 = np.identity(state_shape // 4)  # needs correct number!
    out0 = np.outer(zero, np.conjugate(zero).T)
    a = np.kron(np.kron(out0, ide2), out0)
    E01 = np.outer(zero, np.conjugate(one).T)
    E10 = np.outer(one, np.conjugate(zero).T)
    b = np.kron(np.kron(E01, ide2), E10)
    c = np.kron(np.kron(E10, ide2), E01)
    out3 = np.outer(one, np.conjugate(one).T)
    d = np.kron(np.kron(out3, ide2), out3)
    r = a + b + c + d
    return r
