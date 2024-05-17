import sys
from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
import re
sys.tracebacklimit=4
class Return:
    def __init__(self, out):
        self.out = out
        
class VisitorInterp(ExprVisitor):
    def __init__(self, global_valiables = {}, functions = {}) -> None:
        super().__init__()
        self.functions = functions
        self.global_variables = global_valiables
        self.local_variables = {}
        
    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        for i in range(0, ctx.getChildCount()-1):
            self.visit(ctx.getChild(i))
        return 0


    # Visit a parse tree produced by ExprParser#statment.
    def visitStatment(self, ctx:ExprParser.StatmentContext):
        if ctx.getChild(0).getText()=='return':
            return Return(self.visit(ctx.getChild(1)))
        elif ctx.getChildCount() == 2 and type(ctx.getChild(0)) == ExprParser.ExprContext:
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by ExprParser#ifstat.
    def visitIfstat(self, ctx:ExprParser.IfstatContext):
        if self.visit(ctx.getChild(2)) == True:
            for i in range(5, ctx.getChildCount()):
                out = self.visit(ctx.getChild(i))
                if isinstance(out, Return):
                    return out

    # Visit a parse tree produced by ExprParser#funcstat.
    def visitFuncstat(self, ctx:ExprParser.FuncstatContext):
        self.functions[ctx.getChild(1).getText()] = ctx
        
    def visitFuncstatOut(self, ctx:ExprParser.FuncstatContext, params: list):
        params_ids = []
        first_statement = 0
        for idx in range(3, ctx.getChildCount(), 2):
            if ctx.getChild(idx).getText() == "{":
                first_statement = idx+1
                break
            params_ids.append(ctx.getChild(idx).getText())
        for idx in range(len(params)):
            self.local_variables[params_ids[idx]] = params[idx]
        for idx in range(first_statement, ctx.getChildCount()):
            out = self.visit(ctx.getChild(idx))
            if isinstance(out, Return):
                return out.out
        return 0

    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        if(type(ctx.getChild(0)) == ExprParser.FuncContext):
            return self.visit(ctx.getChild(0))
        if ctx.getChildCount() == 1:
            if re.search("[a-zA-Z_][a-zA-Z_0-9]*", ctx.getText()):
                return self.local_variables[ctx.getText()]
            else:
                return int(ctx.getText())
        if ctx.getChildCount() == 3:
            v1 = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            v2 = self.visit(ctx.getChild(2))
            if op == "==":
                return v1 == v2
            if op == "+":
                return v1 + v2
            if op == "-":
                return v1 - v2
            if op == "or":
                return v1 or v2

    # Visit a parse tree produced by ExprParser#func.
    def visitFunc(self, ctx:ExprParser.FuncContext):
        if ctx.getChild(0).getText() == 'print':
            print(self.visit(ctx.getChild(2)))
            return None
        params = [self.visit(ctx.getChild(idx)) for idx in range(2, ctx.getChildCount()-1, 2)]
        func_interp = VisitorInterp()
        func_interp.functions =self.functions
        func_interp.global_variables = self.global_variables
        return func_interp.visitFuncstatOut(self.functions[ctx.getChild(0).getText()], params)