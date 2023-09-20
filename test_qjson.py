import os

import numpy as np

from qjson import from_json_file
from qparser import parse_and_solve


def test_from_json():
    os.chdir("./test_data")
    for f in os.listdir():
        if os.path.isfile(f):
            circuit, result = from_json_file(f)
            print(circuit)
            print(result)

            my_result, prob, in_len = parse_and_solve(circuit)
            assert np.allclose(result, my_result)
