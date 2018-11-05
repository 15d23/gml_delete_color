
# dot_parser_tab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARROW COLON COMMA COMMENT DDASH DIGRAPH EDGE EQUAL GRAPH ID LCURLY LSQUARE NODE RCURLY RSQUARE SEMI STRICT SUBGRAPHGraphs : GraphGraphs : Graphs GraphGraph : GraphStmtGraph : COMMENTGraphStmt : GraphType GraphBodyGraphStmt : GraphType ID GraphBodyGraphStmt : STRICT GraphType GraphBodyGraphStmt : STRICT GraphType ID GraphBody\n        GraphType : GRAPH\n                  | DIGRAPH\n        GraphBody : LCURLY StmtList RCURLYGraphBody : LCURLY RCURLY\n        StmtList : Stmt\n                 | Stmt SEMI\n        \n        StmtList : Stmt StmtList\n                 | Stmt SEMI StmtList\n        Stmt : ID EQUAL IDStmt : NodeStmtStmt : EdgeStmtStmt : AttrStmtStmt : SubGraphStmt : COMMENTNodeStmt : NodeIdNodeStmt : NodeId AttrListNodeId : IDNodeId : ID PortPort : COLON IDPort : COLON ID COLON IDAttrStmt : AttrType AttrList\n        AttrType : NODE\n                 | EDGE\n                 | GRAPH\n        AttrList : LSQUARE RSQUAREAttrList : LSQUARE AList RSQUAREAttrList : LSQUARE RSQUARE AttrListAttrList : LSQUARE AList RSQUARE AttrListAList : AExprAList : AExpr AList\n        AExpr : ID EQUAL ID\n              | ID EQUAL ID COMMA\n              | ID EQUAL ID SEMI\n        \n        EdgeStmt : EdgeReciever EdgeRHS\n                 | EdgeReciever EdgeRHS AttrList\n        EdgeReciever : NodeIdEdgeReciever : SubGraphEdgeRHS : EdgeOp EdgeRecieverEdgeRHS : EdgeOp EdgeReciever EdgeRHS\n        EdgeOp : ARROW\n               | DDASH\n        SubGraph : GraphBodySubGraph : SUBGRAPH GraphBodySubGraph : SUBGRAPH ID GraphBody'
    
_lr_action_items = {'COMMENT':([0,1,2,5,6,9,10,12,14,17,18,20,21,22,27,28,29,30,31,32,36,38,40,42,43,45,46,49,50,51,52,53,54,55,60,61,62,63,64,65,69,71,],[1,-4,-3,1,-1,-5,18,-2,-21,-20,-22,-12,-50,18,-23,-19,-25,-18,-6,-7,-42,-11,-29,18,-51,-24,-26,-8,-45,-44,-46,-25,-43,-33,-52,-27,-17,-47,-35,-34,-36,-28,]),'NODE':([10,14,17,18,20,21,22,27,28,29,30,36,38,40,42,43,45,46,50,51,52,53,54,55,60,61,62,63,64,65,69,71,],[24,-21,-20,-22,-12,-50,24,-23,-19,-25,-18,-42,-11,-29,24,-51,-24,-26,-45,-44,-46,-25,-43,-33,-52,-27,-17,-47,-35,-34,-36,-28,]),'SEMI':([14,17,18,20,21,22,27,28,29,30,36,38,40,43,45,46,50,51,52,53,54,55,60,61,62,63,64,65,69,70,71,],[-21,-20,-22,-12,-50,42,-23,-19,-25,-18,-42,-11,-29,-51,-24,-26,-45,-44,-46,-25,-43,-33,-52,-27,-17,-47,-35,-34,-36,73,-28,]),'SUBGRAPH':([10,14,17,18,20,21,22,27,28,29,30,34,35,36,37,38,40,42,43,45,46,50,51,52,53,54,55,60,61,62,63,64,65,69,71,],[25,-21,-20,-22,-12,-50,25,-23,-19,-25,-18,-49,25,-42,-48,-11,-29,25,-51,-24,-26,-45,-44,-46,-25,-43,-33,-52,-27,-17,-47,-35,-34,-36,-28,]),'LCURLY':([3,4,7,10,11,13,14,17,18,20,21,22,25,27,28,29,30,33,34,35,36,37,38,40,42,43,44,45,46,50,51,52,53,54,55,60,61,62,63,64,65,69,71,],[-10,10,-9,10,10,10,-21,-20,-22,-12,-50,10,10,-23,-19,-25,-18,10,-49,10,-42,-48,-11,-29,10,-51,10,-24,-26,-45,-44,-46,-25,-43,-33,-52,-27,-17,-47,-35,-34,-36,-28,]),'DIGRAPH':([0,1,2,5,6,8,9,12,20,31,32,38,49,],[3,-4,-3,3,-1,3,-5,-2,-12,-6,-7,-11,-8,]),'GRAPH':([0,1,2,5,6,8,9,10,12,14,17,18,20,21,22,27,28,29,30,31,32,36,38,40,42,43,45,46,49,50,51,52,53,54,55,60,61,62,63,64,65,69,71,],[7,-4,-3,7,-1,7,-5,26,-2,-21,-20,-22,-12,-50,26,-23,-19,-25,-18,-6,-7,-42,-11,-29,26,-51,-24,-26,-8,-45,-44,-46,-25,-43,-33,-52,-27,-17,-47,-35,-34,-36,-28,]),'RCURLY':([10,14,16,17,18,20,21,22,27,28,29,30,36,38,40,41,42,43,45,46,50,51,52,53,54,55,59,60,61,62,63,64,65,69,71,],[20,-21,38,-20,-22,-12,-50,-13,-23,-19,-25,-18,-42,-11,-29,-15,-14,-51,-24,-26,-45,-44,-46,-25,-43,-33,-16,-52,-27,-17,-47,-35,-34,-36,-28,]),'EQUAL':([29,57,],[48,66,]),'STRICT':([0,1,2,5,6,9,12,20,31,32,38,49,],[8,-4,-3,8,-1,-5,-2,-12,-6,-7,-11,-8,]),'EDGE':([10,14,17,18,20,21,22,27,28,29,30,36,38,40,42,43,45,46,50,51,52,53,54,55,60,61,62,63,64,65,69,71,],[23,-21,-20,-22,-12,-50,23,-23,-19,-25,-18,-42,-11,-29,23,-51,-24,-26,-45,-44,-46,-25,-43,-33,-52,-27,-17,-47,-35,-34,-36,-28,]),'COLON':([29,53,61,],[47,47,68,]),'ARROW':([14,15,20,21,27,29,38,43,46,50,51,52,53,60,61,71,],[-45,37,-12,-50,-44,-25,-11,-51,-26,-45,-44,37,-25,-52,-27,-28,]),'RSQUARE':([39,56,58,67,70,72,73,],[55,65,-37,-38,-39,-40,-41,]),'COMMA':([70,],[72,]),'DDASH':([14,15,20,21,27,29,38,43,46,50,51,52,53,60,61,71,],[-45,34,-12,-50,-44,-25,-11,-51,-26,-45,-44,34,-25,-52,-27,-28,]),'LSQUARE':([19,20,21,23,24,26,27,29,36,38,43,46,50,51,52,53,55,60,61,63,65,71,],[39,-12,-50,-31,-30,-32,39,-25,39,-11,-51,-26,-45,-44,-46,-25,39,-52,-27,-47,39,-28,]),'ID':([3,4,7,10,13,14,17,18,20,21,22,25,27,28,29,30,34,35,36,37,38,39,40,42,43,45,46,47,48,50,51,52,53,54,55,58,60,61,62,63,64,65,66,68,69,70,71,72,73,],[-10,11,-9,29,33,-21,-20,-22,-12,-50,29,44,-23,-19,-25,-18,-49,53,-42,-48,-11,57,-29,29,-51,-24,-26,61,62,-45,-44,-46,-25,-43,-33,57,-52,-27,-17,-47,-35,-34,70,71,-36,-39,-28,-40,-41,]),'$end':([1,2,5,6,9,12,20,31,32,38,49,],[-4,-3,0,-1,-5,-2,-12,-6,-7,-11,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'AttrList':([19,27,36,55,65,],[40,45,54,64,69,]),'AttrType':([10,22,42,],[19,19,19,]),'SubGraph':([10,22,35,42,],[14,14,50,14,]),'GraphStmt':([0,5,],[2,2,]),'EdgeOp':([15,52,],[35,35,]),'GraphBody':([4,10,11,13,22,25,33,35,42,44,],[9,21,31,32,21,43,49,21,21,60,]),'AExpr':([39,58,],[58,58,]),'AList':([39,58,],[56,67,]),'GraphType':([0,5,8,],[4,4,13,]),'Stmt':([10,22,42,],[22,22,22,]),'NodeId':([10,22,35,42,],[27,27,51,27,]),'Graphs':([0,],[5,]),'EdgeRHS':([15,52,],[36,63,]),'EdgeReciever':([10,22,35,42,],[15,15,52,15,]),'StmtList':([10,22,42,],[16,41,59,]),'Graph':([0,5,],[6,12,]),'EdgeStmt':([10,22,42,],[28,28,28,]),'Port':([29,53,],[46,46,]),'NodeStmt':([10,22,42,],[30,30,30,]),'AttrStmt':([10,22,42,],[17,17,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Graphs","S'",1,None,None,None),
  ('Graphs -> Graph','Graphs',1,'p_Graphs_1','dot_parser.py',65),
  ('Graphs -> Graphs Graph','Graphs',2,'p_Graphs_3','dot_parser.py',68),
  ('Graph -> GraphStmt','Graph',1,'p_Graph_1','dot_parser.py',72),
  ('Graph -> COMMENT','Graph',1,'p_Graph_2','dot_parser.py',75),
  ('GraphStmt -> GraphType GraphBody','GraphStmt',2,'p_GraphStmt_1','dot_parser.py',79),
  ('GraphStmt -> GraphType ID GraphBody','GraphStmt',3,'p_GraphStmt_2','dot_parser.py',82),
  ('GraphStmt -> STRICT GraphType GraphBody','GraphStmt',3,'p_GraphStmt_3','dot_parser.py',85),
  ('GraphStmt -> STRICT GraphType ID GraphBody','GraphStmt',4,'p_GraphStmt_4','dot_parser.py',88),
  ('GraphType -> GRAPH','GraphType',1,'p_GraphType_1','dot_parser.py',93),
  ('GraphType -> DIGRAPH','GraphType',1,'p_GraphType_1','dot_parser.py',94),
  ('GraphBody -> LCURLY StmtList RCURLY','GraphBody',3,'p_GraphBody_1','dot_parser.py',99),
  ('GraphBody -> LCURLY RCURLY','GraphBody',2,'p_GraphBody_3','dot_parser.py',102),
  ('StmtList -> Stmt','StmtList',1,'p_StmtList_1','dot_parser.py',107),
  ('StmtList -> Stmt SEMI','StmtList',2,'p_StmtList_1','dot_parser.py',108),
  ('StmtList -> Stmt StmtList','StmtList',2,'p_StmtList_2','dot_parser.py',113),
  ('StmtList -> Stmt SEMI StmtList','StmtList',3,'p_StmtList_2','dot_parser.py',114),
  ('Stmt -> ID EQUAL ID','Stmt',3,'p_Stmt_1','dot_parser.py',129),
  ('Stmt -> NodeStmt','Stmt',1,'p_Stmt_2','dot_parser.py',132),
  ('Stmt -> EdgeStmt','Stmt',1,'p_Stmt_3','dot_parser.py',135),
  ('Stmt -> AttrStmt','Stmt',1,'p_Stmt_4','dot_parser.py',138),
  ('Stmt -> SubGraph','Stmt',1,'p_Stmt_5','dot_parser.py',141),
  ('Stmt -> COMMENT','Stmt',1,'p_Stmt_6','dot_parser.py',144),
  ('NodeStmt -> NodeId','NodeStmt',1,'p_NodeStmt_1','dot_parser.py',148),
  ('NodeStmt -> NodeId AttrList','NodeStmt',2,'p_NodeStmt_2','dot_parser.py',151),
  ('NodeId -> ID','NodeId',1,'p_NodeId_1','dot_parser.py',155),
  ('NodeId -> ID Port','NodeId',2,'p_NodeId_2','dot_parser.py',158),
  ('Port -> COLON ID','Port',2,'p_Port_1','dot_parser.py',162),
  ('Port -> COLON ID COLON ID','Port',4,'p_Port_2','dot_parser.py',165),
  ('AttrStmt -> AttrType AttrList','AttrStmt',2,'p_AttrStmt_1','dot_parser.py',171),
  ('AttrType -> NODE','AttrType',1,'p_AttrType_1','dot_parser.py',176),
  ('AttrType -> EDGE','AttrType',1,'p_AttrType_1','dot_parser.py',177),
  ('AttrType -> GRAPH','AttrType',1,'p_AttrType_1','dot_parser.py',178),
  ('AttrList -> LSQUARE RSQUARE','AttrList',2,'p_AttrList_1','dot_parser.py',183),
  ('AttrList -> LSQUARE AList RSQUARE','AttrList',3,'p_AttrList_2','dot_parser.py',186),
  ('AttrList -> LSQUARE RSQUARE AttrList','AttrList',3,'p_AttrList_3','dot_parser.py',189),
  ('AttrList -> LSQUARE AList RSQUARE AttrList','AttrList',4,'p_AttrList_4','dot_parser.py',192),
  ('AList -> AExpr','AList',1,'p_AList_1','dot_parser.py',196),
  ('AList -> AExpr AList','AList',2,'p_AList_2','dot_parser.py',199),
  ('AExpr -> ID EQUAL ID','AExpr',3,'p_AExpr_1','dot_parser.py',204),
  ('AExpr -> ID EQUAL ID COMMA','AExpr',4,'p_AExpr_1','dot_parser.py',205),
  ('AExpr -> ID EQUAL ID SEMI','AExpr',4,'p_AExpr_1','dot_parser.py',206),
  ('EdgeStmt -> EdgeReciever EdgeRHS','EdgeStmt',2,'p_EdgeStmt_1','dot_parser.py',212),
  ('EdgeStmt -> EdgeReciever EdgeRHS AttrList','EdgeStmt',3,'p_EdgeStmt_1','dot_parser.py',213),
  ('EdgeReciever -> NodeId','EdgeReciever',1,'p_EdgeReciever_1','dot_parser.py',226),
  ('EdgeReciever -> SubGraph','EdgeReciever',1,'p_EdgeReciever_2','dot_parser.py',229),
  ('EdgeRHS -> EdgeOp EdgeReciever','EdgeRHS',2,'p_EdgeRHS_1','dot_parser.py',233),
  ('EdgeRHS -> EdgeOp EdgeReciever EdgeRHS','EdgeRHS',3,'p_EdgeRHS_2','dot_parser.py',236),
  ('EdgeOp -> ARROW','EdgeOp',1,'p_EdgeOp_1','dot_parser.py',241),
  ('EdgeOp -> DDASH','EdgeOp',1,'p_EdgeOp_1','dot_parser.py',242),
  ('SubGraph -> GraphBody','SubGraph',1,'p_SubGraph_1','dot_parser.py',247),
  ('SubGraph -> SUBGRAPH GraphBody','SubGraph',2,'p_SubGraph_2','dot_parser.py',250),
  ('SubGraph -> SUBGRAPH ID GraphBody','SubGraph',3,'p_SubGraph_3','dot_parser.py',253),
]