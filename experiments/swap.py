import numpy as np


# GateSwap = np.array([[1., 0.,0.,0.], [0., 0.,1.,0.],[0., 1.,0.,0.],[0., 0.,0.,1.]])
# s = np.array([1.0, 2.0, 3., 4.])
# r = np.dot(GateSwap, s)
# assert np.allclose(r, np.array([1., 3., 2., 4.]))
# print (r)



input0 = np.array([0.,1.])
input1 = np.array([1./np.sqrt(2.),1./np.sqrt(2.)])
input2 = np.array([1.,0.])
state = np.kron(np.kron(input2, input1), input0)
print (state)
# [0. 0. 0. 1. 0. 0. 0. 0.]
# state = np.arange(0,8, dtype=np.float)
GateSwap = np.array([[1., 0., 0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 1., 0., 0., 0.],
                     [0., 0., 1., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0., 1., 0.],
                     [0., 1., 0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 1., 0., 0.],
                     [0., 0., 0., 1., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0., 0., 1.]])

r = np.dot(GateSwap, state)
print (r)

assert np.allclose(r, np.array([0., 0., 0., 0., 1./np.sqrt(2.), 0., 1./np.sqrt(2), 0.,]))


##############################################
input0 = np.array([0.,1.])
input1 = np.array([1.,0.])
state = np.kron(input1, input0)

GateSwap4x4 = np.array([[1., 0., 0., 0., ],
                        [0., 0., 1., 0., ],  1 -> 2
                        [0., 1., 0., 0., ],
                        [0., 0., 0., 1., ]])
#OK

GateSwap8x8 = np.array([[1., 0., 0., 0., 0., 0., 0., 0.],
                        [0., 0., 0., 0., 1., 0., 0., 0.],  
                        [0., 0., 1., 0., 0., 0., 0., 0.],
                        [0., 0., 0., 0., 0., 0., 1., 0.], 
                        [0., 1., 0., 0., 0., 0., 0., 0.],
                        [0., 0., 0., 0., 0., 1., 0., 0.],
                        [0., 0., 0., 1., 0., 0., 0., 0.],
                        [0., 0., 0., 0., 0., 0., 0., 1.]])











input0 = np.array([0.,1.])
input1 = np.array([1./np.sqrt(2.),1./np.sqrt(2.)])
input2 = np.array([1.,0.])
input3 = np.array([1.,0.])
state = np.kron(np.kron(np.kron(input3, input2), input1), input0)
print (state)



GateSwap16x16 = np.array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
       [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]])

r = np.dot(GateSwap16x16, state)
print (r)

assert np.allclose(r, np.array([0.,0., 0., 0., 0.,0., 0., 0., 1./np.sqrt(2.),0., 1./np.sqrt(2.), 0., 0.,0., 0., 0.]))


https://quantumcomputing.stackexchange.com/questions/31942/how-to-represent-as-a-matrix-the-cswap-on-non-adjacent-qubits

# SWAP1,3=|0⟩⟨0|⊗I⊗|0⟩⟨0|+E01⊗I⊗E10+E10⊗I⊗E01+|1⟩⟨1|⊗I⊗|1⟩⟨1|

zero = np.array([1.,0.])
one = np.array([0.,1.])

ide2 = np.identity(2)
out0=np.outer (zero, np.conjugate(zero).T)
out1=np.outer (one, np.conjugate(one).T)

a = np.kron(np.kron(ide2, out0), out0)

b = np.kron(np.kron(ide2, out0), out1)

# c = np.kron(np.kron(out0, ide2), out1)
# 
# c = np.kron(np.kron(out1, ide2), out1)
gnot = np.array([[0., 1.], [1., 0.]]) # not
c = np.kron(np.kron(ide2, gnot), ide2)

a+b+c



E01 = np.outer (zero, np.conjugate(one).T)
E10 = np.outer (one, np.conjugate(zero).T)
b = np.kron(np.kron(E01, ide2), E10)
c = np.kron(np.kron(E10, ide2), E01)
out3=np.outer (one, np.conjugate(one).T)
d = np.kron(np.kron(out3, ide2), out3)
r = a + b + c + d
# works


zero = np.array([1.,0.])
one = np.array([0.,1.])

ide2 = np.identity(4) # needs correct number!
out0=np.outer (zero, np.conjugate(zero).T)
a = np.kron(np.kron(out0, ide2), out0)
E01 = np.outer (zero, np.conjugate(one).T)
E10 = np.outer (one, np.conjugate(zero).T)
b = np.kron(np.kron(E01, ide2), E10)
c = np.kron(np.kron(E10, ide2), E01)
out3=np.outer (one, np.conjugate(one).T)
d = np.kron(np.kron(out3, ide2), out3)
r = a + b + c + d
# works

