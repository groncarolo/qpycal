import sys

import numpy as np

from qutils import complex_2_polar_coordinates, rad_2_deg


def display_circuit(states, gates):
    max_len = max(len(ele.label) for ele in states)
    for i in reversed(range(len(states))):
        print("{:>{width}}".format(states[i].label, width=max_len), end="")
        print(" ", end="")
        for j in range(len(gates)):
            print(gates[j][i].label, end="")
            print(" ", end="")
        print("")
    print("{:>{width}}".format("", width=max_len + 1), end="")
    for i in range(len(gates)):
        if i == 0:
            print(str(i), end="")
        elif (i % 5) == 0:
            print("{:>{width}}".format(str(i), width=10), end="")
    print("")


def display_result(ret, in_len):
    np.set_printoptions(linewidth=sys.maxsize)
    np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

    if (in_len % 2) == 0:
        a = int(np.sqrt(ret.shape[0]))
        b = int(np.sqrt(ret.shape[0]))
    else:
        b = int(np.sqrt(ret.shape[0] * 2))
        a = b // 2

    print("values:")
    print(ret.reshape(b, a))

    abs, angles = complex_2_polar_coordinates(ret)
    print("mag^2:")
    print(np.square(abs).reshape(b, a))
    print("phase:")
    print(rad_2_deg(angles).reshape(b, a))
