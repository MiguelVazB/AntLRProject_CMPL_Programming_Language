import sys
import antlr4
from antlr4 import *
from CMPLLexer import CMPLLexer
from CMPLParser import CMPLParser
from MyCMPLVisitor import MyCMPLVisitor


def main(argv):
    userInput = ""
    cmpl = MyCMPLVisitor()
    if len(argv) > 1:
        file = open(argv[1], mode='r')
        all_of_it = file.read()
        file.close()
        inputReady = all_of_it.replace("\n", "")
        userInput = InputStream(inputReady)
        lexer = CMPLLexer(userInput)
        stream = CommonTokenStream(lexer)
        parser = CMPLParser(stream)
        tree = parser.prog()

        cmpl.visitProg(tree)  # Evaluate the expression
    else:
        try:
            while userInput != "u0004":
                userInput = InputStream(input("(◔◡◔)✎ ➡ "))

                lexer = CMPLLexer(userInput)
                stream = CommonTokenStream(lexer)
                parser = CMPLParser(stream)
                tree = parser.prog()

                cmpl.visitProg(tree)  # Evaluate the expression
        except EOFError:
            print("That was CMPL right? Good Bye!")


if __name__ == '__main__':
    main(sys.argv)
