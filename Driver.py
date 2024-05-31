import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from VisitorInterp import VisitorInterp
from Compiler import Compiler
import time
import llvmlite.binding as llvm
from ctypes import CFUNCTYPE, c_int, c_float


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        compiler = Compiler()
        compiler.visit_program(tree)
        module = compiler.module
        module.triple = llvm.get_default_triple()
        with open("debug/program.ll","w") as f:
            f.write(str(module))

if __name__ == '__main__':
    main(sys.argv)