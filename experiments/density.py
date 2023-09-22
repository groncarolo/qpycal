import numpy as np
plus = np.matrix([1./np.sqrt(2.), 1./np.sqrt(2.)])
one = np.matrix([0.,1.])
kets = [plus, one]
probs = [1./2., 1./2. ]
matrix = np.zeros( (2,2))
for x,y in zip(kets, probs):
    matrix += y*np.outer(x, x)

print(matrix)
