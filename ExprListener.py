# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#statment.
    def enterStatment(self, ctx:ExprParser.StatmentContext):
        pass

    # Exit a parse tree produced by ExprParser#statment.
    def exitStatment(self, ctx:ExprParser.StatmentContext):
        pass


    # Enter a parse tree produced by ExprParser#ifstat.
    def enterIfstat(self, ctx:ExprParser.IfstatContext):
        pass

    # Exit a parse tree produced by ExprParser#ifstat.
    def exitIfstat(self, ctx:ExprParser.IfstatContext):
        pass


    # Enter a parse tree produced by ExprParser#funcstat.
    def enterFuncstat(self, ctx:ExprParser.FuncstatContext):
        pass

    # Exit a parse tree produced by ExprParser#funcstat.
    def exitFuncstat(self, ctx:ExprParser.FuncstatContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#func.
    def enterFunc(self, ctx:ExprParser.FuncContext):
        pass

    # Exit a parse tree produced by ExprParser#func.
    def exitFunc(self, ctx:ExprParser.FuncContext):
        pass



del ExprParser