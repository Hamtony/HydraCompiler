# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#int_type.
    def enterInt_type(self, ctx:ExprParser.Int_typeContext):
        pass

    # Exit a parse tree produced by ExprParser#int_type.
    def exitInt_type(self, ctx:ExprParser.Int_typeContext):
        pass


    # Enter a parse tree produced by ExprParser#float_type.
    def enterFloat_type(self, ctx:ExprParser.Float_typeContext):
        pass

    # Exit a parse tree produced by ExprParser#float_type.
    def exitFloat_type(self, ctx:ExprParser.Float_typeContext):
        pass


    # Enter a parse tree produced by ExprParser#type.
    def enterType(self, ctx:ExprParser.TypeContext):
        pass

    # Exit a parse tree produced by ExprParser#type.
    def exitType(self, ctx:ExprParser.TypeContext):
        pass


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


    # Enter a parse tree produced by ExprParser#id.
    def enterId(self, ctx:ExprParser.IdContext):
        pass

    # Exit a parse tree produced by ExprParser#id.
    def exitId(self, ctx:ExprParser.IdContext):
        pass


    # Enter a parse tree produced by ExprParser#int.
    def enterInt(self, ctx:ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#int.
    def exitInt(self, ctx:ExprParser.IntContext):
        pass


    # Enter a parse tree produced by ExprParser#float.
    def enterFloat(self, ctx:ExprParser.FloatContext):
        pass

    # Exit a parse tree produced by ExprParser#float.
    def exitFloat(self, ctx:ExprParser.FloatContext):
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


    # Enter a parse tree produced by ExprParser#declaration.
    def enterDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#declaration.
    def exitDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#asingment.
    def enterAsingment(self, ctx:ExprParser.AsingmentContext):
        pass

    # Exit a parse tree produced by ExprParser#asingment.
    def exitAsingment(self, ctx:ExprParser.AsingmentContext):
        pass


    # Enter a parse tree produced by ExprParser#func.
    def enterFunc(self, ctx:ExprParser.FuncContext):
        pass

    # Exit a parse tree produced by ExprParser#func.
    def exitFunc(self, ctx:ExprParser.FuncContext):
        pass



del ExprParser