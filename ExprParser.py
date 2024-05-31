# Generated from Expr.g4 by ANTLR 4.13.1
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
        4,1,25,159,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,1,1,1,1,2,1,2,3,2,35,8,2,1,3,5,3,38,8,3,10,3,12,3,41,9,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,60,8,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,68,8,5,10,5,12,5,71,
        9,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,
        87,8,9,10,9,12,9,90,9,9,1,9,1,9,1,9,5,9,95,8,9,10,9,12,9,98,9,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,109,8,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,132,8,10,10,10,12,10,135,9,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,
        13,1,13,1,13,5,13,152,8,13,10,13,12,13,155,9,13,1,13,1,13,1,13,0,
        1,20,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,0,166,0,28,1,0,0,
        0,2,30,1,0,0,0,4,34,1,0,0,0,6,39,1,0,0,0,8,59,1,0,0,0,10,61,1,0,
        0,0,12,74,1,0,0,0,14,76,1,0,0,0,16,78,1,0,0,0,18,80,1,0,0,0,20,108,
        1,0,0,0,22,136,1,0,0,0,24,142,1,0,0,0,26,146,1,0,0,0,28,29,5,1,0,
        0,29,1,1,0,0,0,30,31,5,2,0,0,31,3,1,0,0,0,32,35,3,0,0,0,33,35,3,
        2,1,0,34,32,1,0,0,0,34,33,1,0,0,0,35,5,1,0,0,0,36,38,3,8,4,0,37,
        36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,
        0,41,39,1,0,0,0,42,43,5,0,0,1,43,7,1,0,0,0,44,60,3,10,5,0,45,60,
        3,18,9,0,46,47,3,20,10,0,47,48,5,17,0,0,48,60,1,0,0,0,49,50,3,24,
        12,0,50,51,5,17,0,0,51,60,1,0,0,0,52,53,3,22,11,0,53,54,5,17,0,0,
        54,60,1,0,0,0,55,56,5,3,0,0,56,57,3,20,10,0,57,58,5,17,0,0,58,60,
        1,0,0,0,59,44,1,0,0,0,59,45,1,0,0,0,59,46,1,0,0,0,59,49,1,0,0,0,
        59,52,1,0,0,0,59,55,1,0,0,0,60,9,1,0,0,0,61,62,5,13,0,0,62,63,5,
        18,0,0,63,64,3,20,10,0,64,65,5,19,0,0,65,69,5,20,0,0,66,68,3,8,4,
        0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,
        1,0,0,0,71,69,1,0,0,0,72,73,5,21,0,0,73,11,1,0,0,0,74,75,5,25,0,
        0,75,13,1,0,0,0,76,77,5,22,0,0,77,15,1,0,0,0,78,79,5,23,0,0,79,17,
        1,0,0,0,80,81,5,14,0,0,81,82,3,12,6,0,82,83,5,18,0,0,83,88,3,12,
        6,0,84,85,5,16,0,0,85,87,3,12,6,0,86,84,1,0,0,0,87,90,1,0,0,0,88,
        86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,88,1,0,0,0,91,92,5,19,
        0,0,92,96,5,20,0,0,93,95,3,8,4,0,94,93,1,0,0,0,95,98,1,0,0,0,96,
        94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,96,1,0,0,0,99,100,5,21,
        0,0,100,19,1,0,0,0,101,102,6,10,-1,0,102,109,3,12,6,0,103,109,3,
        26,13,0,104,105,5,12,0,0,105,109,3,20,10,4,106,109,3,14,7,0,107,
        109,3,16,8,0,108,101,1,0,0,0,108,103,1,0,0,0,108,104,1,0,0,0,108,
        106,1,0,0,0,108,107,1,0,0,0,109,133,1,0,0,0,110,111,10,10,0,0,111,
        112,5,4,0,0,112,132,3,20,10,11,113,114,10,9,0,0,114,115,5,11,0,0,
        115,132,3,20,10,10,116,117,10,8,0,0,117,118,5,5,0,0,118,132,3,20,
        10,9,119,120,10,7,0,0,120,121,5,6,0,0,121,132,3,20,10,8,122,123,
        10,6,0,0,123,124,5,7,0,0,124,132,3,20,10,7,125,126,10,5,0,0,126,
        127,5,8,0,0,127,132,3,20,10,6,128,129,10,3,0,0,129,130,5,10,0,0,
        130,132,3,20,10,4,131,110,1,0,0,0,131,113,1,0,0,0,131,116,1,0,0,
        0,131,119,1,0,0,0,131,122,1,0,0,0,131,125,1,0,0,0,131,128,1,0,0,
        0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,21,1,0,0,0,
        135,133,1,0,0,0,136,137,3,12,6,0,137,138,5,9,0,0,138,139,3,4,2,0,
        139,140,5,15,0,0,140,141,3,20,10,0,141,23,1,0,0,0,142,143,3,12,6,
        0,143,144,5,15,0,0,144,145,3,20,10,0,145,25,1,0,0,0,146,147,3,12,
        6,0,147,148,5,18,0,0,148,153,3,20,10,0,149,150,5,16,0,0,150,152,
        3,20,10,0,151,149,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,
        1,0,0,0,154,156,1,0,0,0,155,153,1,0,0,0,156,157,5,19,0,0,157,27,
        1,0,0,0,10,34,39,59,69,88,96,108,131,133,153
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'return'", "'=='", 
                     "'*'", "'/'", "'+'", "'-'", "':'", "'and'", "'or'", 
                     "'not'", "'if'", "'def'", "'='", "','", "';'", "'('", 
                     "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "AND", "OR", "NOT", "IF", 
                      "DEF", "EQ", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "INT", "FLOAT", "WS", "ID" ]

    RULE_int_type = 0
    RULE_float_type = 1
    RULE_type = 2
    RULE_program = 3
    RULE_statment = 4
    RULE_ifstat = 5
    RULE_id = 6
    RULE_int = 7
    RULE_float = 8
    RULE_funcstat = 9
    RULE_expr = 10
    RULE_declaration = 11
    RULE_asingment = 12
    RULE_func = 13

    ruleNames =  [ "int_type", "float_type", "type", "program", "statment", 
                   "ifstat", "id", "int", "float", "funcstat", "expr", "declaration", 
                   "asingment", "func" ]

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
    AND=10
    OR=11
    NOT=12
    IF=13
    DEF=14
    EQ=15
    COMMA=16
    SEMI=17
    LPAREN=18
    RPAREN=19
    LCURLY=20
    RCURLY=21
    INT=22
    FLOAT=23
    WS=24
    ID=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Int_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_int_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_type" ):
                listener.enterInt_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_type" ):
                listener.exitInt_type(self)




    def int_type(self):

        localctx = ExprParser.Int_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_int_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(ExprParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_float_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_type" ):
                listener.enterFloat_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_type" ):
                listener.exitFloat_type(self)




    def float_type(self):

        localctx = ExprParser.Float_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_float_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ExprParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_type(self):
            return self.getTypedRuleContext(ExprParser.Int_typeContext,0)


        def float_type(self):
            return self.getTypedRuleContext(ExprParser.Float_typeContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = ExprParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.int_type()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.float_type()
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


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def statment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatmentContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatmentContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 46166024) != 0):
                self.state = 36
                self.statment()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifstat(self):
            return self.getTypedRuleContext(ExprParser.IfstatContext,0)


        def funcstat(self):
            return self.getTypedRuleContext(ExprParser.FuncstatContext,0)


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)

        def asingment(self):
            return self.getTypedRuleContext(ExprParser.AsingmentContext,0)


        def declaration(self):
            return self.getTypedRuleContext(ExprParser.DeclarationContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_statment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatment" ):
                listener.enterStatment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatment" ):
                listener.exitStatment(self)




    def statment(self):

        localctx = ExprParser.StatmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statment)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.ifstat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.funcstat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.expr(0)
                self.state = 47
                self.match(ExprParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.asingment()
                self.state = 50
                self.match(ExprParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.declaration()
                self.state = 53
                self.match(ExprParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.match(ExprParser.T__2)
                self.state = 56
                self.expr(0)
                self.state = 57
                self.match(ExprParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def LCURLY(self):
            return self.getToken(ExprParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(ExprParser.RCURLY, 0)

        def statment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatmentContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatmentContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_ifstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstat" ):
                listener.enterIfstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstat" ):
                listener.exitIfstat(self)




    def ifstat(self):

        localctx = ExprParser.IfstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ExprParser.IF)
            self.state = 62
            self.match(ExprParser.LPAREN)
            self.state = 63
            self.expr(0)
            self.state = 64
            self.match(ExprParser.RPAREN)
            self.state = 65
            self.match(ExprParser.LCURLY)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 46166024) != 0):
                self.state = 66
                self.statment()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(ExprParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)




    def id_(self):

        localctx = ExprParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)




    def int_(self):

        localctx = ExprParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(ExprParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)




    def float_(self):

        localctx = ExprParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ExprParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(ExprParser.DEF, 0)

        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.IdContext)
            else:
                return self.getTypedRuleContext(ExprParser.IdContext,i)


        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def LCURLY(self):
            return self.getToken(ExprParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(ExprParser.RCURLY, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def statment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatmentContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatmentContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_funcstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncstat" ):
                listener.enterFuncstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncstat" ):
                listener.exitFuncstat(self)




    def funcstat(self):

        localctx = ExprParser.FuncstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(ExprParser.DEF)
            self.state = 81
            self.id_()
            self.state = 82
            self.match(ExprParser.LPAREN)
            self.state = 83
            self.id_()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 84
                self.match(ExprParser.COMMA)
                self.state = 85
                self.id_()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self.match(ExprParser.RPAREN)
            self.state = 92
            self.match(ExprParser.LCURLY)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 46166024) != 0):
                self.state = 93
                self.statment()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self.match(ExprParser.RCURLY)
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

        def id_(self):
            return self.getTypedRuleContext(ExprParser.IdContext,0)


        def func(self):
            return self.getTypedRuleContext(ExprParser.FuncContext,0)


        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def int_(self):
            return self.getTypedRuleContext(ExprParser.IntContext,0)


        def float_(self):
            return self.getTypedRuleContext(ExprParser.FloatContext,0)


        def OR(self):
            return self.getToken(ExprParser.OR, 0)

        def AND(self):
            return self.getToken(ExprParser.AND, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 102
                self.id_()
                pass

            elif la_ == 2:
                self.state = 103
                self.func()
                pass

            elif la_ == 3:
                self.state = 104
                self.match(ExprParser.NOT)
                self.state = 105
                self.expr(4)
                pass

            elif la_ == 4:
                self.state = 106
                self.int_()
                pass

            elif la_ == 5:
                self.state = 107
                self.float_()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 131
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 111
                        self.match(ExprParser.T__3)
                        self.state = 112
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 113
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 114
                        self.match(ExprParser.OR)
                        self.state = 115
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 116
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 117
                        self.match(ExprParser.T__4)
                        self.state = 118
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 119
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 120
                        self.match(ExprParser.T__5)
                        self.state = 121
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 123
                        self.match(ExprParser.T__6)
                        self.state = 124
                        self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 125
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 126
                        self.match(ExprParser.T__7)
                        self.state = 127
                        self.expr(6)
                        pass

                    elif la_ == 7:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 129
                        self.match(ExprParser.AND)
                        self.state = 130
                        self.expr(4)
                        pass

             
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(ExprParser.IdContext,0)


        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)


        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = ExprParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.id_()
            self.state = 137
            self.match(ExprParser.T__8)
            self.state = 138
            self.type_()
            self.state = 139
            self.match(ExprParser.EQ)
            self.state = 140
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsingmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(ExprParser.IdContext,0)


        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_asingment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsingment" ):
                listener.enterAsingment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsingment" ):
                listener.exitAsingment(self)




    def asingment(self):

        localctx = ExprParser.AsingmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_asingment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.id_()
            self.state = 143
            self.match(ExprParser.EQ)
            self.state = 144
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(ExprParser.IdContext,0)


        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = ExprParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.id_()
            self.state = 147
            self.match(ExprParser.LPAREN)
            self.state = 148
            self.expr(0)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 149
                self.match(ExprParser.COMMA)
                self.state = 150
                self.expr(0)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.match(ExprParser.RPAREN)
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
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




