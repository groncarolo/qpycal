import argparse
import logging

from qjson import from_json
from qparser import parse_and_calculate
from qutils import print_cartesian_coordinates, complex_2_cartesian_coordinates
from qutils import complex_2_spherical_coordinates, print_spherical_coordinates



def main():
    logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG, force=True)

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-j", action='store_true')
    args, leftovers = arg_parser.parse_known_args()

    while True:
        try:
            if args.j is True:
                j_str = input('qpycal > ')
                circuit, result = from_json(j_str)
            else:
                circuit = input('qpycal > ')
        except EOFError:
            print("")
            break

        if not circuit:
            continue
        ret = parse_and_calculate(circuit)

        if len(ret) == 2:
            ret_r_ph_th = complex_2_spherical_coordinates(ret)
            ret_xyz = complex_2_cartesian_coordinates(ret)
            print_spherical_coordinates(ret_r_ph_th)
            print_cartesian_coordinates(ret_xyz)
        else:
            print(ret)
            #print(ret.reshape((4, 2)))


if __name__ == "__main__":
    main()
