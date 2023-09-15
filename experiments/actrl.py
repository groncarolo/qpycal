import numpy as np

# input0 = np.array([1,0])
# input1 = np.array([1,0])
# state = np.kron(input1, input0)
# g = np.array([[1., 0. ,0., 0.],
#               [0., 1. ,0., 0.],
#               [0., 0. ,0., 1.],
#               [0., 0. ,1., 0.]]) # cnot
# r = np.dot(g, state)
# print (r)

# left -> bottom right -> top.
#A
#X

input0 = np.array([1,0])
input1 = np.array([1,0])
state = np.kron(input1, input0)
print (state)
g = np.array([[0., 0. ,1., 0.],
              [0., 1. ,0., 0.],
              [1., 0. ,0., 0.],
              [0., 0. ,0., 1.]])
r = np.dot(g, state)
print (r)

input0 = np.array([0,1])
input1 = np.array([1,0])
state = np.kron(input1, input0)
print (state)
r = np.dot(g, state)
print (r)

input0 = np.array([1,0])
input1 = np.array([0,1])
state = np.kron(input1, input0)
print (state)
r = np.dot(g, state)
print (r)

input0 = np.array([0,1])
input1 = np.array([0,1])
state = np.kron(input1, input0)
print (state)
r = np.dot(g, state)
print (r)


zero = np.array([1.,0.])
one = np.array([0.,1.])


E00 = np.outer (zero, np.conjugate(zero).T)
E01 = np.outer (zero, np.conjugate(one).T)
E10 = np.outer (one, np.conjugate(zero).T)
E11 = np.outer (one, np.conjugate(one).T)

state_shape = 8
ide2 = np.identity(2)
idex = np.identity(state_shape//4)




#A
#I
#X
g8x8 = np.array([[0., 0. ,0., 0., 1., 0. ,0., 0],
              [0., 1. ,0., 0., 0., 0. ,0., 0],
              [0., 0. ,0., 0., 0., 0. ,1., 0],
              [0., 0. ,0., 1., 0., 0. ,0., 0],
              [1., 0. ,0., 0., 0., 0. ,0., 0],
              [0., 0. ,0., 0., 0., 1. ,0., 0],
              [0., 0. ,1., 0., 0., 0. ,0., 0],
              [0., 0. ,0., 0., 0., 0. ,0., 1]
              ])





input0 = np.array([1.,0.])
input1 = np.array([1.,0.])
input2 = np.array([1.,0.])
state = np.kron(np.kron(input2, input1), input0)

state_shape=8
zero = np.array([1.,0.])
one = np.array([0.,1.])
ide2 = np.identity(state_shape//2)
idex = np.identity(state_shape//4)

E00=np.outer (zero, np.conjugate(zero).T)
E01=np.outer (zero, np.conjugate(one).T)
E10=np.outer (one, np.conjugate(zero).T)
E11=np.outer (one, np.conjugate(one).T)


a = np.kron(ide2, E11)
# array([[0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 1., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 1., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 1., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 1.]])


b = np.kron(np.kron(E10, idex), E00)
# array([[0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.],
#        [1., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 1., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.]])


c = np.kron(np.kron(E01, idex), E00)
# array([[0., 0., 0., 0., 1., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 1., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0.]])



g_c = a+b+c
np.allclose(g_c, g)






# A
# X
g4x4 = np.array([[0., 0. ,1., 0.],
                 [0., 1. ,0., 0.],
                 [1., 0. ,0., 0.],
                 [0., 0. ,0., 1.]])


#A
#I
#X
g8x8 = np.array([[0., 0. ,0., 0., 1., 0. ,0., 0],
              [0., 1. ,0., 0., 0., 0. ,0., 0],
              [0., 0. ,0., 0., 0., 0. ,1., 0],
              [0., 0. ,0., 1., 0., 0. ,0., 0],
              [1., 0. ,0., 0., 0., 0. ,0., 0],
              [0., 0. ,0., 0., 0., 1. ,0., 0],
              [0., 0. ,1., 0., 0., 0. ,0., 0],
              [0., 0. ,0., 0., 0., 0. ,0., 1]
              ])



# cnot ij i control j target
def get_cnot_actrl_01(state_shape):
    zero = np.array([1.,0.])
    one = np.array([0.,1.])
    ide2 = np.identity(state_shape//2)
    idex = np.identity(state_shape//4)
    
    E00=np.outer (zero, np.conjugate(zero).T)
    E01=np.outer (zero, np.conjugate(one).T)
    E10=np.outer (one, np.conjugate(zero).T)
    E11=np.outer (one, np.conjugate(one).T)
    
    a = np.kron(ide2, E11)
    b = np.kron(np.kron(E10, idex), E00)
    c = np.kron(np.kron(E01, idex), E00)
    return a+b+c

g_c = get_cnot_actrl_01(8)
np.allclose(g_c, g8x8)


g_c = get_cnot_actrl(4)
g_c
np.allclose(g_c, g4x4)



# ==============+++++++++++++++++++++++++++
# ==============+++++++++++++++++++++++++++

# X
# A
g4x4 = np.array([[0., 1. ,0., 0.],
                 [1., 0. ,0., 0.],
                 [0., 0. ,1., 0.],
                 [0., 0. ,0., 1.]])


# X
# I
# A
g8x8 = np.array([[0., 1. ,0., 0., 0., 0. ,0., 0],
                 [1., 0. ,0., 0., 0., 0. ,0., 0],
                 [0., 0. ,0., 1., 0., 0. ,0., 0],
                 [0., 0. ,1., 0., 0., 0. ,0., 0],
                 [0., 0. ,0., 0., 1., 0. ,0., 0],
                 [0., 0. ,0., 0., 0., 1. ,0., 0],
                 [0., 0. ,0., 0., 0., 0. ,1., 0],
                 [0., 0. ,0., 0., 0., 0. ,0., 1]
              ])



# cnot ij i control j target
def get_cnot_actrl_10(state_shape):
    zero = np.array([1.,0.])
    one = np.array([0.,1.])
    ide2 = np.identity(2)
    idex = np.identity(state_shape//4)
    
    E00=np.outer (zero, np.conjugate(zero).T)
    E01=np.outer (zero, np.conjugate(one).T)
    E10=np.outer (one, np.conjugate(zero).T)
    E11=np.outer (one, np.conjugate(one).T)
    
    gnot = np.array([[0., 1.], [1., 0.]]) # not
    
    a = np.kron(E00, np.kron(idex, gnot))
    b = np.kron(E11, np.kron(idex, ide2))
    
    return a+b

g_c = get_cnot_actrl_10(8)
np.allclose(g_c, g8x8)


g_c = get_cnot_actrl_10(4)
g_c
np.allclose(g_c, g4x4)

