import numpy as np

from qstates import State0, State1

zero = State0().state
one = State1().state
E00 = np.outer(zero, np.conjugate(zero).T)
E01 = np.outer(zero, np.conjugate(one).T)
E10 = np.outer(one, np.conjugate(zero).T)
E11 = np.outer(one, np.conjugate(one).T)
ide2 = np.identity(2, dtype=complex)


# i control j target
# C
# U
def get_unitary_gate_01(state_shape, gate):
    iden = np.identity(state_shape // 4, dtype=complex)
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
    idex = np.identity(state_shape // 4, dtype=complex)
    out = np.outer(zero, np.conjugate(zero).T)
    a = np.kron(np.kron(out, ide2), idex)
    out2 = np.outer(one, np.conjugate(one).T)
    b = np.kron(np.kron(out2, idex), gate)
    result_gate = a + b
    return result_gate


def get_cnot_actrl_10(state_shape):
    idex = np.identity(state_shape // 4, dtype=complex)

    gnot = np.array([[0., 1.], [1., 0.]], dtype=complex)  # not

    a = np.kron(E00, np.kron(idex, gnot))
    b = np.kron(E11, np.kron(idex, ide2))

    return a + b


# cnot ij i control j target
# A
# X
def get_cnot_actrl_01(state_shape):
    iden = np.identity(state_shape // 2, dtype=complex)
    idex = np.identity(state_shape // 4, dtype=complex)

    a = np.kron(iden, E11)
    b = np.kron(np.kron(E10, idex), E00)
    c = np.kron(np.kron(E01, idex), E00)
    return a + b + c


# SWAP1,3=|0⟩⟨0|⊗I⊗|0⟩⟨0|+E01⊗I⊗E10+E10⊗I⊗E01+|1⟩⟨1|⊗I⊗|1⟩⟨1|
def get_generic_swap(state_shape):
    idex = np.identity(state_shape // 4, dtype=complex)  # needs correct number!
    out0 = np.outer(zero, np.conjugate(zero).T)
    a = np.kron(np.kron(out0, idex), out0)
    b = np.kron(np.kron(E01, idex), E10)
    c = np.kron(np.kron(E10, idex), E01)
    out3 = np.outer(one, np.conjugate(one).T)
    d = np.kron(np.kron(out3, idex), out3)
    r = a + b + c + d
    return r
