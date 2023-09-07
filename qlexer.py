import logging

import ply.lex as lex
import numpy as np

import qgates
import qstates

# List of token names
tokens = (
    # 1 qubit states
    'state_0',
    'state_1',
    'state_plus',
    'state_minus',
    'state_i',
    'state_minus_i',
    # gates one qubit
    'X',
    'Y',
    'Z',
    'S',
    'T',
    'H',
    'I',
    # gates two qubit
    'C',
    'A',
    # digits
    'NUMBER',
    # operation
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    # parentheses
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    # math fx
    'i',
    'SQRT',
)


def t_state_0(t):
    r'\|0\>'
    t.value = qstates.State0()
    return t


def t_state_1(t):
    r'\|1\>'
    t.value = qstates.State1()
    return t


def t_state_plus(t):
    r'\|\+\>'
    t.value = qstates.StatePlus()
    return t


def t_state_minus(t):
    r'\|\-\>'
    t.value = qstates.StateMinus()
    return t


def t_state_i(t):
    r'\|i\>'
    t.value = qstates.StateI()
    return t


def t_state_minus_i(t):
    r'\|\-i\>'
    t.value = qstates.StateMinusI()
    return t


def t_X(t):
    'X'
    t.value = qgates.XGate()
    return t


def t_Y(t):
    'Y'
    t.value = qgates.YGate()
    return t


def t_Z(t):
    'Z'
    t.value = qgates.ZGate()
    return t


def t_S(t):
    'S'
    t.value = qgates.SGate()
    return t


def t_T(t):
    'T'
    t.value = qgates.TGate()
    return t


def t_H(t):
    'H'
    t.value = qgates.HGate()
    return t


def t_I(t):
    'I'
    t.value = qgates.Identity()
    return t


def t_C(t):
    'C'
    t.value = qgates.Ctrl()
    return t


def t_A(t):
    'A'
    t.value = qgates.ACtrl()
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
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'


def t_PLUS(t):
    r'\+'
    t.value = float(1.)
    return t


def t_MINUS(t):
    r'\-'
    t.value = float(-1.)
    return t


def t_NUMBER(t):
    r'\d+.\d+'
    t.value = float(t.value)
    return t


def t_SQRT(t):
    r'sqrt'
    t.value = np.sqrt
    return t


# Build the lexer
lexer = lex.lex()

###################################
# tests
data = '''
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
+
-
/
*
sqrt
55.0
(
)
[
]
i
'''
# Give the lexer some input
lexer.input(data)

for tok in lexer:
    logging.info(tok)
