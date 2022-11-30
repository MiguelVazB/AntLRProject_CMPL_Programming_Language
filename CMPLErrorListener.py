from antlr4.error.ErrorListener import ErrorListener


class CMPLErrorListener(ErrorListener):

    def __init__(self):
        super(CMPLErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error! check line:{line} column:{column}. "
                        f"There may be a missing parenthesis or curly brackets. "
                        f"Remember the CMPLicity of the language")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception("Context Sensitivity Error!")