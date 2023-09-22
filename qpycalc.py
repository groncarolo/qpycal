import logging

import numpy as np
from qconsole import Qconsole


def main():
    logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG, force=True)

    np.set_printoptions(precision=3)
    np.set_printoptions(suppress=True)
    try:
        Qconsole().cmdloop()
    except KeyboardInterrupt:
        print("")
    print("")


if __name__ == "__main__":
    main()
