import logging

from ply import lex

import qgates
import qstates
from qgates import QGate

reserved = {
    'sqrt': 'SQRT',
    'pi': 'PI',
}

# List of token names
tokens = [
             # 1 qubit states
             'state_0',
             'state_1',
             'state_plus',
             'state_minus',
             'state_i',
             'state_minus_i',
             # gates one qubit
             'gate_x',
             'gate_y',
             'gate_z',
             'gate_s',
             'gate_t',
             'gate_h',
             'gate_i',
             'gate_c',
             'gate_a',
             'gate_swap',
             'gate_custom',
             # digits
             'number',
             # operation
             'plus',
             'minus',
             'times',
             'divide',
             # parentheses
             'lparen',
             'rparen',
             'lbracket',
             'rbracket',
             # math fx
             'i',
             'ID',
         ] + list(reserved.values())


def t_state_0(t):
    r'\|0\>'
    t.value = qstates.qstate_0()
    return t


def t_state_1(t):
    r'\|1\>'
    t.value = qstates.qstate_1()
    return t


def t_state_plus(t):
    r'\|\+\>'
    t.value = qstates.qstate_plus()
    return t


def t_state_minus(t):
    r'\|\-\>'
    t.value = qstates.qstate_minus()
    return t


def t_state_i(t):
    r'\|i\>'
    t.value = qstates.qstate_i()
    return t


def t_state_minus_i(t):
    r'\|\-i\>'
    t.value = qstates.qstate_minus_i()
    return t


def t_gate_x(t):
    'X'
    t.value = qgates.xgate()
    return t


def t_gate_y(t):
    'Y'
    t.value = qgates.ygate()
    return t


def t_gate_z(t):
    'Z'
    t.value = qgates.zgate()
    return t


def t_gate_s(t):
    'S'
    t.value = qgates.sgate()
    return t


def t_gate_t(t):
    'T'
    t.value = qgates.tgate()
    return t


def t_gate_h(t) -> 'QGate':
    'H'
    t.value = qgates.hgate()
    return t


def t_gate_i(t):
    'I'
    t.value = qgates.identity_gate()
    return t


def t_gate_c(t):
    'C'
    t.value = qgates.ctrl_gate()
    return t


def t_gate_a(t):
    'A'
    t.value = qgates.actrl_gate()
    return t


def t_gate_swap(t):
    'W'
    t.value = qgates.swap_gate()
    return t


def t_gate_custom(t):
    'G'
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_i = 'i'
t_times = r'\*'
t_divide = r'/'
t_lparen = r'\('
t_rparen = r'\)'
t_lbracket = r'\['
t_rbracket = r'\]'


def t_plus(t):
    r'\+'
    t.value = float(1.)
    return t


def t_minus(t):
    r'\-'
    t.value = float(-1.)
    return t


def t_number(t):
    r'\d+.\d+'
    t.value = float(t.value)
    return t


def t_ID(t):
    r'[a-z]+'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


# Build the lexer
lexer = lex.lex()

###################################
# tests
data = """
|0>
|1>
|+>
|->
|i>
|-i>
X
Y
Z
S
T
C
A
W
+
-
/
*
sqrt
pi
string
55.0
(
)
[
]
i
"""
# Give the lexer some input
lexer.input(data)

for tok in lexer:
    logging.info(tok)
