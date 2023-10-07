import numpy as np

from qstates import State0, State1

zero = State0().state
one = State1().state
E00 = np.outer(zero, np.conjugate(zero).T)
E01 = np.outer(zero, np.conjugate(one).T)
E10 = np.outer(one, np.conjugate(zero).T)
E11 = np.outer(one, np.conjugate(one).T)
ide2 = np.identity(2, dtype=complex)


def get_cnot_ctrl_10(how_many_bits, ctrls, gate):
    '''
    get a CNOT like
    # C
    # .
    # .
    # X
    '''
    state_shape = 2 ** how_many_bits
    idex = np.identity(state_shape // 4)
    out = np.outer(zero, np.conjugate(zero).T)
    a = np.kron(np.kron(out, ide2), idex)
    out2 = np.outer(one, np.conjugate(one).T)
    b = np.kron(np.kron(out2, idex), gate)
    r = a + b
    return r


def get_cnot_actrl_10(state_shape):
    '''
    get a CNOT like
    # A
    # .
    # .
    # X
    '''
    idex = np.identity(state_shape // 4, dtype=complex)
    gnot = np.array([[0., 1.], [1., 0.]], dtype=complex)  # not
    a = np.kron(E00, np.kron(idex, gnot))
    b = np.kron(E11, np.kron(idex, ide2))
    return a + b


# U
# C
def get_unitary_gate_10(how_many_bits, ctrls, gate):
    '''
    get a TOFFOLI like
    # C
    # .
    # .
    # C
    # .
    # .
    # X
    '''
    state_shape = 2 ** how_many_bits
    ret = np.zeros((state_shape, state_shape), dtype=complex)

    for i in range(2 ** (how_many_bits - 2)):  # 8
        binary = "{0:>0{1}b}".format(i, how_many_bits - 2)
        print(binary)

        if i in ctrls:
            pr = gate
        else:
            pr = np.identity(2)

        # we read it in reversed order to
        # match endianness of bit we want to
        # turn ON as control
        for c in reversed(binary):
            pr = np.kron(E00 if c == '0' else E11, pr)
        pr = np.kron(E11, pr)
        ret += pr

    idex = np.identity(state_shape // 4, dtype=complex)
    a = np.kron(E00, np.kron(idex, ide2))
    ret = ret + a
    return ret


def get_unitary_agate_10(how_many_bits, ctrls, gate):
    '''
    get a TOFFOLI like
    # A
    # .
    # .
    # A
    # .
    # .
    # X
    '''
    state_shape = 2 ** how_many_bits
    ret = np.zeros((state_shape, state_shape), dtype=complex)

    if how_many_bits == 2:
        ret = np.kron(E11, gate)
    else:
        for i in range(2 ** (how_many_bits - 2)):  # 8
            binary = "{0:>0{1}b}".format(i, how_many_bits - 2)
            if i in ctrls:
                pr = gate
            else:
                pr = np.identity(2)

            # we read it in reversed order to
            # match endianness of bit we want to
            # turn ON as control
            for c in reversed(binary):
                pr = np.kron(E11 if c == '0' else E00, pr)
            pr = np.kron(E00, pr)
            ret += pr

    idex = np.identity(state_shape // 4, dtype=complex)
    a = np.kron(E11, np.kron(idex, ide2))
    ret = ret + a
    return ret


def get_cnot_ctrl_01(how_many_bits, ctrls, gate):
    '''
    get a CNOT like
    # X
    # .
    # .
    # C
    '''
    state_shape = 2 ** how_many_bits
    iden = np.identity(state_shape // 4, dtype=complex)
    out = np.outer(zero, np.conjugate(zero).T)
    a = np.kron(np.kron(ide2, iden), out)
    out2 = np.outer(one, np.conjugate(one).T)
    b = np.kron(np.kron(gate, iden), out2)
    result_gate = a + b
    return result_gate


def get_cnot_actrl_01(state_shape):
    '''
    get a CNOT like
    # X
    # .
    # .
    # A
    '''
    iden = np.identity(state_shape // 2, dtype=complex)
    idex = np.identity(state_shape // 4, dtype=complex)

    a = np.kron(iden, E11)
    b = np.kron(np.kron(E10, idex), E00)
    c = np.kron(np.kron(E01, idex), E00)
    return a + b + c


def get_unitary_gate_01(how_many_bits, ctrls, gate):
    '''
    get a TOFFOLI like
    # X
    # .
    # .
    # C
    # .
    # .
    # C
    '''
    state_shape = 2 ** how_many_bits
    if ctrls[0] - ctrls[1] == 1:
        x = 2 ** ctrls[1]
        r = np.kron(np.identity(x), np.kron(E00, np.identity(2)))
        r = r + np.kron(np.identity(x), np.kron(E11, E00))
        r = r + np.kron(np.kron(np.kron(E01, np.identity(x // 2)), E11), E11)
        r = r + np.kron(np.kron(np.kron(E10, np.identity(x // 2)), E11), E11)
    elif ctrls[1] == 1:
        x = state_shape // 8
        r = np.kron(np.kron(np.kron(E01, E11), np.identity(x)), E11)  # OK
        r = r + np.kron(np.kron(np.kron(E10, E11), np.identity(x)), E11)  # OK
        r = r + np.kron(E00, np.kron(E00, np.kron(ide2, np.identity(x))))
        r = r + np.kron(E11, np.kron(E00, np.kron(ide2, np.identity(x))))
        r = r + np.kron(E00, np.kron(E11, np.kron(np.identity(x), E00)))
        r = r + np.kron(E11, np.kron(E11, np.kron(np.identity(x), E00)))  # WORKS!
    else:
        b = 2 ** (ctrls[0] - ctrls[1]) // 2
        a = (2 ** ctrls[1]) // 2

        r = np.kron(E01, np.kron(np.identity(a), np.kron(np.kron(E11, np.identity(b)), E11)))
        r = r + np.kron(E10, np.kron(np.identity(a), np.kron(np.kron(E11, np.identity(b)), E11)))
        for i in np.where(r.any(axis=1) == 0.)[0]:
            r[i, i] = 1
    return r


def get_unitary_agate_01(how_many_bits, ctrls, gate):
    '''
    get a TOFFOLI like
    # X
    # .
    # .
    # A
    # .
    # .
    # A
    '''
    state_shape = 2 ** how_many_bits
    if ctrls[0] - ctrls[1] == 1:
        x = 2 ** ctrls[1]
        r = np.kron(np.identity(x), np.kron(E11, np.identity(2)))
        r = r + np.kron(np.identity(x), np.kron(E00, E11))
        r = r + np.kron(np.kron(np.kron(E01, np.identity(x // 2)), E00), E00)
        r = r + np.kron(np.kron(np.kron(E10, np.identity(x // 2)), E00), E00)
    elif ctrls[1] == 1:
        x = state_shape // 8
        r = np.kron(np.kron(np.kron(E01, E00), np.identity(x)), E00)  # OK
        r = r + np.kron(np.kron(np.kron(E10, E00), np.identity(x)), E00)  # OK
        r = r + np.kron(E11, np.kron(E11, np.kron(ide2, np.identity(x))))
        r = r + np.kron(E00, np.kron(E11, np.kron(ide2, np.identity(x))))
        r = r + np.kron(E11, np.kron(E00, np.kron(np.identity(x), E11)))
        r = r + np.kron(E00, np.kron(E00, np.kron(np.identity(x), E11)))  # WORKS!
    else:
        b = 2 ** (ctrls[0] - ctrls[1]) // 2
        a = (2 ** ctrls[1]) // 2

        r = np.kron(E01, np.kron(np.identity(a), np.kron(np.kron(E00, np.identity(b)), E00)))
        r = r + np.kron(E10, np.kron(np.identity(a), np.kron(np.kron(E00, np.identity(b)), E00)))
        for i in np.where(r.any(axis=1) == 0.)[0]:
            r[i, i] = 1
    return r


# SWAP1,3=|0⟩⟨0|⊗I⊗|0⟩⟨0|+E01⊗I⊗E10+E10⊗I⊗E01+|1⟩⟨1|⊗I⊗|1⟩⟨1|
def get_generic_swap(state_shape):
    '''
    get a swap gate
    '''
    idex = np.identity(state_shape // 4, dtype=complex)
    out0 = np.outer(zero, np.conjugate(zero).T)
    a = np.kron(np.kron(out0, idex), out0)
    b = np.kron(np.kron(E01, idex), E10)
    c = np.kron(np.kron(E10, idex), E01)
    out3 = np.outer(one, np.conjugate(one).T)
    d = np.kron(np.kron(out3, idex), out3)
    r = a + b + c + d
    return r
