import logging
import numpy as np
from functools import reduce

from qgates import CNOT10, Gate, apply_gate, CNOT01, Ctrl, ACtrl, XGate, Swap, Identity, ACNOT10, \
    ACNOT01, Toffoli10, Toffoli01, AToffoli10, AToffoli01
from qstates import State, is_state_normalized
from qutils import get_probability
from qvisualization import display_circuit


def calculate_initial_state(states):
    if len(states) > 1:
        state = reduce(lambda x, y: State(np.kron(x.state, y.state)), states)
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
        print("substitute_cnot")
        if ctrls[0] < nots[0]:
            start_index = ctrls[0]
            end_index = nots[0] + 1
            cnot = CNOT10
            print("CONTROLS")
            print(ctrls)
            print("idx: " + str(end_index - start_index))

            rctrls = [end_index - x - 2 for x in ctrls]
            print("rctrls")
            print(rctrls)

        else:
            start_index = nots[0]
            end_index = ctrls[0] + 1
            cnot = CNOT01
            rctrls = ctrls
        # clean all the gates that are in between
        del col[start_index:end_index]

        g = cnot(end_index - start_index, rctrls)
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
    '''
    we accept ONE TOFFOLI per colum
    :param ctrls:
    :param actrls:
    :param nots:
    :return:
    '''
    # get the order of the gate
    if len(ctrls) == 2 and len(nots) == 1:
        print("substitute_toffoli")
        if ctrls[0] < nots[0]:
            start_index = ctrls[0]
            end_index = nots[0] + 1
            toffoli = Toffoli10
            print("CONTROLS")
            print("end_index")
            print(str(end_index))
            print("start_index")
            print(str(start_index))
            print(ctrls)
            rctrls = [nots[0] - x for x in ctrls]
            print("rctrls")
            print(rctrls)
        else:
            print("nots")
            print(nots)
            start_index = nots[0]
            end_index = ctrls[len(ctrls) - 1] + 1
            toffoli = Toffoli01

            print("CONTROLS DDDDD")
            print("end_index")
            print(str(end_index))
            print("start_index")
            print(str(start_index))
            print(ctrls)

            rctrls = ctrls.reverse()

            rctrls = ctrls
            print("rctrls")
            print(rctrls)
        # clean all the gates that are in between
        del col[start_index:end_index]
        g = toffoli(end_index - start_index, rctrls)
        col.insert(start_index, g)

    if len(actrls) == 2 and len(nots) == 1:
        print("substitute_atoffoli")
        if actrls[0] < nots[0]:
            start_index = actrls[0]
            end_index = nots[0] + 1
            toffoli = AToffoli10
            print("ACONTROLS")
            print("end_index")
            print(str(end_index))
            print("start_index")
            print(str(start_index))
            print(actrls)
            ractrls = [nots[0] - x for x in actrls]
            print("ractrls")
            print(ractrls)
        else:
            print("nots")
            print(nots)
            start_index = nots[0]
            end_index = actrls[len(actrls) - 1] + 1
            toffoli = AToffoli01

            print("CONTROLS DDDDD")
            print("end_index")
            print(str(end_index))
            print("start_index")
            print(str(start_index))
            print(actrls)

            ractrls = actrls.reverse()

            ractrls = actrls
            print("ractrls")
            print(ractrls)
        # clean all the gates that are in between
        del col[start_index:end_index]
        g = toffoli(end_index - start_index, ractrls)
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


def calculate_probability(how_many_bits, state):
    # print("bit zero prob: ")
    # print(state.shape)

    prob = np.zeros(how_many_bits, dtype=complex)

    for i in range(how_many_bits):
        for idx, s in enumerate(state):
            # print (int(2**i))
            # print (bin(2**i))
            # print (bin(idx))
            a = idx & (2 ** i)
            if a == 2 ** i:
                # print("in")
                prob[i] += get_probability(s)

    return prob


def solve_circuit(states, circuit):
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
        swaps = [i for i, e in enumerate(col) if isinstance(e, Swap)]
        logging.info("swaps")
        logging.info(swaps)

        substitute_cnot(col, ctrls, actrls, nots)
        substitute_toffoli(col, ctrls, actrls, nots)
        substitute_swap(col, swaps)

        complete = reduce(lambda x, y: Gate(np.kron(x.gate, y.gate)), col)

        logging.warning(complete.gate)

        state = apply_gate(complete, state)
        logging.warning("=")
        logging.warning(state)

    prob = calculate_probability(len(states), state)

    return state, prob
