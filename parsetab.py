
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE H I LPAREN MINUS NUMBER PLUS RPAREN S SQRT T TIMES X Y Z state_0 state_1 state_i state_minus state_minus_i state_pluscircuit : states gatesfactor : NUMBER\n              | SQRT LPAREN NUMBER RPAREN\n              | NUMBER TIMES SQRT LPAREN NUMBER RPARENfactors : factor\n               | factor DIVIDE factor\n               | LPAREN factor PLUS I TIMES factor RPAREN DIVIDE factor\n               | LPAREN factor MINUS I TIMES factor RPAREN DIVIDE factorstates : state\n              | factors state\n              | factors state MINUS factors state\n              | factors state PLUS factors state state : state_0\n    | state_1\n    | state_plus\n    | state_minus\n    | state_i\n    | state_minus_i gates : gates gate\n                   | gategate : X\n           | Y\n           | Z\n           | S\n           | T\n           | H'
    
_lr_action_items = {'state_0':([0,4,11,13,31,36,37,41,49,54,55,],[5,5,-5,-2,-6,5,5,-3,-4,-7,-8,]),'state_1':([0,4,11,13,31,36,37,41,49,54,55,],[6,6,-5,-2,-6,6,6,-3,-4,-7,-8,]),'state_plus':([0,4,11,13,31,36,37,41,49,54,55,],[7,7,-5,-2,-6,7,7,-3,-4,-7,-8,]),'state_minus':([0,4,11,13,31,36,37,41,49,54,55,],[8,8,-5,-2,-6,8,8,-3,-4,-7,-8,]),'state_i':([0,4,11,13,31,36,37,41,49,54,55,],[9,9,-5,-2,-6,9,9,-3,-4,-7,-8,]),'state_minus_i':([0,4,11,13,31,36,37,41,49,54,55,],[10,10,-5,-2,-6,10,10,-3,-4,-7,-8,]),'LPAREN':([0,14,29,30,34,],[12,27,12,12,40,]),'NUMBER':([0,12,24,27,29,30,40,44,45,52,53,],[13,13,13,35,13,13,46,13,13,13,13,]),'SQRT':([0,12,24,26,29,30,44,45,52,53,],[14,14,14,34,14,14,14,14,14,14,]),'$end':([1,15,16,17,18,19,20,21,22,28,],[0,-1,-20,-21,-22,-23,-24,-25,-26,-19,]),'X':([2,3,5,6,7,8,9,10,15,16,17,18,19,20,21,22,23,28,42,43,],[17,-9,-13,-14,-15,-16,-17,-18,17,-20,-21,-22,-23,-24,-25,-26,-10,-19,-11,-12,]),'Y':([2,3,5,6,7,8,9,10,15,16,17,18,19,20,21,22,23,28,42,43,],[18,-9,-13,-14,-15,-16,-17,-18,18,-20,-21,-22,-23,-24,-25,-26,-10,-19,-11,-12,]),'Z':([2,3,5,6,7,8,9,10,15,16,17,18,19,20,21,22,23,28,42,43,],[19,-9,-13,-14,-15,-16,-17,-18,19,-20,-21,-22,-23,-24,-25,-26,-10,-19,-11,-12,]),'S':([2,3,5,6,7,8,9,10,15,16,17,18,19,20,21,22,23,28,42,43,],[20,-9,-13,-14,-15,-16,-17,-18,20,-20,-21,-22,-23,-24,-25,-26,-10,-19,-11,-12,]),'T':([2,3,5,6,7,8,9,10,15,16,17,18,19,20,21,22,23,28,42,43,],[21,-9,-13,-14,-15,-16,-17,-18,21,-20,-21,-22,-23,-24,-25,-26,-10,-19,-11,-12,]),'H':([2,3,5,6,7,8,9,10,15,16,17,18,19,20,21,22,23,28,42,43,],[22,-9,-13,-14,-15,-16,-17,-18,22,-20,-21,-22,-23,-24,-25,-26,-10,-19,-11,-12,]),'MINUS':([5,6,7,8,9,10,13,23,25,41,49,],[-13,-14,-15,-16,-17,-18,-2,29,33,-3,-4,]),'PLUS':([5,6,7,8,9,10,13,23,25,41,49,],[-13,-14,-15,-16,-17,-18,-2,30,32,-3,-4,]),'DIVIDE':([11,13,41,49,50,51,],[24,-2,-3,-4,52,53,]),'RPAREN':([13,35,41,46,47,48,49,],[-2,41,-3,49,50,51,-4,]),'TIMES':([13,38,39,],[26,44,45,]),'I':([32,33,],[38,39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'circuit':([0,],[1,]),'states':([0,],[2,]),'state':([0,4,36,37,],[3,23,42,43,]),'factors':([0,29,30,],[4,36,37,]),'factor':([0,12,24,29,30,44,45,52,53,],[11,25,31,11,11,47,48,54,55,]),'gates':([2,],[15,]),'gate':([2,15,],[16,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> circuit","S'",1,None,None,None),
  ('circuit -> states gates','circuit',2,'p_circuit','qpycalc.py',16),
  ('factor -> NUMBER','factor',1,'p_factor','qpycalc.py',26),
  ('factor -> SQRT LPAREN NUMBER RPAREN','factor',4,'p_factor','qpycalc.py',27),
  ('factor -> NUMBER TIMES SQRT LPAREN NUMBER RPAREN','factor',6,'p_factor','qpycalc.py',28),
  ('factors -> factor','factors',1,'p_factors','qpycalc.py',37),
  ('factors -> factor DIVIDE factor','factors',3,'p_factors','qpycalc.py',38),
  ('factors -> LPAREN factor PLUS I TIMES factor RPAREN DIVIDE factor','factors',9,'p_factors','qpycalc.py',39),
  ('factors -> LPAREN factor MINUS I TIMES factor RPAREN DIVIDE factor','factors',9,'p_factors','qpycalc.py',40),
  ('states -> state','states',1,'p_states','qpycalc.py',49),
  ('states -> factors state','states',2,'p_states','qpycalc.py',50),
  ('states -> factors state MINUS factors state','states',5,'p_states','qpycalc.py',51),
  ('states -> factors state PLUS factors state','states',5,'p_states','qpycalc.py',52),
  ('state -> state_0','state',1,'p_state','qpycalc.py',71),
  ('state -> state_1','state',1,'p_state','qpycalc.py',72),
  ('state -> state_plus','state',1,'p_state','qpycalc.py',73),
  ('state -> state_minus','state',1,'p_state','qpycalc.py',74),
  ('state -> state_i','state',1,'p_state','qpycalc.py',75),
  ('state -> state_minus_i','state',1,'p_state','qpycalc.py',76),
  ('gates -> gates gate','gates',2,'p_gates','qpycalc.py',82),
  ('gates -> gate','gates',1,'p_gates','qpycalc.py',83),
  ('gate -> X','gate',1,'p_gate','qpycalc.py',94),
  ('gate -> Y','gate',1,'p_gate','qpycalc.py',95),
  ('gate -> Z','gate',1,'p_gate','qpycalc.py',96),
  ('gate -> S','gate',1,'p_gate','qpycalc.py',97),
  ('gate -> T','gate',1,'p_gate','qpycalc.py',98),
  ('gate -> H','gate',1,'p_gate','qpycalc.py',99),
]
