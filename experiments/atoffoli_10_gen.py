import numpy as np
import ctypes

np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)



np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)


gnot = np.array([[0., 1.], [1., 0.]]) # not

class State:
    def __init__(self, state, label="", name=""):
        self.state = state
        self.label = label
        self.name = name


class State0(State):
    def __init__(self, name=""):
        super().__init__(np.array([1., 0.]),
                         "|0>", name)


class State1(State):
    def __init__(self, name=""):
        super().__init__(np.array([0., 1.]),
                         "|1>", name)




zero = State0().state
one = State1().state
E00 = np.outer(zero, np.conjugate(zero).T)
E01 = np.outer(zero, np.conjugate(one).T)
E10 = np.outer(one, np.conjugate(zero).T)
E11 = np.outer(one, np.conjugate(one).T)
ide2 = np.identity(2)



def get_unitary_agate_10(how_many_bits, ctrls, gate):
    print("get_unitary_agate_10 ")
    print(ctrls)

    state_shape = 2 ** how_many_bits
    idex = np.identity(state_shape // 4, dtype=complex)
    ret = np.zeros((state_shape, state_shape), dtype=complex)

    if how_many_bits == 2:
        ret = np.kron(E11, gate)
    else:
        for i in range(2 ** (how_many_bits - 2)):  # 8
            #print("CALCULATING " + str(i))
            binary = "{0:>0{1}b}".format(i, how_many_bits - 2)
            #print(binary)

            if i in ctrls:
                #print("NOTTTTTTTTT " + str(i))
                pr = gate
            else:
                pr = np.identity(2)

            # we read it in reversed order to
            # match endianness of bit we want to
            # turn ON as control
            for c in reversed(binary):
                #print("mult")
                pr = np.kron(E11 if c == '0' else E00, pr)
            pr = np.kron(E00, pr)
            ret += pr

    idex = np.identity(state_shape // 4, dtype=complex)
    ide2 = np.identity(2, dtype=complex)
    a = np.kron(E11, np.kron(idex, ide2))
    ret = ret + a
    print(ret)
    return ret

##########################################################################
# # X
# # A
# # A
##########################################################################
g = np.array([
              [0.,1.,0.,0., 0.,0.,0.,0.],
              [1.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,1.,0., 0.,0.,0.,0.],
              [0.,0.,0.,1., 0.,0.,0.,0.],

              [0.,0.,0.,0., 1.,0.,0.,0.],
              [0.,0.,0.,0., 0.,1.,0.,0.],
              [0.,0.,0.,0., 0.,0.,1.,0.],
              [0.,0.,0.,0., 0.,0.,0.,1.],
]) # toffoli
print ("X")
print ("A")
print ("A")
t = get_unitary_agate_10(3, [1,2], gnot)
assert np.allclose(t,g)
print ("OK")
##########################################################################


#########################################################################
# X
# A
# I
# A
##########################################################################
g = np.array([
              [0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0, 0.,0.,0.,0],
              [1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0, 0.,0.,0.,0],
              [0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0, 0.,0.,0.,0],
              [0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0, 0.,0.,0.,0],

              [0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0, 0.,0.,0.,0],
              [0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0, 0.,0.,0.,0],
              [0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0, 0.,0.,0.,0],
              [0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0, 0.,0.,0.,0],

              [0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0, 0.,0.,0.,0],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0, 0.,0.,0.,0],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0, 0.,0.,0.,0],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1, 0.,0.,0.,0],

              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0, 1.,0.,0.,0],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0, 0.,1.,0.,0],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0, 0.,0.,1.,0],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0, 0.,0.,0.,1],
]) # toffoli
print ("X")
print ("A")
print ("I")
print ("A")
t = get_unitary_agate_10(4, [1,3], gnot)
assert np.allclose(t,g)
print ("OK")
##########################################################################




# X
# I
# A
# A
g = np.array([
              [0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0, 0.,0.,0.,0],
              [1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0, 0.,0.,0.,0],
              [0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0, 0.,0.,0.,0],
              [0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0, 0.,0.,0.,0],

              [0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0, 0.,0.,0.,0],
              [0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0, 0.,0.,0.,0],
              [0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0, 0.,0.,0.,0],
              [0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0, 0.,0.,0.,0],

              [0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0, 0.,0.,0.,0],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0, 0.,0.,0.,0],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0, 0.,0.,0.,0],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1, 0.,0.,0.,0],

              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0, 1.,0.,0.,0],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0, 0.,1.,0.,0],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0, 0.,0.,1.,0],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0, 0.,0.,0.,1],
]) # toffoli
print ("X")
print ("I")
print ("A")
print ("A")
t = get_unitary_agate_10(4, [2,3], gnot)
assert np.allclose(t,g)
print ("OK")
