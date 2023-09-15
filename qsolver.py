import logging
from functools import reduce

from qgates import CNOT10, SwapPlaceHolder, Gate, apply_gate, CNOT01, Ctrl, ACtrl, XGate, Swap, Identity, ACNOT10, \
    ACNOT01
from qmath import tensor_prod
from qstates import State, is_state_normalized
from qvisualization import display_circuit


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
    if len(actrls) == 1 and len(nots) == 1:
        # get the order of the gate
        if actrls[0] < nots[0]:
            start_index = actrls[0]
            end_index = nots[0] + 1
            acnot = ACNOT10
        else:
            start_index = nots[0]
            end_index = actrls[0] + 1
            acnot = ACNOT01
        # clean all the gates that are in between
        del col[start_index:end_index]
        g = acnot(2 ** (end_index - start_index))
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
                        circuit[idx_col + i].insert(idx_gate + len(new_col), Identity())
    logging.info(circuit)


def solve_circuit(states, circuit):
    state = calculate_initial_state(states)

    # substitute custom gates with their
    # representation
    substitute_custom_gates(len(states), circuit)

    display_circuit(states, circuit)

    logging.info(circuit)
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

        logging.info(complete.gate.shape)
        logging.info(complete.gate)

        state = apply_gate(complete, state)
        logging.info("=")
        logging.info(state)
        logging.info("^^^^^^^^^^^")
    return state
