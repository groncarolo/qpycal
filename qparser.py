import logging

from ply import yacc

from qsolver import calculate_initial_state, solve_circuit
from qlexer import tokens

from qvisualization import display_circuit


def p_circuit(p):
    '''circuit : states gates'''
    logging.info("p_circuit")
    display_circuit(p[1], p[2])

    initial_state = calculate_initial_state(p[1])

    ret = solve_circuit(initial_state, p[2])
    p[0] = ret, len(p[1])


def p_factor(p):
    '''factor : number
              | sqrt lparen number rparen
              | number times sqrt lparen number rparen'''
    logging.info("p_factor")
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 5:
        p[0] = p[1](p[3])
    elif len(p) == 7:
        p[0] = p[1] * p[3](p[5])


def p_opearand(p):
    '''operand : minus
               | plus'''
    logging.info("p_operand")
    p[0] = 1.0 * p[1]


def p_factors(p):
    '''factors : factor
               | factor divide factor
               | lparen factor operand i times factor rparen divide factor'''

    logging.info("p_factors")
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] / p[3]
    elif len(p) == 10:
        p[0] = (p[2] + 1j * p[3] * p[6]) / p[9]


def p_states(p):
    '''states : states times comp_state
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
                  | lbracket factors state operand factors state rbracket'''
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
              | gates times gate
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
    '''gate : gate_x
           | gate_y
           | gate_z
           | gate_s
           | gate_t
           | gate_h
           | gate_i
           | gate_c
           | gate_a
           | gate_swap
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
