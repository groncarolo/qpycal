import argparse
import logging
import sys

import numpy as np

from qjson import from_json
from qparser import parse_and_calculate
from qutils import print_cartesian_coordinates, complex_2_cartesian_coordinates
from qutils import complex_2_spherical_coordinates, print_spherical_coordinates


def main():
    logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG, force=True)

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-j", action='store_true')
    args, leftovers = arg_parser.parse_known_args()

    print("left -> bottom right -> top")
    while True:
        try:
            if args.j is True:
                j_str = input('qpycal > ')
                circuit, result = from_json(j_str)
            else:
                # left bottom
                # right top
                circuit = input('qpycal > ')
        except EOFError:
            print("")
            break

        if not circuit:
            continue
        ret, in_len = parse_and_calculate(circuit)

        if len(ret) == 2:
            ret_r_ph_th = complex_2_spherical_coordinates(ret)
            ret_xyz = complex_2_cartesian_coordinates(ret)
            print_spherical_coordinates(ret_r_ph_th)
            print_cartesian_coordinates(ret_xyz)
        else:
            np.set_printoptions(linewidth=sys.maxsize)
            np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

            print(ret.shape[0])
            if (in_len % 2) == 0:
                a = int(np.sqrt(ret.shape[0]))
                b = int(np.sqrt(ret.shape[0]))
            else:
                b = int(np.sqrt(ret.shape[0]*2))
                a = b //2

            print(ret.reshape(b, a))


if __name__ == "__main__":
    main()
