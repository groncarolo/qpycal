import sys

import numpy as np

from qutils import complex_2_polar_coordinates, rad_2_deg


def display_circuit(states, gates):
    '''
    display a circuit in columns
    :param states: initial states
    :param gates: gates
    :return:
    '''
    max_len_label = max(len(ele.label) for ele in states)
    max_len_name = max(len(ele.name) for ele in states)
    for i in reversed(range(len(states))):
        print("{:>{width}}".format(states[i].name, width=max_len_name), end="")
        print(" ", end="")
        print("{:>{width}}".format(states[i].label, width=max_len_label), end="")
        print(" ", end="")
        for j in range(len(gates)):
            print(gates[j][i].label, end="")
            print(" ", end="")
        print("")
    print("{:>{width}}".format("", width=max_len_name + max_len_label + 2), end="")
    for i in range(len(gates)):
        if i == 0:
            print(str(i), end="")
        elif (i % 5) == 0:
            print("{:>{width}}".format(str(i), width=10), end="")
    print("")


def display_result(ret, prob, in_len):
    '''
    display results: values, magnitudes and phases
    :param ret: result
    :param in_len: len of result
    :return:
    '''
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

    mag, angles = complex_2_polar_coordinates(ret)
    print("mag^2:")
    print(np.square(mag).reshape(b, a))
    print("phase:")
    print(rad_2_deg(angles).reshape(b, a))

    display_probability(prob)


def display_probability(prob):
    print("Prob ON")
    print(prob)
