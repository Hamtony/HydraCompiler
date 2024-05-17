# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statment.
    def visitStatment(self, ctx:ExprParser.StatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifstat.
    def visitIfstat(self, ctx:ExprParser.IfstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#funcstat.
    def visitFuncstat(self, ctx:ExprParser.FuncstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#func.
    def visitFunc(self, ctx:ExprParser.FuncContext):
        return self.visitChildren(ctx)



del ExprParser