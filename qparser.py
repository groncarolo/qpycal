import logging

from ply import yacc
import numpy as np

from qgates import apply_gate, Gate, Ctrl, ACtrl, XGate
from qstates import is_normalized, State, get_U_10, get_U_01
from qutils import tensor_prod
from qlexer import tokens
from functools import reduce


def display_circuit(states, gates):
    for i in reversed(range(len(states))):
        print(states[i].label, end="")
        print(" ", end="")
        for j in reversed(range(len(gates))):
            print(gates[j][i].label, end="")
            print(" ", end="")
        print("")


def p_circuit(p):
    '''circuit : states gates'''
    logging.info("p_circuit")
    display_circuit(p[1], p[2])

    if len(p[1]) > 1:
        state = reduce(lambda x, y: State(tensor_prod(x.state, y.state)), p[1])
    else:
        state = p[1][0]

    if not is_normalized(state):
        raise
    ret = state.state
    for col in p[2]:
        logging.info("Multiplying:")
        logging.info(ret)
        logging.info("*")

        for g in col:
            logging.info(g.gate)

        if len(col) > 1:
            # look for a control
            ctrls = [i for i, e in enumerate(col) if type(e) == type(Ctrl())]
            logging.info("ctrls")
            logging.info(ctrls)
            actrls = [i for i, e in enumerate(col) if type(e) == type(ACtrl())]
            logging.info("actrls")
            logging.info(actrls)
            nots = [i for i, e in enumerate(col) if type(e) == type(XGate())]
            logging.info("nots")
            logging.info(nots)

            if len(ctrls) > 0:
                # remove from list between indexes
                if ctrls[0] < nots[0]:
                    start_index=ctrls[0]
                    end_index=nots[0]+1
                    op=get_U_10
                else:
                    start_index = nots[0]
                    end_index = ctrls[0]+1
                    op = get_U_01
                del col[start_index:end_index]

                logging.info("now col is:")
                logging.info(col)
                # if there is nothing else in the column
                # this is the final gate
                g = Gate(op(2**(end_index-start_index), XGate.gate))
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

        ret = apply_gate(complete, ret)
        logging.info("=")
        logging.info(ret)
        logging.info("^^^^^^^^^^^")

    p[0] = ret,len(p[1])


def p_factor(p):
    '''factor : NUMBER
              | SQRT LPAREN NUMBER RPAREN
              | NUMBER TIMES SQRT LPAREN NUMBER RPAREN'''
    logging.info("p_factor")
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 5:
        p[0] = p[1](p[3])
    elif len(p) == 7:
        p[0] = p[1] * p[3](p[5])


def p_opearand(p):
    '''operand : MINUS
               | PLUS'''
    logging.info("p_operand")
    p[0] = 1.0 * p[1]


def p_factors(p):
    '''factors : factor
               | factor DIVIDE factor
               | LPAREN factor operand i TIMES factor RPAREN DIVIDE factor'''

    logging.info("p_factors")
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] / p[3]
    elif len(p) == 10:
        p[0] = (p[2] + 1j * p[3] * p[6]) / p[9]


def p_states(p):
    '''states : states TIMES comp_state
    | comp_state'''
    logging.info("p_states")
    if len(p) == 2:
        logging.info(">>len 2")
        p[0] = [p[1]]
    elif len(p) == 4:
        logging.info(">>len 4")
        p[1].append(p[3])
        p[0] = p[1]


def p_comp_states(p):
    '''comp_state : state
                  | factors state
                  | LBRACKET factors state operand factors state RBRACKET'''
    logging.info("p_comp_states")
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        s = p[2]
        s.state = s.state * p[1]
        p[0] = s
    elif len(p) == 8:
        s1 = p[3]
        s1.state = s1.state * p[2]
        s2 = p[6]
        s2.state = s2.state * p[4] * p[5]
        s1.state = s1.state + s2.state
        p[0] = s1


def p_state(p):
    '''state : state_0
    | state_1
    | state_plus
    | state_minus
    | state_i
    | state_minus_i'''
    # logging.info("p_state")
    p[0] = p[1]
    # logging.info("state " + str(p[0].state))


def p_gates(p):
    r'''gates : gates gate
              | gates TIMES gate
              | gate'''
    logging.info("p_gates")

    if len(p) == 2:
        logging.info("p_gates: first gate")
        # create a list
        p[0] = [[p[1]]]
    elif len(p) == 4:
        logging.info("p_gates: len4")
        last = p[1][len(p[1]) - 1]
        last.append(p[3])
        p[0] = p[1]
    else:
        logging.info("p_gates: append")
        last = p[1]
        last.append([p[2]])
        p[0] = p[1]


def p_gate(p):
    '''gate : X
           | Y
           | Z
           | S
           | T
           | H
           | I
           | C
           | A
    '''
    p[0] = p[1]
    logging.info("p_gate")
    logging.info(p[0].gate)


# Error rule for syntax errors
def p_error(p):
    logging.error("Syntax error in input! %s", str(p))
    raise RuntimeError


# Build the parser
log = logging.getLogger()
parser = yacc.yacc(debug=True, debuglog=log)


def parse_and_calculate(data):
    return parser.parse(data, debug=log)
