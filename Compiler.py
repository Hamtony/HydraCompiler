from llvmlite.ir import Module
from llvmlite import ir
from ExprVisitor import ExprVisitor
from ExprParser import ExprParser
from enviroment import Enviroment
ir.instructions
class Compiler:
    def __init__(self) -> None:
        self.visitor = ExprVisitor()
        self.type_map = {
            'int': ir.IntType(32),
            'float': ir.FloatType()
        }
        self.module = Module('main')
        self.builder = ir.IRBuilder()
        self.env: Enviroment = Enviroment()
        
        
    def visit_program(self, ctx: ExprParser.ProgramContext):
        func_name: str = "main"
        param_types = []
        return_type : ir.Type = self.type_map["int"]
        fnty = ir.FunctionType(return_type, param_types)
        func = ir.Function(self.module, fnty, name=func_name)
        
        block = func.append_basic_block(f"{func_name}_entry")
        
        self.builder = ir.IRBuilder(block)
        
        for stat in ctx.getChildren():
            self.compile(stat)
            
        return_value = ir.Constant(self.type_map["int"],69)
        self.builder.ret(return_value)
        
    def visit_statement(self, ctx:ExprParser.StatmentContext):
        if ((ctx.funcstat()) != None):
            print("is a func stat")
        elif ((ctx.ifstat()) != None):
            self.visit_ifstat(ctx.ifstat())
        elif ((ctx.expr()) != None and ctx.getChildCount() == 2):
            self.visit_expr(ctx.expr())
        elif (ctx.declaration() != None):
            self.visit_declaration(ctx.declaration())
        elif (ctx.asingment() != None):
            self.visit_asingment(ctx.asingment())
        
    def visit_ifstat(self, ctx:ExprParser.StatmentContext):
        pass
            
    
    def visit_expr(self, ctx:ExprParser.ExprContext):
        if isinstance(ctx.getChild(0), ExprParser.IdContext):
            return self.resolve_value(ctx.getChild(0))
        if ctx.getChildCount() == 3:
            if ctx.getChild(1).getText() == "=":#assingment
                pass
            else:#operation
                operator = ctx.getChild(1).getText()
                left_value, left_type = self.resolve_value(ctx.getChild(0))
                right_value, right_type = self.resolve_value(ctx.getChild(2))
                value = None
                dtype = None
                if isinstance(right_type, ir.IntType) and isinstance(left_type, ir.IntType):
                    dtype = self.type_map['int']
                    match operator:
                        case '+':
                            value = self.builder.add(left_value,right_value)
                        case '-':
                            value = self.builder.sub(left_value,right_value)
                        case '*':
                            value = self.builder.mul(left_value,right_value)
                        case '/':
                            value = self.builder.sdiv(left_value,right_value)
                        case '%':
                            value = self.builder.srem(left_value,right_value)
                        case '^':
                            pass
                    return value, dtype
                elif isinstance(right_type, ir.FloatType) and isinstance(left_type, ir.FloatType):
                    dtype = self.type_map['float']
                    match operator:
                        case '+':
                            value = self.builder.fadd(left_value,right_value)
                        case '-':
                            value = self.builder.fsub(left_value,right_value)
                        case '*':
                            value = self.builder.fmul(left_value,right_value)
                        case '/':
                            value = self.builder.fdiv(left_value,right_value)
                        case '+':
                            value = self.builder.frem(left_value,right_value)
                        case '^':
                            pass
                    return value, dtype
        elif isinstance(ctx.getChild(0), ExprParser.IntContext) or isinstance(ctx.getChild(0), ExprParser.FloatContext):
            return self.resolve_value(ctx.getChild(0))
        
    def compile(self, node):
        if isinstance(node, ExprParser.ProgramContext):
            self.visit_program(node)
        if isinstance(node, ExprParser.StatmentContext):
            self.visit_statement(node)
        if isinstance(node, ExprParser.ExprContext):
            self.visit_expr(node)
        if isinstance(node, ExprParser.DeclarationContext):
            self.visit_declaration(node)
    
    def visit_declaration(self, node: ExprParser.DeclarationContext):
        name = node.getChild(0).getText()
        value = node.getChild(4)
        value_type: str = node.getChild(2).getText()
        #TODO
        value, dtype = self.resolve_value(value)
        
        if self.env.lookup(name) is None:
            ptr = self.builder.alloca(dtype)
            self.builder.store(value,ptr)
            print(name,"\n" ,ptr,"\n",dtype, "\n")
            self.env.define(name,ptr,dtype)
        else:
            print(name,"\n")
            ptr, _ = self.env.lookup(name)
            self.builder.store(value, ptr)
            
    def visit_asingment(self, node: ExprParser.AsingmentContext):
        name = node.getChild(0).getText()
        value = node.getChild(2)
        
        value, dtype = self.resolve_value(value)

        ptr, _ = self.env.lookup(name)
        self.builder.store(value, ptr)
        
        
                
    def resolve_value(self, node):
        if isinstance(node, ExprParser.IntContext):
            node:ExprParser.IntContext = node
            value, dtype =  int(node.getChild(0).getText()),self.type_map['int']
            return ir.Constant(dtype,value),dtype
        elif isinstance(node, ExprParser.FloatContext):
            node:ExprParser.FloatContext = node
            value, dtype =  float(node.getChild(0).getText()),self.type_map['float']
            return ir.Constant(dtype,value),dtype
        elif isinstance(node, ExprParser.IdContext):
            node:ExprParser.IdContext = node
            ptr, dtype = self.env.lookup(node.getChild(0).getText())
            return self.builder.load(ptr), dtype
        elif isinstance(node, ExprParser.ExprContext):
            return self.visit_expr(node)
        else:
            raise TypeError(f'Not valid value in {node.getText()}')

            