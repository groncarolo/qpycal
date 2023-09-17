import numpy as np


# i control j target
# C
# U
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
    out2 = np.outer(one, np.conjugate(one).T)
    b = np.kron(np.kron(out2, iden), gate)
    result_gate = a + b
    return result_gate


def get_cnot_actrl_10(state_shape):
    zero = np.array([1., 0.])
    one = np.array([0., 1.])
    ide2 = np.identity(2)
    idex = np.identity(state_shape // 4)

    E00 = np.outer(zero, np.conjugate(zero).T)
    E11 = np.outer(one, np.conjugate(one).T)

    gnot = np.array([[0., 1.], [1., 0.]])  # not

    a = np.kron(E00, np.kron(idex, gnot))
    b = np.kron(E11, np.kron(idex, ide2))

    return a + b


# cnot ij i control j target
# A
# X
def get_cnot_actrl_01(state_shape):
    zero = np.array([1., 0.])
    one = np.array([0., 1.])
    ide2 = np.identity(state_shape // 2)
    idex = np.identity(state_shape // 4)

    E00 = np.outer(zero, np.conjugate(zero).T)
    E01 = np.outer(zero, np.conjugate(one).T)
    E10 = np.outer(one, np.conjugate(zero).T)
    E11 = np.outer(one, np.conjugate(one).T)

    a = np.kron(ide2, E11)
    b = np.kron(np.kron(E10, idex), E00)
    c = np.kron(np.kron(E01, idex), E00)
    return a + b + c


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
