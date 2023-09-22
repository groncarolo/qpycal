import logging

from ply import yacc

from qcustomgate import get_custom_gate
from qgates import GenericZGate, XGate, YGate, ZGate, GenericXGate, GenericYGate
from qlexer import tokens
from qsolver import solve_circuit

import numpy as np


def p_circuit(p):
    '''circuit : states gates'''
    ret, prob = solve_circuit(p[1], p[2])
    p[0] = ret, prob, len(p[1])


def p_float(p):
    '''float : number
             | minus number '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = -1 * p[1]


def p_factor(p):
    '''factor : float
              | SQRT lparen float rparen
              | float  times SQRT lparen float rparen'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 5:
        p[0] = np.sqrt(p[3])
    elif len(p) == 7:
        p[0] = p[1] * np.sqrt(p[5])


def p_opearand(p):
    '''operand : minus
               | plus'''
    p[0] = 1.0 * p[1]


def p_factors(p):
    '''factors : factor
               | factor divide factor
               | lparen factor operand i times factor rparen divide factor'''

    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] / p[3]
    elif len(p) == 10:
        p[0] = (p[2] + 1j * p[3] * p[6]) / p[9]


def p_states(p):
    '''states : states times comp_state
    | comp_state'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]


def p_comp_states(p):
    '''comp_state : named_state
                  | factors state
                  | ID factors state
                  | lbracket factors state operand factors state rbracket
                  | ID lbracket factors state operand factors state rbracket
                  '''

    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        s = p[2]
        s.state = s.state * p[1]
        s.label = str(p[1]) + s.label
        p[0] = s
    elif len(p) == 4:
        s = p[3]
        s.state = s.state * p[2]
        s.label = str(p[2]) + s.label
        s.name = p[1]
        p[0] = s

    elif len(p) == 8:
        s1 = p[3]
        s1.state = s1.state * p[2]
        s2 = p[6]
        s2.state = s2.state * p[4] * p[5]
        s1.state = s1.state + s2.state
        s1.label = str(f"{p[2]:.3f}") + s1.label + str(f"{p[4] * p[5]:.3f}") + s2.label

        p[0] = s1
    elif len(p) == 9:
        s1 = p[4]
        s1.state = s1.state * p[3]
        s2 = p[7]
        s2.state = s2.state * p[5] * p[6]
        s1.state = s1.state + s2.state
        s1.label = str(f"{p[3]:.3f}") + s1.label + str(f"{p[5] * p[6]:.3f}") + s2.label

        s1.name = p[1]
        p[0] = s1


def p_named_state(p):
    '''named_state : ID state
    | state'''
    if len(p) == 3:
        p[0] = p[2]
        p[0].name = p[1]
    else:
        p[0] = p[1]


def p_state(p):
    '''state : state_0
    | state_1
    | state_plus
    | state_minus
    | state_i
    | state_minus_i'''
    p[0] = p[1]


def p_gates(p):
    r'''gates : gates gate
              | gates times gate
              | gate'''

    if len(p) == 2:
        # create a list
        p[0] = [[p[1]]]
    elif len(p) == 4:
        last = p[1][len(p[1]) - 1]
        last.append(p[3])
        p[0] = p[1]
    else:
        last = p[1]
        last.append([p[2]])
        p[0] = p[1]


def p_custom_gate(p):
    '''custom_gate : gate_custom lparen ID rparen '''
    p[0] = get_custom_gate(p[3])


def p_pi_factor(p):
    '''pi_factor : lparen PI rparen
                 | lparen float rparen
                 | lparen PI divide float rparen'''
    if len(p) == 4:
        if p.slice[2].type == "number":
            p[0] = np.deg2rad(p[2])
        else:
            p[0] = np.pi
    else:
        p[0] = np.pi / p[4]


def p_gate(p):
    '''gate : gate_x
           | gate_x pi_factor
           | gate_y
           | gate_y pi_factor
           | gate_z
           | gate_z pi_factor
           | gate_s
           | gate_t
           | gate_h
           | gate_i
           | gate_c
           | gate_a
           | gate_swap
           | custom_gate
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if isinstance(p[1], XGate):
            p[0] = GenericXGate(p[2])
        if isinstance(p[1], YGate):
            p[0] = GenericYGate(p[2])
        if isinstance(p[1], ZGate):
            p[0] = GenericZGate(p[2])


# Error rule for syntax errors
def p_error(p):
    logging.error("Syntax error in input! %s", str(p))
    raise RuntimeError


# Build the parser
log = logging.getLogger()
parser = yacc.yacc(debug=True, debuglog=log)


def parse_and_solve(data, debug=False):
    return parser.parse(data, debug=log)
