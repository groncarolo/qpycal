import logging
from functools import reduce

from qgates import CNOT10, SwapPlaceHolder, Gate, apply_gate, CNOT01, Ctrl, ACtrl, XGate
from qmath import tensor_prod
from qstates import State, is_state_normalized


def calculate_initial_state(states):
    if len(states) > 1:
        state = reduce(lambda x, y: State(tensor_prod(x.state, y.state)), states)
    else:
        state = states[0]

    if not is_state_normalized(state):
        raise "State is not normalized"
    return state.state


def solve_circuit(state, circuit):
    for col in circuit:
        logging.info("Multiplying:")
        logging.info(state)
        logging.info("*")

        for g in col:
            logging.info(g.gate)

        if len(col) > 1:
            # look for a control
            ctrls = [i for i, e in enumerate(col) if isinstance(e, Ctrl)]
            logging.info("ctrls")
            logging.info(ctrls)

            actrls = [i for i, e in enumerate(col) if isinstance(e, ACtrl)]
            logging.info("actrls")
            logging.info(actrls)

            nots = [i for i, e in enumerate(col) if isinstance(e, XGate)]
            logging.info("nots")
            logging.info(nots)

            swaps = [i for i, e in enumerate(col) if isinstance(e, SwapPlaceHolder)]
            logging.info("swaps")
            logging.info(swaps)

            if len(ctrls) > 0:
                # remove from list between indexes
                if ctrls[0] < nots[0]:
                    start_index = ctrls[0]
                    end_index = nots[0] + 1
                    cnot = CNOT10
                else:
                    start_index = nots[0]
                    end_index = ctrls[0] + 1
                    cnot = CNOT01
                del col[start_index:end_index]

                logging.info("now col is:")
                logging.info(col)
                # if there is nothing else in the column
                # this is the final gate
                g = cnot(2 ** (end_index - start_index))
                if len(col) == 0:
                    complete = g
                else:
                    # we need to insert the new gate in the correct position
                    col.insert(start_index, g)
                    complete = reduce(lambda x, y: Gate(tensor_prod(x.gate, y.gate)), col)
            else:
                complete = reduce(lambda x, y: Gate(tensor_prod(x.gate, y.gate)), col)
        else:
            # this is one bit case
            complete = col[0]
        logging.info(complete.gate)

        state = apply_gate(complete, state)
        logging.info("=")
        logging.info(state)
        logging.info("^^^^^^^^^^^")
    return state
