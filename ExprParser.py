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
        4,1,19,104,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,1,3,1,3,1,3,5,3,54,8,3,10,3,
        12,3,57,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,70,8,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,
        4,87,8,4,10,4,12,4,90,9,4,1,5,1,5,1,5,1,5,1,5,5,5,97,8,5,10,5,12,
        5,100,9,5,1,5,1,5,1,5,0,1,8,6,0,2,4,6,8,10,0,0,113,0,15,1,0,0,0,
        2,29,1,0,0,0,4,31,1,0,0,0,6,39,1,0,0,0,8,69,1,0,0,0,10,91,1,0,0,
        0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,
        1,0,0,0,16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,
        30,3,4,2,0,21,30,3,6,3,0,22,23,3,8,4,0,23,24,5,12,0,0,24,30,1,0,
        0,0,25,26,5,1,0,0,26,27,3,8,4,0,27,28,5,12,0,0,28,30,1,0,0,0,29,
        20,1,0,0,0,29,21,1,0,0,0,29,22,1,0,0,0,29,25,1,0,0,0,30,3,1,0,0,
        0,31,32,5,8,0,0,32,33,5,13,0,0,33,34,3,8,4,0,34,35,5,14,0,0,35,36,
        5,15,0,0,36,37,3,2,1,0,37,38,5,16,0,0,38,5,1,0,0,0,39,40,5,9,0,0,
        40,41,5,19,0,0,41,42,5,13,0,0,42,47,5,19,0,0,43,44,5,11,0,0,44,46,
        5,19,0,0,45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,
        48,50,1,0,0,0,49,47,1,0,0,0,50,51,5,14,0,0,51,55,5,15,0,0,52,54,
        3,2,1,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,
        56,58,1,0,0,0,57,55,1,0,0,0,58,59,5,16,0,0,59,7,1,0,0,0,60,61,6,
        4,-1,0,61,70,5,19,0,0,62,70,3,10,5,0,63,64,5,19,0,0,64,65,5,10,0,
        0,65,70,3,8,4,6,66,67,5,7,0,0,67,70,3,8,4,3,68,70,5,17,0,0,69,60,
        1,0,0,0,69,62,1,0,0,0,69,63,1,0,0,0,69,66,1,0,0,0,69,68,1,0,0,0,
        70,88,1,0,0,0,71,72,10,8,0,0,72,73,5,2,0,0,73,87,3,8,4,9,74,75,10,
        7,0,0,75,76,5,6,0,0,76,87,3,8,4,8,77,78,10,5,0,0,78,79,5,3,0,0,79,
        87,3,8,4,6,80,81,10,4,0,0,81,82,5,4,0,0,82,87,3,8,4,5,83,84,10,2,
        0,0,84,85,5,5,0,0,85,87,3,8,4,3,86,71,1,0,0,0,86,74,1,0,0,0,86,77,
        1,0,0,0,86,80,1,0,0,0,86,83,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,
        88,89,1,0,0,0,89,9,1,0,0,0,90,88,1,0,0,0,91,92,5,19,0,0,92,93,5,
        13,0,0,93,98,3,8,4,0,94,95,5,11,0,0,95,97,3,8,4,0,96,94,1,0,0,0,
        97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,
        1,0,0,0,101,102,5,14,0,0,102,11,1,0,0,0,8,15,29,47,55,69,86,88,98
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return'", "'=='", "'+'", "'-'", "'and'", 
                     "'or'", "'not'", "'if'", "'def'", "'='", "','", "';'", 
                     "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "AND", "OR", "NOT", "IF", "DEF", "EQ", 
                      "COMMA", "SEMI", "LPAREN", "RPAREN", "LCURLY", "RCURLY", 
                      "INT", "WS", "ID" ]

    RULE_program = 0
    RULE_statment = 1
    RULE_ifstat = 2
    RULE_funcstat = 3
    RULE_expr = 4
    RULE_func = 5

    ruleNames =  [ "program", "statment", "ifstat", "funcstat", "expr", 
                   "func" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    AND=5
    OR=6
    NOT=7
    IF=8
    DEF=9
    EQ=10
    COMMA=11
    SEMI=12
    LPAREN=13
    RPAREN=14
    LCURLY=15
    RCURLY=16
    INT=17
    WS=18
    ID=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 656258) != 0):
                self.state = 12
                self.statment()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
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

        def getRuleIndex(self):
            return ExprParser.RULE_statment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatment" ):
                listener.enterStatment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatment" ):
                listener.exitStatment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatment" ):
                return visitor.visitStatment(self)
            else:
                return visitor.visitChildren(self)




    def statment(self):

        localctx = ExprParser.StatmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statment)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.ifstat()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.funcstat()
                pass
            elif token in [7, 17, 19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.expr(0)
                self.state = 23
                self.match(ExprParser.SEMI)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.match(ExprParser.T__0)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(ExprParser.SEMI)
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

        def statment(self):
            return self.getTypedRuleContext(ExprParser.StatmentContext,0)


        def RCURLY(self):
            return self.getToken(ExprParser.RCURLY, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_ifstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstat" ):
                listener.enterIfstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstat" ):
                listener.exitIfstat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstat" ):
                return visitor.visitIfstat(self)
            else:
                return visitor.visitChildren(self)




    def ifstat(self):

        localctx = ExprParser.IfstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifstat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ExprParser.IF)
            self.state = 32
            self.match(ExprParser.LPAREN)
            self.state = 33
            self.expr(0)
            self.state = 34
            self.match(ExprParser.RPAREN)
            self.state = 35
            self.match(ExprParser.LCURLY)
            self.state = 36
            self.statment()
            self.state = 37
            self.match(ExprParser.RCURLY)
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncstat" ):
                return visitor.visitFuncstat(self)
            else:
                return visitor.visitChildren(self)




    def funcstat(self):

        localctx = ExprParser.FuncstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(ExprParser.DEF)
            self.state = 40
            self.match(ExprParser.ID)
            self.state = 41
            self.match(ExprParser.LPAREN)
            self.state = 42
            self.match(ExprParser.ID)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 43
                self.match(ExprParser.COMMA)
                self.state = 44
                self.match(ExprParser.ID)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(ExprParser.RPAREN)
            self.state = 51
            self.match(ExprParser.LCURLY)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 656258) != 0):
                self.state = 52
                self.statment()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
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

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def func(self):
            return self.getTypedRuleContext(ExprParser.FuncContext,0)


        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 61
                self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                self.state = 62
                self.func()
                pass

            elif la_ == 3:
                self.state = 63
                self.match(ExprParser.ID)
                self.state = 64
                self.match(ExprParser.EQ)
                self.state = 65
                self.expr(6)
                pass

            elif la_ == 4:
                self.state = 66
                self.match(ExprParser.NOT)
                self.state = 67
                self.expr(3)
                pass

            elif la_ == 5:
                self.state = 68
                self.match(ExprParser.INT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 86
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 72
                        self.match(ExprParser.T__1)
                        self.state = 73
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 75
                        self.match(ExprParser.OR)
                        self.state = 76
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 78
                        self.match(ExprParser.T__2)
                        self.state = 79
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 80
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 81
                        self.match(ExprParser.T__3)
                        self.state = 82
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 84
                        self.match(ExprParser.AND)
                        self.state = 85
                        self.expr(3)
                        pass

             
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = ExprParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(ExprParser.ID)
            self.state = 92
            self.match(ExprParser.LPAREN)
            self.state = 93
            self.expr(0)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 94
                self.match(ExprParser.COMMA)
                self.state = 95
                self.expr(0)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
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
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




