import ply.yacc as yacc
import logging

from qgates import apply
from qstates import is_normalized
from qutils import *
from qlexer import tokens


def p_circuit(p):
    '''circuit : states gates'''
    logging.info("p_circuit")

    if not (is_normalized(p[1])):
        raise
    ret = p[1].state
    for g in p[2]:
        ret = apply(g, ret)

    p[0] = ret


def p_factor(p):
    '''factor : NUMBER
              | SQRT LPAREN NUMBER RPAREN
              | NUMBER TIMES SQRT LPAREN NUMBER RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
        log.info("factor: " + str(p[0]))
    elif len(p) == 5:
        p[0] = p[1](p[3])
        log.info("factor: " + str(p[0]))
    elif len(p) == 7:
        p[0] = p[1] * p[3](p[5])
        log.info("factor: " + str(p[0]))


def p_opearand(p):
    '''operand : MINUS
                  | PLUS'''
    p[0] = 1.0 * p[1]


def p_factors(p):
    '''factors : factor
               | factor DIVIDE factor
               | LPAREN factor operand i TIMES factor RPAREN DIVIDE factor'''

    if len(p) == 2:
        p[0] = p[1]
        logging.info("factors: " + str(p[0]))
    elif len(p) == 4:
        p[0] = p[1] / p[3]
        logging.info("factors: " + str(p[0]))
    elif len(p) == 10:
        p[0] = (p[2] + 1j * p[3] * p[6]) / p[9]
        logging.info("factors: " + str(p[0]))


def p_states(p):
    '''states : state
              | factors state
              | factors state operand factors state'''
    logging.info("p_states")
    if len(p) == 2:
        p[0] = p[1]
        logging.info("states s: " + str(p[0].state))
    elif len(p) == 3:
        s = p[2]
        s.state = s.state * p[1]
        p[0] = s
        logging.info("states s: " + str(p[0].state))
    elif len(p) == 6:
        s1 = p[2]
        s1.state = s1.state * p[1]
        logging.info("states s1: " + str(s1.state))

        s2 = p[5]
        s2.state = s2.state * p[3] * p[4]
        logging.info("states s2: " + str(s2.state))
        s1.state = s1.state + s2.state
        p[0] = s1
        logging.info("states s: " + str(p[0].state))


def p_state(p):
    '''state : state_0
    | state_1
    | state_plus
    | state_minus
    | state_i
    | state_minus_i '''
    logging.info("p_state")
    p[0] = p[1]
    logging.info("state " + str(p[0].state))


def p_gates(p):
    r'''gates : gates gate
                   | gate'''
    logging.info("p_gates")

    if len(p) > 2:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_gate(p):
    '''gate : X
           | Y
           | Z
           | S
           | T
           | H
           | I
    '''
    p[0] = p[1]
    logging.info("gate " + str(p[0].gate))


# Error rule for syntax errors
def p_error(p):
    logging.error("Syntax error in input!")
    raise RuntimeError


# Build the parser
log = logging.getLogger()
parser = yacc.yacc(debug=True, debuglog=log)


def calculate(data):
    return parser.parse(data, debug=log)


def main():
    while True:
        try:
            s = input('qpycal > ')
        except EOFError:
            break
        if not s: continue
        ret = calculate(s)
        print(ret)
        if (len(ret) == 2):
            ret_r_ph_th = complex_2_spherical_coordinates(ret)
            ret_xyz = complex_2_cartesian_coordinates(ret)
            print_spherical_coordinates(ret_r_ph_th)
            print_cartesian_coordinates(ret_xyz)
        break


if __name__ == "__main__":
    main()
