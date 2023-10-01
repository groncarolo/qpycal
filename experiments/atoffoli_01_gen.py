import numpy as np

np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)


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

def bit_mov(how_many_bits, g=np.identity(1), s="", a=E10, b=E11, sa="E10", sb="E11"):
    for i in range(2**how_many_bits):
        binary = "{0:>0{1}b}".format(i, how_many_bits)
        pr = g # np.kron(np.identity(2), E11) # np.identity(1)
        pr_str = s # "np.kron(np.identity(2), E11)"
        f=1
        for c in reversed(binary):
            pr = np.kron(a if c == '0' else b, pr)
            if f == 1:
                m = ""
            else:
                m = "np.kron("
            if c == '0':
                m = m + sa
            else:
                m = m + sb
            if f == 1:
                f = 0
            else:
                m = m + ","+ pr_str+")"
            pr_str = m
        print (str(i))
        print (binary)
        print (pr)
        print (pr_str)

def get_unitary_agate_01(how_many_bits, ctrls):
    print("get_unitary_gate_01 ")
    state_shape = 2 ** how_many_bits
    ret = np.zeros((state_shape, state_shape), dtype=complex)
    print ("how_many_bits: " + str(how_many_bits))
    print ("ctrls: ")
    print(ctrls)
    if ctrls[0] - ctrls[1] == 1:
        print ("AAAA")
        x=2**ctrls[1]
        r = np.kron(np.identity(x), np.kron(E11, np.identity(2)))
        r = r + np.kron(np.identity(x), np.kron(E00, E11))
        r = r + np.kron(np.kron(np.kron(E01, np.identity(x//2)), E00), E00)
        r = r + np.kron(np.kron(np.kron(E10, np.identity(x//2)), E00), E00)
    elif ctrls[1] == 1:
        print ("BBBB")
        x= state_shape // 8
        print (x)
        r = np.kron(np.kron(np.kron(E01, E00), np.identity(x)), E00) #OK
        r = r + np.kron(np.kron(np.kron(E10, E00), np.identity(x)), E00) #OK
        r = r + np.kron(E11,np.kron(E11, np.kron(ide2, np.identity(x))))
        r = r + np.kron(E00,np.kron(E11, np.kron(ide2, np.identity(x))))
        r = r + np.kron(E11,np.kron(E00, np.kron(np.identity(x), E11)))
        r = r + np.kron(E00,np.kron(E00, np.kron(np.identity(x), E11))) # WORKS!
    else:
        print ("CCCC")
        b = 2**(ctrls[0] - ctrls[1])//2
        a = (2**ctrls[1])//2
        print (a)
        print (b)

        r = np.kron(E01, np.kron(np.identity(a), np.kron(np.kron(E00, np.identity(b)), E00)))
        r = r + np.kron(E10, np.kron(np.identity(a), np.kron(np.kron(E00, np.identity(b)), E00)))
        for i in np.where(r.any(axis=1) == 0.)[0]:
            r[i,i] = 1
    print(r)
    return r


# #############################################################################
# A  2
# A  1
# X  0
# #############################################################################
g = np.array([ #        3            7
              [0.,0.,0.,0., 1.,0.,0.,0.],
              [0.,1.,0.,0., 0.,0.,0.,0.],
              [0.,0.,1.,0., 0.,0.,0.,0.],
              [0.,0.,0.,1., 0.,0.,0.,0.],  #3

              [1.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,1.,0.,0.],
              [0.,0.,0.,0., 0.,0.,1.,0.],
              [0.,0.,0.,0., 0.,0.,0.,1.],  #7
])
x=2
a = np.kron(np.identity(x), np.kron(E00, np.identity(2)))
b = np.kron(np.identity(x), np.kron(E11, E00))

c = np.kron(np.kron(np.kron(E01, np.identity(x//2)), E11), E11)
d = np.kron(np.kron(np.kron(E10, np.identity(x//2)), E11), E11)

r=a+b+c+d
print ("A")
print ("A")
print ("X")
#assert np.allclose(g, r)
print ("OK")
r = get_unitary_agate_01(3, [2,1])
assert np.allclose(g, r)
# #############################################################################


#############################################################################
# A  3
# A  2
# I  1
# X  0
#############################################################################
g = np.array([ #        3*            7*          11*          15*
              [0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0.],
              [0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #3*

              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0.],
              [0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0.], #7*

              [1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0.], #11*

              [0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1.], #15*
])

x=4
a = np.kron(np.identity(x), np.kron(E00, np.identity(2)))
b = np.kron(np.identity(x), np.kron(E11, E00))

c = np.kron(np.kron(np.kron(E01, np.identity(x//2)), E11), E11)
d = np.kron(np.kron(np.kron(E10, np.identity(x//2)), E11), E11)

r=a+b+c+d
print ("A")
print ("A")
print ("I")
print ("X")
#assert np.allclose(g, r)
print ("OK")
r = get_unitary_agate_01(4, [3,2])
assert np.allclose(g, r)
#############################################################################



#############################################################################
# A 3
# I 2
# A 1
# X 0
#############################################################################
g = np.array([
#                       3     5*     7*          11     13*   15*
              [0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0.],
              [0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0.],
              [0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #3

              [0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #5*
              [0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0.], #7*

              [1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0.],
              [0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0.], #11

              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0.], #13*
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1.], #15*
]) # toffoli


x = 2
r = np.kron(np.kron(np.kron(E01, E11), np.identity(x)), E11) #OK
r = r + np.kron(np.kron(np.kron(E10, E11), np.identity(x)), E11) #OK

r = r + np.kron(E00,np.kron(E00, np.kron(ide2, np.identity(x))))
r = r + np.kron(E11,np.kron(E00, np.kron(ide2, np.identity(x))))

r = r + np.kron(E00,np.kron(E11, np.kron(np.identity(x), E00)))
r = r + np.kron(E11,np.kron(E11, np.kron(np.identity(x), E00))) # WORKS!

print ("A")
print ("I")
print ("A")
print ("X")
#assert np.allclose(g, r) # OK
print ("OK")
r = get_unitary_agate_01(4, [3,1])
assert np.allclose(g, r)
#############################################################################
#
#
#
# #############################################################################
# # C  4
# # C  3
# # I  2
# # I  1
# # X  0
# ############################################################################
# g = np.array( [#        3*           7*          11*          15*           19*          23*          27*          31*
#               [1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #3*
# 
#               [0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0.], #7*
# 
#               [0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0 , 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0.], #11*
# 
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1.], #15*
# 
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #19*
# 
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #23*
# 
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #27*
# 
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #31*
# ])
# 
# print("C")
# print("C")
# print("I")
# print("I")
# print("X")
# 
# x=8
# a = np.kron(np.identity(x), np.kron(E00, np.identity(2)))
# b = np.kron(np.identity(x), np.kron(E11, E00))
# 
# c = np.kron(np.kron(np.kron(E01, np.identity(x//2)), E11), E11)
# d = np.kron(np.kron(np.kron(E10, np.identity(x//2)), E11), E11)
# 
# r=a+b+c+d
# assert np.allclose(g, r) #OK!!
# print ("OK")
# r = get_unitary_gate_01(5, [4,3])
# assert np.allclose(g, r)
# ############################################################################
# 


# ############################################################################4
# A 4
# I 3
# A 2
# I 1
# X 0
g = np.array([
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #3

              [0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #7*

              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #11

              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #15*

              [1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.], #19

              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0.], #23

              [0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0.], #27*

              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0.],
              [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1.], #31*
]) # toffoli

x = 4
r = np.kron(E01, np.kron(np.identity(x//2), np.kron(np.kron(E11, np.identity(x//2)), E11)))
r = r + np.kron(E10, np.kron(np.identity(x//2), np.kron(np.kron(E11, np.identity(x//2)), E11)))

for i in np.where(r.any(axis=1) == 0.)[0]:
    r[i,i] = 1


print("A")
print("I")
print("A")
print("I")
print("X")

#assert np.allclose(g, r) #OK
print ("OK")
r = get_unitary_agate_01(5, [4,2])
assert np.allclose(g, r)
############################################################################
# 
# 
# 
# ############################################################################
#  # C 4
#  # I 3
#  # I 2
#  # C 1
#  # X 0
# ############################################################################
# g = np.array([
#               [1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
# 
#               [0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
# 
#               [0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0 , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0.],
# 
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1.],
# 
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
# 
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0., 0.,0.,0.,0.],
# 
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
# 
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 1.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,1.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,1.,0.],
#               [0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,1. , 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0., 0.,0.,0.,0.],
# ])
# 
# x = 4
# r = np.kron(np.kron(np.kron(E01, E11), np.identity(x)), E11) #OK
# r = r + np.kron(np.kron(np.kron(E10, E11), np.identity(x)), E11) #OK
# 
# r = r + np.kron(E00,np.kron(E00, np.kron(ide2, np.identity(x))))
# r = r + np.kron(E11,np.kron(E00, np.kron(ide2, np.identity(x))))
# 
# r = r + np.kron(E00,np.kron(E11, np.kron(np.identity(x), E00)))
# r = r + np.kron(E11,np.kron(E11, np.kron(np.identity(x), E00))) # WORKS!
# 
# print("C")
# print("I")
# print("C")
# print("I")
# print("X")
# assert np.allclose(g, r) #OK
# print ("OK")
# r = get_unitary_gate_01(5, [4,1])
# assert np.allclose(g, r)
# ############################################################################
# 
# r = get_unitary_gate_01(6, [5,4])
# print (r)
# r = get_unitary_gate_01(6, [5,3])
# print (r)
# r = get_unitary_gate_01(6, [5,2])
# print (r)
# r = get_unitary_gate_01(6, [5,1])
# print (r)
