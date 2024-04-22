import logging
from typing import Any

import numpy as np
from functools import reduce

from qgates import cnot01_gate, cnot10_gate, QGate, acnot10_gate, acnot01_gate, swap_gate, identity_gate, \
    toffoli01_gate, toffoli10_gate, atoffoli01_gate, atoffoli10_gate
from qstates import QState
from qutils import get_probability
from qvisualization import display_circuit


def calculate_initial_state(states) -> QState:
    if len(states) > 1:
        state = reduce(lambda x, y: QState(np.kron(x.state, y.state)), states)
    else:
        state = states[0]

    if not state.is_normalized():
        raise RuntimeError("State is not normalized")
    return state


def substitute_cnot(col, ctrls, actrls, nots):
    '''
    we accept ONE CNOT per colum so we expect
    one ctrl and one NOT
    :param ctrls:
    :param actrls:
    :param nots:
    :return:
    '''
    if len(ctrls) == 1 and len(nots) == 1:
        # get the order of the gate
        if ctrls[0] < nots[0]:
            start_index = ctrls[0]
            end_index = nots[0] + 1
            cnot_fx = cnot01_gate
            rctrls = [end_index - x - 2 for x in ctrls]
        else:
            start_index = nots[0]
            end_index = ctrls[0] + 1
            cnot_fx = cnot10_gate
            rctrls = ctrls
        # clean all the gates that are in between
        del col[start_index:end_index]

        g = cnot_fx(end_index - start_index, rctrls)
        col.insert(start_index, g)
    if len(actrls) == 1 and len(nots) == 1:
        # get the order of the gate
        if actrls[0] < nots[0]:
            start_index = actrls[0]
            end_index = nots[0] + 1
            acnot_fx = acnot01_gate
        else:
            start_index = nots[0]
            end_index = actrls[0] + 1
            acnot_fx = acnot10_gate
        # clean all the gates that are in between
        del col[start_index:end_index]
        g = acnot_fx(2 ** (end_index - start_index))
        col.insert(start_index, g)


def substitute_toffoli(col, ctrls, actrls, nots):
    '''
    we accept ONE TOFFOLI per colum
    :param ctrls:
    :param actrls:
    :param nots:
    :return:
    '''
    # get the order of the gate
    if len(ctrls) == 2 and len(nots) == 1:
        if ctrls[0] < nots[0]:
            start_index = ctrls[0]
            end_index = nots[0] + 1
            toffoli_fx = toffoli01_gate
            rctrls = [nots[0] - x for x in ctrls]
        else:
            start_index = nots[0]
            end_index = ctrls[len(ctrls) - 1] + 1
            toffoli_fx = toffoli10_gate
            rctrls = [x - start_index for x in ctrls]
            rctrls.reverse()

        # clean all the gates that are in between
        del col[start_index:end_index]
        g = toffoli_fx(end_index - start_index, rctrls)
        col.insert(start_index, g)

    if len(actrls) == 2 and len(nots) == 1:
        if actrls[0] < nots[0]:
            start_index = actrls[0]
            end_index = nots[0] + 1
            atoffoli_fx = atoffoli01_gate
            ractrls = [abs(nots[0] - x) for x in actrls]
        else:
            start_index = nots[0]
            end_index = actrls[len(actrls) - 1] + 1
            atoffoli_fx = atoffoli10_gate
            ractrls = [abs(x - start_index) for x in actrls]
            ractrls.reverse()
        # clean all the gates that are in between
        del col[start_index:end_index]
        g = atoffoli_fx(end_index - start_index, ractrls)
        col.insert(start_index, g)


def substitute_swap(col, swaps):
    '''
    we need two swaps
    :param col:
    :param swaps:
    :return:
    '''
    if len(swaps) == 2:
        start_index = swaps[0]
        end_index = swaps[1] + 1
        del col[start_index:end_index]
        g = swap_gate(2 ** (end_index - start_index))
        col.insert(start_index, g)


def substitute_custom_gates(state_shape, circuit):
    logging.info(str(state_shape))
    logging.info(circuit)

    for idx_col, col in enumerate(circuit):
        for idx_gate, gate in enumerate(col):
            logging.info(gate.is_custom)
            if gate.is_custom:
                logging.info(gate.get_len())
                logging.info(gate.get_height())
                # if it is custom
                assert state_shape >= gate.get_height()
                del circuit[idx_col]
                logging.info("del " + str(idx_col))
                for i, new_col in enumerate(gate.gates):
                    logging.info("insert @ " + str(idx_col + i))
                    circuit.insert(idx_col + i, [])
                    for j, new_gate in enumerate(new_col):
                        logging.info("inserting @ " + str(idx_col + i) + " j " + str(j))
                        circuit[idx_col + i].insert(idx_gate + j, new_gate)
                    # if the new column is shorter than the state
                    for a in range(state_shape - len(new_col)):
                        circuit[idx_col + i].insert(idx_gate + len(new_col), identity_gate())
    logging.info(circuit)


def calculate_probability(how_many_bits, state):
    prob = np.zeros(how_many_bits, dtype=complex)
    for i in range(how_many_bits):
        for idx, s in enumerate(state):
            a = idx & (2 ** i)
            if a == 2 ** i:
                prob[i] += get_probability(s)

    return prob


def solve_circuit(states, circuit) -> [QState, np.ndarray[Any, np.dtype], list[str]]:
    state = calculate_initial_state(states)

    # substitute custom gates with their
    # representation
    substitute_custom_gates(len(states), circuit)

    display_circuit(states, circuit)

    for idx_col, col in enumerate(circuit):
        logging.warning("Column {0}".format(idx_col))
        logging.warning(state)
        logging.warning("*")

        # look for controls
        ctrls = [i for i, e in enumerate(col) if e.label == 'C']
        logging.info("ctrls")
        logging.info(ctrls)

        # look for anti controls
        actrls = [i for i, e in enumerate(col) if e.label == 'A']
        logging.info("actrls")
        logging.info(actrls)

        # look for nots
        nots = [i for i, e in enumerate(col) if e.label == 'X']
        logging.info("nots")
        logging.info(nots)

        # look for swaps
        swaps = [i for i, e in enumerate(col) if e.label == 'W']
        logging.info("swaps")
        logging.info(swaps)

        substitute_cnot(col, ctrls, actrls, nots)
        substitute_toffoli(col, ctrls, actrls, nots)
        substitute_swap(col, swaps)

        complete = reduce(lambda x, y: QGate(np.kron(x.gate, y.gate)), col)

        logging.warning(complete.gate)

        state = complete.apply(state)
        logging.warning("=")
        logging.warning(state)

    prob = calculate_probability(len(states), state.state)
    labels = [x.name for x in states]
    return state, prob, labels
