import logging
import numpy as np


def tensor_prod(a, b):
    logging.info("tensor_prod")
    logging.info(a)
    logging.info(b)
    return np.kron(a, b)
