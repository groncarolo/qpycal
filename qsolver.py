import logging
from functools import reduce

from qgates import CNOT10, SwapPlaceHolder, Gate, apply_gate, CNOT01, Ctrl, ACtrl, XGate, Swap
from qmath import tensor_prod
from qstates import State, is_state_normalized


def calculate_initial_state(states):
    if len(states) > 1:
        state = reduce(lambda x, y: State(tensor_prod(x.state, y.state)), states)
    else:
        state = states[0]

    if not is_state_normalized(state):
        raise RuntimeError("State is not normalized")
    return state.state


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
            cnot = CNOT10
        else:
            start_index = nots[0]
            end_index = ctrls[0] + 1
            cnot = CNOT01
        # clean all the gates that are in between
        del col[start_index:end_index]
        g = cnot(2 ** (end_index - start_index))
        col.insert(start_index, g)


def substitute_toffoli(col, ctrls, actrls, nots):
    pass


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
        g = Swap(2 ** (end_index - start_index))
        col.insert(start_index, g)


def solve_circuit(state, circuit):
    # substitute custom gates with their
    # representation

    for col in circuit:
        logging.info("Multiplying:")
        logging.info(state)
        logging.info("*")

        for g in col:
            logging.info(g.gate)

        # look for controls
        ctrls = [i for i, e in enumerate(col) if isinstance(e, Ctrl)]
        logging.info("ctrls")
        logging.info(ctrls)

        # look for anti controls
        actrls = [i for i, e in enumerate(col) if isinstance(e, ACtrl)]
        logging.info("actrls")
        logging.info(actrls)

        # look for nots
        nots = [i for i, e in enumerate(col) if isinstance(e, XGate)]
        logging.info("nots")
        logging.info(nots)

        # look for swaps
        swaps = [i for i, e in enumerate(col) if isinstance(e, SwapPlaceHolder)]
        logging.info("swaps")
        logging.info(swaps)

        substitute_cnot(col, ctrls, actrls, nots)
        substitute_toffoli(col, ctrls, actrls, nots)
        substitute_swap(col, swaps)

        complete = reduce(lambda x, y: Gate(tensor_prod(x.gate, y.gate)), col)

        logging.info(complete.gate)

        state = apply_gate(complete, state)
        logging.info("=")
        logging.info(state)
        logging.info("^^^^^^^^^^^")
    return state
