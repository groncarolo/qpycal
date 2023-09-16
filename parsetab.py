
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ID SQRT divide gate_a gate_c gate_custom gate_h gate_i gate_s gate_swap gate_t gate_x gate_y gate_z i lbracket lparen minus number plus rbracket rparen state_0 state_1 state_i state_minus state_minus_i state_plus timescircuit : states gatesfactor : number\n              | SQRT lparen number rparen\n              | number times SQRT lparen number rparenoperand : minus\n               | plusfactors : factor\n               | factor divide factor\n               | lparen factor operand i times factor rparen divide factorstates : states times comp_state\n    | comp_statecomp_state : named_state\n                  | factors state\n                  | ID factors state\n                  | lbracket factors state operand factors state rbracket\n                  | ID lbracket factors state operand factors state rbracket\n                  named_state : ID state\n    | statestate : state_0\n    | state_1\n    | state_plus\n    | state_minus\n    | state_i\n    | state_minus_igates : gates gate\n              | gates times gate\n              | gatecustom_gate : gate_custom lparen ID rparen gate : gate_x\n           | gate_y\n           | gate_z\n           | gate_s\n           | gate_t\n           | gate_h\n           | gate_i\n           | gate_c\n           | gate_a\n           | gate_swap\n           | custom_gate\n    '
    
_lr_action_items = {'ID':([0,20,46,],[7,7,57,]),'lbracket':([0,7,20,],[8,37,8,]),'lparen':([0,7,8,18,20,33,37,52,53,54,59,64,],[10,10,10,42,10,46,10,-5,-6,61,10,10,]),'state_0':([0,5,7,9,17,20,35,38,48,50,62,65,68,71,77,],[11,11,11,-7,-2,11,11,11,11,-8,-3,11,11,-4,-9,]),'state_1':([0,5,7,9,17,20,35,38,48,50,62,65,68,71,77,],[12,12,12,-7,-2,12,12,12,12,-8,-3,12,12,-4,-9,]),'state_plus':([0,5,7,9,17,20,35,38,48,50,62,65,68,71,77,],[13,13,13,-7,-2,13,13,13,13,-8,-3,13,13,-4,-9,]),'state_minus':([0,5,7,9,17,20,35,38,48,50,62,65,68,71,77,],[14,14,14,-7,-2,14,14,14,14,-8,-3,14,14,-4,-9,]),'state_i':([0,5,7,9,17,20,35,38,48,50,62,65,68,71,77,],[15,15,15,-7,-2,15,15,15,15,-8,-3,15,15,-4,-9,]),'state_minus_i':([0,5,7,9,17,20,35,38,48,50,62,65,68,71,77,],[16,16,16,-7,-2,16,16,16,16,-8,-3,16,16,-4,-9,]),'number':([0,7,8,10,20,37,39,42,52,53,59,61,64,66,76,],[17,17,17,17,17,17,17,55,-5,-6,17,67,17,17,17,]),'SQRT':([0,7,8,10,20,37,39,41,52,53,59,64,66,76,],[18,18,18,18,18,18,18,54,-5,-6,18,18,18,18,]),'$end':([1,19,21,22,23,24,25,26,27,28,29,30,31,32,43,56,63,],[0,-1,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-25,-26,-28,]),'times':([2,3,4,6,11,12,13,14,15,16,17,19,21,22,23,24,25,26,27,28,29,30,31,32,34,36,43,45,47,56,60,63,73,75,],[20,-11,-12,-18,-19,-20,-21,-22,-23,-24,41,44,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-13,-17,-25,-10,-14,-26,66,-28,-15,-16,]),'gate_x':([2,3,4,6,11,12,13,14,15,16,19,21,22,23,24,25,26,27,28,29,30,31,32,34,36,43,44,45,47,56,63,73,75,],[22,-11,-12,-18,-19,-20,-21,-22,-23,-24,22,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-13,-17,-25,22,-10,-14,-26,-28,-15,-16,]),'gate_y':([2,3,4,6,11,12,13,14,15,16,19,21,22,23,24,25,26,27,28,29,30,31,32,34,36,43,44,45,47,56,63,73,75,],[23,-11,-12,-18,-19,-20,-21,-22,-23,-24,23,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-13,-17,-25,23,-10,-14,-26,-28,-15,-16,]),'gate_z':([2,3,4,6,11,12,13,14,15,16,19,21,22,23,24,25,26,27,28,29,30,31,32,34,36,43,44,45,47,56,63,73,75,],[24,-11,-12,-18,-19,-20,-21,-22,-23,-24,24,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-13,-17,-25,24,-10,-14,-26,-28,-15,-16,]),'gate_s':([2,3,4,6,11,12,13,14,15,16,19,21,22,23,24,25,26,27,28,29,30,31,32,34,36,43,44,45,47,56,63,73,75,],[25,-11,-12,-18,-19,-20,-21,-22,-23,-24,25,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-13,-17,-25,25,-10,-14,-26,-28,-15,-16,]),'gate_t':([2,3,4,6,11,12,13,14,15,16,19,21,22,23,24,25,26,27,28,29,30,31,32,34,36,43,44,45,47,56,63,73,75,],[26,-11,-12,-18,-19,-20,-21,-22,-23,-24,26,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-13,-17,-25,26,-10,-14,-26,-28,-15,-16,]),'gate_h':([2,3,4,6,11,12,13,14,15,16,19,21,22,23,24,25,26,27,28,29,30,31,32,34,36,43,44,45,47,56,63,73,75,],[27,-11,-12,-18,-19,-20,-21,-22,-23,-24,27,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-13,-17,-25,27,-10,-14,-26,-28,-15,-16,]),'gate_i':([2,3,4,6,11,12,13,14,15,16,19,21,22,23,24,25,26,27,28,29,30,31,32,34,36,43,44,45,47,56,63,73,75,],[28,-11,-12,-18,-19,-20,-21,-22,-23,-24,28,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-13,-17,-25,28,-10,-14,-26,-28,-15,-16,]),'gate_c':([2,3,4,6,11,12,13,14,15,16,19,21,22,23,24,25,26,27,28,29,30,31,32,34,36,43,44,45,47,56,63,73,75,],[29,-11,-12,-18,-19,-20,-21,-22,-23,-24,29,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-13,-17,-25,29,-10,-14,-26,-28,-15,-16,]),'gate_a':([2,3,4,6,11,12,13,14,15,16,19,21,22,23,24,25,26,27,28,29,30,31,32,34,36,43,44,45,47,56,63,73,75,],[30,-11,-12,-18,-19,-20,-21,-22,-23,-24,30,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-13,-17,-25,30,-10,-14,-26,-28,-15,-16,]),'gate_swap':([2,3,4,6,11,12,13,14,15,16,19,21,22,23,24,25,26,27,28,29,30,31,32,34,36,43,44,45,47,56,63,73,75,],[31,-11,-12,-18,-19,-20,-21,-22,-23,-24,31,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-13,-17,-25,31,-10,-14,-26,-28,-15,-16,]),'gate_custom':([2,3,4,6,11,12,13,14,15,16,19,21,22,23,24,25,26,27,28,29,30,31,32,34,36,43,44,45,47,56,63,73,75,],[33,-11,-12,-18,-19,-20,-21,-22,-23,-24,33,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-13,-17,-25,33,-10,-14,-26,-28,-15,-16,]),'divide':([9,17,62,71,74,],[39,-2,-3,-4,76,]),'minus':([11,12,13,14,15,16,17,40,49,58,62,71,],[-19,-20,-21,-22,-23,-24,-2,52,52,52,-3,-4,]),'plus':([11,12,13,14,15,16,17,40,49,58,62,71,],[-19,-20,-21,-22,-23,-24,-2,53,53,53,-3,-4,]),'rbracket':([11,12,13,14,15,16,69,72,],[-19,-20,-21,-22,-23,-24,73,75,]),'rparen':([17,55,57,62,67,70,71,],[-2,62,63,-3,71,74,-4,]),'i':([51,52,53,],[60,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'circuit':([0,],[1,]),'states':([0,],[2,]),'comp_state':([0,20,],[3,45,]),'named_state':([0,20,],[4,4,]),'factors':([0,7,8,20,37,59,64,],[5,35,38,5,48,65,68,]),'state':([0,5,7,20,35,38,48,65,68,],[6,34,36,6,47,49,58,69,72,]),'factor':([0,7,8,10,20,37,39,59,64,66,76,],[9,9,9,40,9,9,50,9,9,70,77,]),'gates':([2,],[19,]),'gate':([2,19,44,],[21,43,56,]),'custom_gate':([2,19,44,],[32,32,32,]),'operand':([40,49,58,],[51,59,64,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> circuit","S'",1,None,None,None),
  ('circuit -> states gates','circuit',2,'p_circuit','qparser.py',13),
  ('factor -> number','factor',1,'p_factor','qparser.py',20),
  ('factor -> SQRT lparen number rparen','factor',4,'p_factor','qparser.py',21),
  ('factor -> number times SQRT lparen number rparen','factor',6,'p_factor','qparser.py',22),
  ('operand -> minus','operand',1,'p_opearand','qparser.py',33),
  ('operand -> plus','operand',1,'p_opearand','qparser.py',34),
  ('factors -> factor','factors',1,'p_factors','qparser.py',40),
  ('factors -> factor divide factor','factors',3,'p_factors','qparser.py',41),
  ('factors -> lparen factor operand i times factor rparen divide factor','factors',9,'p_factors','qparser.py',42),
  ('states -> states times comp_state','states',3,'p_states','qparser.py',54),
  ('states -> comp_state','states',1,'p_states','qparser.py',55),
  ('comp_state -> named_state','comp_state',1,'p_comp_states','qparser.py',67),
  ('comp_state -> factors state','comp_state',2,'p_comp_states','qparser.py',68),
  ('comp_state -> ID factors state','comp_state',3,'p_comp_states','qparser.py',69),
  ('comp_state -> lbracket factors state operand factors state rbracket','comp_state',7,'p_comp_states','qparser.py',70),
  ('comp_state -> ID lbracket factors state operand factors state rbracket','comp_state',8,'p_comp_states','qparser.py',71),
  ('named_state -> ID state','named_state',2,'p_named_state','qparser.py',109),
  ('named_state -> state','named_state',1,'p_named_state','qparser.py',110),
  ('state -> state_0','state',1,'p_state','qparser.py',120),
  ('state -> state_1','state',1,'p_state','qparser.py',121),
  ('state -> state_plus','state',1,'p_state','qparser.py',122),
  ('state -> state_minus','state',1,'p_state','qparser.py',123),
  ('state -> state_i','state',1,'p_state','qparser.py',124),
  ('state -> state_minus_i','state',1,'p_state','qparser.py',125),
  ('gates -> gates gate','gates',2,'p_gates','qparser.py',132),
  ('gates -> gates times gate','gates',3,'p_gates','qparser.py',133),
  ('gates -> gate','gates',1,'p_gates','qparser.py',134),
  ('custom_gate -> gate_custom lparen ID rparen','custom_gate',4,'p_custom_gate','qparser.py',154),
  ('gate -> gate_x','gate',1,'p_gate','qparser.py',159),
  ('gate -> gate_y','gate',1,'p_gate','qparser.py',160),
  ('gate -> gate_z','gate',1,'p_gate','qparser.py',161),
  ('gate -> gate_s','gate',1,'p_gate','qparser.py',162),
  ('gate -> gate_t','gate',1,'p_gate','qparser.py',163),
  ('gate -> gate_h','gate',1,'p_gate','qparser.py',164),
  ('gate -> gate_i','gate',1,'p_gate','qparser.py',165),
  ('gate -> gate_c','gate',1,'p_gate','qparser.py',166),
  ('gate -> gate_a','gate',1,'p_gate','qparser.py',167),
  ('gate -> gate_swap','gate',1,'p_gate','qparser.py',168),
  ('gate -> custom_gate','gate',1,'p_gate','qparser.py',169),
]
