import sys
import numpy as np

from qutils import complex_2_spherical_coordinates, complex_2_cartesian_coordinates, print_spherical_coordinates, \
    print_cartesian_coordinates, complex_2_polar_coordinates


def display_circuit(states, gates):
    for i in reversed(range(len(states))):
        print(states[i].label, end="")
        print(" ", end="")
        for j in range(len(gates)):
            print(gates[j][i].label, end="")
            print(" ", end="")
        print("")


def display_result(ret, in_len):
    if len(ret) == 2:
        ret_r_ph_th = complex_2_spherical_coordinates(ret)
        ret_xyz = complex_2_cartesian_coordinates(ret)
        print_spherical_coordinates(ret_r_ph_th)
        print_cartesian_coordinates(ret_xyz)
    else:
        np.set_printoptions(linewidth=sys.maxsize)
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

        if (in_len % 2) == 0:
            a = int(np.sqrt(ret.shape[0]))
            b = int(np.sqrt(ret.shape[0]))
        else:
            b = int(np.sqrt(ret.shape[0] * 2))
            a = b // 2

        print(ret.reshape(b, a))
