import sys
from antlr4 import *

from CMPLErrorListener import CMPLErrorListener
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
        userInput = InputStream(all_of_it)
        lexer = CMPLLexer(userInput)
        lexer.removeErrorListeners()
        lexer.addErrorListener(CMPLErrorListener())

        stream = CommonTokenStream(lexer)

        parser = CMPLParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(CMPLErrorListener())
        try:
            tree = parser.prog()
            cmpl.visitProg(tree)  # Evaluate the expression
        except Exception as e:
            print(e)
    else:
        try:
            while userInput != "u0004":
                userInput = InputStream(input("(◔◡◔)✎ ➡ "))
                lexer = CMPLLexer(userInput)
                lexer.removeErrorListeners()

                stream = CommonTokenStream(lexer)

                parser = CMPLParser(stream)
                parser.removeErrorListeners()
                parser.addErrorListener(CMPLErrorListener())
                try:
                    tree = parser.prog()
                    cmpl.visitProg(tree)  # Evaluate the expression
                except Exception as e:
                    print(e)

        except EOFError:
            print("That was CMPL right? Good Bye!")


if __name__ == '__main__':
    main(sys.argv)
