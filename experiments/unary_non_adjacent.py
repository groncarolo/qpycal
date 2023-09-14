import numpy as np

input0 = np.array([1,0])
input1 = np.array([1,0])
input2 = np.array([0,1])


state = np.kron(np.kron(input2, input1), input0)

GateX = np.array([[0., 1.], [1., 0.]]) # not
g1 = np.array([[1., 0.], [0., 1.]]) # identity
g2 = np.array([[1., 0.], [0., 1.]]) # ctrl

g = np.kron(np.kron(g2, g1), g0)

np.dot( g, state)

#after manip

input0 = np.array([1,0])
input1 = np.array([1,0])
input2 = np.array([0,1])

state = np.kron(np.kron(input2, input1), input0)
g0 = np.array([[1., 0. ,0., 0.], [0., 1. ,0., 0.], [0., 0. ,0., 1.], [0., 0. ,1., 0.]]) # not
g2 = np.array([[1., 0.], [0., 1.]]) # identity



g = np.kron(g0, g2)

np.dot( g, state)



input0 = np.array([1,0])
input1 = np.array([1,0])
state = np.kron(input1, input0)
g = np.array([[1., 0. ,0., 0.], [0., 1. ,0., 0.], [0., 0. ,0., 1.], [0., 0. ,1., 0.]]) # cnot
np.dot(g, state)





input0 = np.array([1,0])
input1 = np.array([0,1])
input2 = np.array([1,0])
state = np.kron(np.kron(input2, input1), input0)

g0 = np.array([[1., 0. ,0., 0.], [0., 1. ,0., 0.], [0., 0. ,0., 1.], [0., 0. ,1., 0.]]) # cnot
g1 = np.array([[1., 0.], [0., 1.]]) # identity
g = np.kron(g1, g0)
np.dot(g, state)






input0 = np.array([1,0])
input1 = np.array([0,1])
state = np.kron(input1, input0)
g = np.array([[1., 0. ,0., 0.], [0., 1. ,0., 0.], [0., 0. ,0., 1.], [0., 0. ,1., 0.]]) # cnot
np.dot(g, state)





input0 = np.array([1,0])
input1 = np.array([1./np.sqrt(2.),1./np.sqrt(2.)])
input2 = np.array([1,0])
state = np.kron(np.kron(input2, input1), input0)

g0 = np.array([
[1,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0],
[0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1],
[0,0,0,0,1,0,0,0],
[0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0],
[0,0,0,1,0,0,0,0] ]) # cnot
np.dot(g0, state)






input0 = np.array([1.,0.])
input1 = np.array([1./np.sqrt(2.),1./np.sqrt(2.)])
input2 = np.array([1.,0.])
state = np.kron(np.kron(input2, input1), input0)

g0 = np.array([

[1,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0],
[0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1],
[0,0,0,0,1,0,0,0],
[0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0],
[0,0,0,1,0,0,0,0]]) # cnot
np.dot(g0, state)


# THIS WORKS!

zero = np.array([1.,0.])
one = np.array([0.,1.])
ide = np.identity(2)
out=np.outer (zero, np.conjugate(zero).T)
a = np.kron(np.kron(ide, ide), out)
gnot = np.array([[0., 1.], [1., 0.]]) # not
out2=np.outer (one, np.conjugate(one).T)
b = np.kron(np.kron(gnot, ide), out2)
c = a+b



# TRY MORE



input0 = np.array([1.,0.])
input1 = np.array([1./np.sqrt(2.),1./np.sqrt(2.)])
input2 = np.array([1./np.sqrt(2.),1./np.sqrt(2.)])
input3 = np.array([1.,0.])
input4 = np.array([1.,0.])
state = np.kron(np.kron(np.kron(np.kron(input4, input3), input2), input1), input0)

# cnot ij i control j target
# WORKS OK
def get_U_10(state_shape, gate):
    zero = np.array([1.,0.])
    one = np.array([0.,1.])
    ide2 = np.identity(2)
    idex = np.identity(state_shape//4)
    out=np.outer (zero, np.conjugate(zero).T)
    a = np.kron(np.kron(out, ide2), idex)
    print (a.shape)
    out2=np.outer (one, np.conjugate(one).T)
    b = np.kron(np.kron(out2, idex), gate)
    print (b.shape)
    g0 = a+b
    g0.shape
    return g0

g0 = get_U_10(state.shape[0], GateX)
np.dot(g0, state)

# {
#   "cols": [
#     [
#       "X",
#       1,
#       "•"
#     ]
#   ],
#   "init": [
#     0,
#     "+"
#   ]
# }

# left bottom
# right top
# |0> * |+> * |0> C * I * X


input0 = np.array([1.,0.])
input1 = np.array([1./np.sqrt(2.),1./np.sqrt(2.)])
input2 = np.array([1.,0.])
state = np.kron(np.kron(input2, input1), input0)

g0 = get_U_10(state.shape[0], GateX)
np.dot(g0, state)


# cnot ij i control j target
# WORKS OK TOO
# def get_U_01(state_shape):
#     zero = np.array([1.,0.])
#     one = np.array([0.,1.])
#     ide2 = np.identity(2)
#     idex = np.identity(state_shape//4)
# 
#     out=np.outer (zero, np.conjugate(one).T)
#     a = np.kron(np.kron(ide2, idex), out)
# 
#     gnot = np.array([[0., 1.], [1., 0.]]) # not
#     out2=np.outer (one, np.conjugate(zero).T)
#     b = np.kron(np.kron(out2, idex), gnot)
#     g0 = a+b
#     g0.shape
#     return g0
def get_U_01(state_shape, gate):
    zero = np.array([1.,0.])
    one = np.array([0.,1.])
    ide2 = np.identity(2)
    idex = np.identity(state_shape//4)
    out=np.outer (zero, np.conjugate(zero).T)
    a = np.kron(np.kron(ide2, idex), out)
    out2=np.outer (one, np.conjugate(one).T)
    b = np.kron(np.kron(gate, idex), out2)
    g0 = a+b
    g0.shape
    return g0


input0 = np.array([1.,0.])
input1 = np.array([1./np.sqrt(2.),1./np.sqrt(2.)])
input2 = np.array([1.,0.])
state = np.kron(np.kron(input2, input1), input0)

g0 = get_U_01(state.shape[0], GateX)
np.dot(g0, state)

# {
#   "cols": [
#     [
#       "•",
#       1,
#       1,
#       1,
#       "X"
#     ]
#   ],
#   "init": [
#     0,
#     0,
#     "+",
#     "+",
#     1
#   ]
# }

# top
input0 = np.array([1.,0.])
input1 = np.array([1.,0.])
input2 = np.array([1./np.sqrt(2.),1./np.sqrt(2.)])
input3 = np.array([1./np.sqrt(2.),1./np.sqrt(2.)])
input4 = np.array([0.,1.])
# bottom
state = np.kron(np.kron(np.kron(np.kron(input4, input3), input2), input1), input0)

g0 = get_U_10(state.shape[0], GateX)
np.dot(g0, state).reshape(8,4)


# {
#   "cols": [
#     [
#       "X",
#       1,
#       1,
#       1,
#       "•"
#     ]
#   ],
#   "init": [
#     0,
#     0,
#     "+",
#     "+",
#     1
#   ]
# }
input0 = np.array([1.,0.])
input1 = np.array([1.,0.])
input2 = np.array([1./np.sqrt(2.),1./np.sqrt(2.)])
input3 = np.array([1./np.sqrt(2.),1./np.sqrt(2.)])
input4 = np.array([0.,1.])
# bottom
state = np.kron(np.kron(np.kron(np.kron(input4, input3), input2), input1), input0)

g0 = get_U_01(state.shape[0], GateX)
np.dot(g0, state).reshape(8,4)
