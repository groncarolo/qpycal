import logging

from ply import yacc

from qgates import apply_gate, Gate
from qstates import is_normalized, State
from qutils import tensor_prod
from qlexer import tokens

def p_circuit(p):
    '''circuit : states gates'''
    logging.info("p_circuit")

    if not is_normalized(p[1]):
        raise
    ret = p[1].state
    for g in p[2]:
        logging.info("Multiplying:")
        logging.info(ret)
        logging.info("*")
        logging.info(g.gate)
        ret = apply_gate(g, ret)
        logging.info("=")
        logging.info(ret)

    p[0] = ret


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
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = State(tensor_prod(p[1].state, p[3].state))


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
        p[0] = [p[1]]
    elif len(p) == 4:
        last = p[1][len(p[1]) - 1]
        r = Gate(tensor_prod(last.gate, p[3].gate))
        p[1][len(p[1]) - 1] = r
        p[0] = p[1]
    else:
        logging.info("p_gates: append")
        p[1].append(p[2])
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
    logging.error("Syntax error in input! %s" , str(p))
    raise RuntimeError


# Build the parser
log = logging.getLogger()
parser = yacc.yacc(debug=True, debuglog=log)


def parse_and_calculate(data):
    return parser.parse(data, debug=log)
