import sys

from antlr4 import *
from antlr4.atn import ATNConfigSet
from antlr4.error.ErrorListener import ErrorListener


class CMPLErrorListener(ErrorListener):

    def __init__(self):
        super(CMPLErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error! check line:{line} column:{column}. "
                        f"There may be a missing paranthesis or curly brackets. "
                        f"Remember the CMPLicity of the language")

    def reportAmbiguity(self, recognizer: Parser, dfa: DFA, startIndex: int,
                        stopIndex: int, exact: bool, ambigAlts: set, configs: ATNConfigSet):
        raise Exception("Ambiguity error!")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception("Context Error!")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception("Context Sensitivity Error!")