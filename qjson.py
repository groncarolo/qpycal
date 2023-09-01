import json
import logging

import numpy as np


def from_json_gate(json_str):
    from_json_gate_dic = {"1": "I", "Z^¼": "T"}
    return from_json_gate_dic.get(str(json_str), str(json_str))


def from_json(jstr):
    j = json.loads(jstr)

    how_many_states = len(j["circuit"]["init"])

    circuit = ""
    for s in reversed(j["circuit"]["init"]):
        circuit = circuit + "|" + str(s) + ">*"
    circuit = circuit[:-1]
    logging.info("state: " + circuit)

    for c in j["circuit"]["cols"]:
        circuit += " "
        for i in range(how_many_states - len(c)):
            circuit = circuit + "I*"
        for g in reversed(c):
            circuit = circuit + from_json_gate(g) + "*"
        circuit = circuit[:-1]

    logging.info(circuit)

    result = np.zeros(2**how_many_states, dtype=complex)
    i=0
    for o in j["output_amplitudes"]:
        real = o["r"]
        imag = o["i"]
        result[i] = float(real) + 1j*float(imag)
        i=i+1

    return circuit, result
