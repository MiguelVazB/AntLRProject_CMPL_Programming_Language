# Generated from CMPL.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,157,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,1,1,1,1,1,3,1,40,8,1,1,
        2,1,2,1,2,3,2,45,8,2,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,3,1,3,1,3,
        1,3,1,3,3,3,58,8,3,1,4,1,4,3,4,62,8,4,1,5,1,5,1,5,1,5,1,6,5,6,69,
        8,6,10,6,12,6,72,9,6,1,6,1,6,5,6,76,8,6,10,6,12,6,79,9,6,1,6,5,6,
        82,8,6,10,6,12,6,85,9,6,1,6,5,6,88,8,6,10,6,12,6,91,9,6,1,6,1,6,
        5,6,95,8,6,10,6,12,6,98,9,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,107,
        8,8,1,8,3,8,110,8,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,118,8,9,1,9,1,9,
        1,9,3,9,123,8,9,3,9,125,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,144,8,9,10,9,12,9,147,9,9,1,
        10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,13,0,1,18,14,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,0,6,1,0,19,20,1,0,17,18,1,0,27,28,2,0,22,
        25,31,31,1,0,9,14,1,0,15,16,166,0,31,1,0,0,0,2,39,1,0,0,0,4,44,1,
        0,0,0,6,52,1,0,0,0,8,61,1,0,0,0,10,63,1,0,0,0,12,70,1,0,0,0,14,99,
        1,0,0,0,16,103,1,0,0,0,18,124,1,0,0,0,20,148,1,0,0,0,22,150,1,0,
        0,0,24,152,1,0,0,0,26,154,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,
        33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,
        0,34,35,5,0,0,1,35,1,1,0,0,0,36,40,3,4,2,0,37,40,3,6,3,0,38,40,3,
        10,5,0,39,36,1,0,0,0,39,37,1,0,0,0,39,38,1,0,0,0,40,3,1,0,0,0,41,
        45,3,14,7,0,42,45,3,18,9,0,43,45,3,16,8,0,44,41,1,0,0,0,44,42,1,
        0,0,0,44,43,1,0,0,0,45,49,1,0,0,0,46,48,5,30,0,0,47,46,1,0,0,0,48,
        51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,5,1,0,0,0,51,49,1,0,0,
        0,52,53,5,1,0,0,53,54,3,18,9,0,54,57,3,12,6,0,55,56,5,2,0,0,56,58,
        3,8,4,0,57,55,1,0,0,0,57,58,1,0,0,0,58,7,1,0,0,0,59,62,3,12,6,0,
        60,62,3,6,3,0,61,59,1,0,0,0,61,60,1,0,0,0,62,9,1,0,0,0,63,64,5,26,
        0,0,64,65,3,18,9,0,65,66,3,12,6,0,66,11,1,0,0,0,67,69,5,30,0,0,68,
        67,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,
        0,72,70,1,0,0,0,73,77,5,3,0,0,74,76,5,30,0,0,75,74,1,0,0,0,76,79,
        1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,83,1,0,0,0,79,77,1,0,0,0,
        80,82,3,2,1,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,
        0,0,0,84,89,1,0,0,0,85,83,1,0,0,0,86,88,5,30,0,0,87,86,1,0,0,0,88,
        91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,89,1,0,0,
        0,92,96,5,4,0,0,93,95,5,30,0,0,94,93,1,0,0,0,95,98,1,0,0,0,96,94,
        1,0,0,0,96,97,1,0,0,0,97,13,1,0,0,0,98,96,1,0,0,0,99,100,5,29,0,
        0,100,101,5,5,0,0,101,102,3,18,9,0,102,15,1,0,0,0,103,104,5,6,0,
        0,104,106,5,7,0,0,105,107,3,18,9,0,106,105,1,0,0,0,106,107,1,0,0,
        0,107,109,1,0,0,0,108,110,3,20,10,0,109,108,1,0,0,0,109,110,1,0,
        0,0,110,111,1,0,0,0,111,112,5,8,0,0,112,17,1,0,0,0,113,114,6,9,-1,
        0,114,125,3,22,11,0,115,117,5,7,0,0,116,118,3,18,9,0,117,116,1,0,
        0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,125,5,8,0,0,120,122,5,29,
        0,0,121,123,3,20,10,0,122,121,1,0,0,0,122,123,1,0,0,0,123,125,1,
        0,0,0,124,113,1,0,0,0,124,115,1,0,0,0,124,120,1,0,0,0,125,145,1,
        0,0,0,126,127,10,6,0,0,127,128,5,21,0,0,128,144,3,18,9,7,129,130,
        10,5,0,0,130,131,7,0,0,0,131,144,3,18,9,6,132,133,10,4,0,0,133,134,
        7,1,0,0,134,144,3,18,9,5,135,136,10,3,0,0,136,137,3,24,12,0,137,
        138,3,18,9,4,138,144,1,0,0,0,139,140,10,2,0,0,140,141,3,26,13,0,
        141,142,3,18,9,3,142,144,1,0,0,0,143,126,1,0,0,0,143,129,1,0,0,0,
        143,132,1,0,0,0,143,135,1,0,0,0,143,139,1,0,0,0,144,147,1,0,0,0,
        145,143,1,0,0,0,145,146,1,0,0,0,146,19,1,0,0,0,147,145,1,0,0,0,148,
        149,7,2,0,0,149,21,1,0,0,0,150,151,7,3,0,0,151,23,1,0,0,0,152,153,
        7,4,0,0,153,25,1,0,0,0,154,155,7,5,0,0,155,27,1,0,0,0,18,31,39,44,
        49,57,61,70,77,83,89,96,106,109,117,122,124,143,145
    ]

class CMPLParser ( Parser ):

    grammarFileName = "CMPL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'{'", "'}'", "'='", 
                     "'show'", "'('", "')'", "'equals'", "'not equals'", 
                     "'greater'", "'smaller'", "'greater or equal'", "'smaller or equal'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'^'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'null'", "'while'", 
                     "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", 
                      "OP_POW", "FLOAT", "BOOLEAN", "STRING", "NULL", "WHILE", 
                      "PLUS_PLUS", "MINUS_MINUS", "VAR", "NEWLINE", "INT", 
                      "WS" ]

    RULE_prog = 0
    RULE_stmts = 1
    RULE_stmt = 2
    RULE_if_scope = 3
    RULE_else_if_scope = 4
    RULE_while_scope = 5
    RULE_scope = 6
    RULE_variable_stmt = 7
    RULE_show_stmt = 8
    RULE_expr = 9
    RULE_plus_plus_minus_minus = 10
    RULE_data_type = 11
    RULE_comparison_op = 12
    RULE_logic_op = 13

    ruleNames =  [ "prog", "stmts", "stmt", "if_scope", "else_if_scope", 
                   "while_scope", "scope", "variable_stmt", "show_stmt", 
                   "expr", "plus_plus_minus_minus", "data_type", "comparison_op", 
                   "logic_op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    OP_ADD=17
    OP_SUB=18
    OP_MUL=19
    OP_DIV=20
    OP_POW=21
    FLOAT=22
    BOOLEAN=23
    STRING=24
    NULL=25
    WHILE=26
    PLUS_PLUS=27
    MINUS_MINUS=28
    VAR=29
    NEWLINE=30
    INT=31
    WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CMPLParser.EOF, 0)

        def stmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMPLParser.StmtsContext)
            else:
                return self.getTypedRuleContext(CMPLParser.StmtsContext,i)


        def getRuleIndex(self):
            return CMPLParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CMPLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 2814378178) != 0:
                self.state = 28
                self.stmts()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(CMPLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CMPLParser.StmtContext,0)


        def if_scope(self):
            return self.getTypedRuleContext(CMPLParser.If_scopeContext,0)


        def while_scope(self):
            return self.getTypedRuleContext(CMPLParser.While_scopeContext,0)


        def getRuleIndex(self):
            return CMPLParser.RULE_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmts" ):
                listener.enterStmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmts" ):
                listener.exitStmts(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = CMPLParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmts)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 22, 23, 24, 25, 29, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.stmt()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.if_scope()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.while_scope()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_stmt(self):
            return self.getTypedRuleContext(CMPLParser.Variable_stmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(CMPLParser.ExprContext,0)


        def show_stmt(self):
            return self.getTypedRuleContext(CMPLParser.Show_stmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CMPLParser.NEWLINE)
            else:
                return self.getToken(CMPLParser.NEWLINE, i)

        def getRuleIndex(self):
            return CMPLParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CMPLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 41
                self.variable_stmt()
                pass

            elif la_ == 2:
                self.state = 42
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 43
                self.show_stmt()
                pass


            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 46
                    self.match(CMPLParser.NEWLINE) 
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_scopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CMPLParser.ExprContext,0)


        def scope(self):
            return self.getTypedRuleContext(CMPLParser.ScopeContext,0)


        def else_if_scope(self):
            return self.getTypedRuleContext(CMPLParser.Else_if_scopeContext,0)


        def getRuleIndex(self):
            return CMPLParser.RULE_if_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_scope" ):
                listener.enterIf_scope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_scope" ):
                listener.exitIf_scope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_scope" ):
                return visitor.visitIf_scope(self)
            else:
                return visitor.visitChildren(self)




    def if_scope(self):

        localctx = CMPLParser.If_scopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(CMPLParser.T__0)
            self.state = 53
            self.expr(0)
            self.state = 54
            self.scope()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 55
                self.match(CMPLParser.T__1)
                self.state = 56
                self.else_if_scope()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_scopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scope(self):
            return self.getTypedRuleContext(CMPLParser.ScopeContext,0)


        def if_scope(self):
            return self.getTypedRuleContext(CMPLParser.If_scopeContext,0)


        def getRuleIndex(self):
            return CMPLParser.RULE_else_if_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_if_scope" ):
                listener.enterElse_if_scope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_if_scope" ):
                listener.exitElse_if_scope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_scope" ):
                return visitor.visitElse_if_scope(self)
            else:
                return visitor.visitChildren(self)




    def else_if_scope(self):

        localctx = CMPLParser.Else_if_scopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_else_if_scope)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.scope()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.if_scope()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_scopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CMPLParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(CMPLParser.ExprContext,0)


        def scope(self):
            return self.getTypedRuleContext(CMPLParser.ScopeContext,0)


        def getRuleIndex(self):
            return CMPLParser.RULE_while_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_scope" ):
                listener.enterWhile_scope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_scope" ):
                listener.exitWhile_scope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_scope" ):
                return visitor.visitWhile_scope(self)
            else:
                return visitor.visitChildren(self)




    def while_scope(self):

        localctx = CMPLParser.While_scopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_while_scope)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(CMPLParser.WHILE)
            self.state = 64
            self.expr(0)
            self.state = 65
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CMPLParser.NEWLINE)
            else:
                return self.getToken(CMPLParser.NEWLINE, i)

        def stmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMPLParser.StmtsContext)
            else:
                return self.getTypedRuleContext(CMPLParser.StmtsContext,i)


        def getRuleIndex(self):
            return CMPLParser.RULE_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScope" ):
                listener.enterScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScope" ):
                listener.exitScope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScope" ):
                return visitor.visitScope(self)
            else:
                return visitor.visitChildren(self)




    def scope(self):

        localctx = CMPLParser.ScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 67
                self.match(CMPLParser.NEWLINE)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self.match(CMPLParser.T__2)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 74
                    self.match(CMPLParser.NEWLINE) 
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 2814378178) != 0:
                self.state = 80
                self.stmts()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 86
                self.match(CMPLParser.NEWLINE)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(CMPLParser.T__3)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 93
                    self.match(CMPLParser.NEWLINE) 
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CMPLParser.RULE_variable_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarStatementContext(Variable_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CMPLParser.Variable_stmtContext
            super().__init__(parser)
            self.var = None # Token
            self.exp = None # ExprContext
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(CMPLParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(CMPLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarStatement" ):
                listener.enterVarStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarStatement" ):
                listener.exitVarStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarStatement" ):
                return visitor.visitVarStatement(self)
            else:
                return visitor.visitChildren(self)



    def variable_stmt(self):

        localctx = CMPLParser.Variable_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable_stmt)
        try:
            localctx = CMPLParser.VarStatementContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            localctx.var = self.match(CMPLParser.VAR)
            self.state = 100
            self.match(CMPLParser.T__4)
            self.state = 101
            localctx.exp = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Show_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CMPLParser.RULE_show_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ShowStatementContext(Show_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CMPLParser.Show_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CMPLParser.ExprContext,0)

        def plus_plus_minus_minus(self):
            return self.getTypedRuleContext(CMPLParser.Plus_plus_minus_minusContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShowStatement" ):
                listener.enterShowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShowStatement" ):
                listener.exitShowStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowStatement" ):
                return visitor.visitShowStatement(self)
            else:
                return visitor.visitChildren(self)



    def show_stmt(self):

        localctx = CMPLParser.Show_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_show_stmt)
        self._la = 0 # Token type
        try:
            localctx = CMPLParser.ShowStatementContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(CMPLParser.T__5)
            self.state = 104
            self.match(CMPLParser.T__6)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 2747269248) != 0:
                self.state = 105
                self.expr(0)


            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27 or _la==28:
                self.state = 108
                self.plus_plus_minus_minus()


            self.state = 111
            self.match(CMPLParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CMPLParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CMPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(CMPLParser.VAR, 0)
        def plus_plus_minus_minus(self):
            return self.getTypedRuleContext(CMPLParser.Plus_plus_minus_minusContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarExpr" ):
                listener.enterVarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarExpr" ):
                listener.exitVarExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CMPLParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(CMPLParser.ExprContext,i)

        def OP_POW(self):
            return self.getToken(CMPLParser.OP_POW, 0)
        def OP_MUL(self):
            return self.getToken(CMPLParser.OP_MUL, 0)
        def OP_DIV(self):
            return self.getToken(CMPLParser.OP_DIV, 0)
        def OP_ADD(self):
            return self.getToken(CMPLParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(CMPLParser.OP_SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)


    class TypeExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CMPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def data_type(self):
            return self.getTypedRuleContext(CMPLParser.Data_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeExpr" ):
                listener.enterTypeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeExpr" ):
                listener.exitTypeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeExpr" ):
                return visitor.visitTypeExpr(self)
            else:
                return visitor.visitChildren(self)


    class LogicExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CMPLParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Logic_opContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(CMPLParser.ExprContext,i)

        def logic_op(self):
            return self.getTypedRuleContext(CMPLParser.Logic_opContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicExpr" ):
                listener.enterLogicExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicExpr" ):
                listener.exitLogicExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr" ):
                return visitor.visitLogicExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CMPLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CMPLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class CompareExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CMPLParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Comparison_opContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CMPLParser.ExprContext)
            else:
                return self.getTypedRuleContext(CMPLParser.ExprContext,i)

        def comparison_op(self):
            return self.getTypedRuleContext(CMPLParser.Comparison_opContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareExpr" ):
                listener.enterCompareExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareExpr" ):
                listener.exitCompareExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExpr" ):
                return visitor.visitCompareExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CMPLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24, 25, 31]:
                localctx = CMPLParser.TypeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 114
                self.data_type()
                pass
            elif token in [7]:
                localctx = CMPLParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(CMPLParser.T__6)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 2747269248) != 0:
                    self.state = 116
                    self.expr(0)


                self.state = 119
                self.match(CMPLParser.T__7)
                pass
            elif token in [29]:
                localctx = CMPLParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(CMPLParser.VAR)
                self.state = 122
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 121
                    self.plus_plus_minus_minus()


                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 143
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = CMPLParser.InfixExprContext(self, CMPLParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 126
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 127
                        localctx.op = self.match(CMPLParser.OP_POW)
                        self.state = 128
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = CMPLParser.InfixExprContext(self, CMPLParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 129
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 130
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 131
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = CMPLParser.InfixExprContext(self, CMPLParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 132
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 133
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 134
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = CMPLParser.CompareExprContext(self, CMPLParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 135
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 136
                        localctx.op = self.comparison_op()
                        self.state = 137
                        localctx.right = self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = CMPLParser.LogicExprContext(self, CMPLParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 139
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 140
                        localctx.op = self.logic_op()
                        self.state = 141
                        localctx.right = self.expr(3)
                        pass

             
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Plus_plus_minus_minusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS_PLUS(self):
            return self.getToken(CMPLParser.PLUS_PLUS, 0)

        def MINUS_MINUS(self):
            return self.getToken(CMPLParser.MINUS_MINUS, 0)

        def getRuleIndex(self):
            return CMPLParser.RULE_plus_plus_minus_minus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlus_plus_minus_minus" ):
                listener.enterPlus_plus_minus_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlus_plus_minus_minus" ):
                listener.exitPlus_plus_minus_minus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlus_plus_minus_minus" ):
                return visitor.visitPlus_plus_minus_minus(self)
            else:
                return visitor.visitChildren(self)




    def plus_plus_minus_minus(self):

        localctx = CMPLParser.Plus_plus_minus_minusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_plus_plus_minus_minus)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CMPLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CMPLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(CMPLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(CMPLParser.STRING, 0)

        def NULL(self):
            return self.getToken(CMPLParser.NULL, 0)

        def getRuleIndex(self):
            return CMPLParser.RULE_data_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_type" ):
                listener.enterData_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_type" ):
                listener.exitData_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = CMPLParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 2210398208) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CMPLParser.RULE_comparison_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_op" ):
                listener.enterComparison_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_op" ):
                listener.exitComparison_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison_op" ):
                return visitor.visitComparison_op(self)
            else:
                return visitor.visitChildren(self)




    def comparison_op(self):

        localctx = CMPLParser.Comparison_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comparison_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CMPLParser.RULE_logic_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_op" ):
                listener.enterLogic_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_op" ):
                listener.exitLogic_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_op" ):
                return visitor.visitLogic_op(self)
            else:
                return visitor.visitChildren(self)




    def logic_op(self):

        localctx = CMPLParser.Logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




