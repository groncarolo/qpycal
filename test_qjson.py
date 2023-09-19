import os

import numpy as np

from qjson import from_json
from qparser import parse_and_solve


def test_from_json():
    os.chdir("./test_data")
    for f in os.listdir():
        if os.path.isfile(f):
            with open(f, 'r') as file:
                data = file.read().replace('\n', '')
                print("")
                print(f)
                print(data)
                circuit, result = from_json(data)
                print(circuit)
                print(result)

                my_result, in_len = parse_and_solve(circuit)
                assert np.allclose(result, my_result)
