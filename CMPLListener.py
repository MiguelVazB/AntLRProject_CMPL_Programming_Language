# Generated from CMPL.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CMPLParser import CMPLParser
else:
    from CMPLParser import CMPLParser

# This class defines a complete listener for a parse tree produced by CMPLParser.
class CMPLListener(ParseTreeListener):

    # Enter a parse tree produced by CMPLParser#prog.
    def enterProg(self, ctx:CMPLParser.ProgContext):
        pass

    # Exit a parse tree produced by CMPLParser#prog.
    def exitProg(self, ctx:CMPLParser.ProgContext):
        pass


    # Enter a parse tree produced by CMPLParser#stmts.
    def enterStmts(self, ctx:CMPLParser.StmtsContext):
        pass

    # Exit a parse tree produced by CMPLParser#stmts.
    def exitStmts(self, ctx:CMPLParser.StmtsContext):
        pass


    # Enter a parse tree produced by CMPLParser#stmt.
    def enterStmt(self, ctx:CMPLParser.StmtContext):
        pass

    # Exit a parse tree produced by CMPLParser#stmt.
    def exitStmt(self, ctx:CMPLParser.StmtContext):
        pass


    # Enter a parse tree produced by CMPLParser#if_scope.
    def enterIf_scope(self, ctx:CMPLParser.If_scopeContext):
        pass

    # Exit a parse tree produced by CMPLParser#if_scope.
    def exitIf_scope(self, ctx:CMPLParser.If_scopeContext):
        pass


    # Enter a parse tree produced by CMPLParser#else_if_scope.
    def enterElse_if_scope(self, ctx:CMPLParser.Else_if_scopeContext):
        pass

    # Exit a parse tree produced by CMPLParser#else_if_scope.
    def exitElse_if_scope(self, ctx:CMPLParser.Else_if_scopeContext):
        pass


    # Enter a parse tree produced by CMPLParser#while_scope.
    def enterWhile_scope(self, ctx:CMPLParser.While_scopeContext):
        pass

    # Exit a parse tree produced by CMPLParser#while_scope.
    def exitWhile_scope(self, ctx:CMPLParser.While_scopeContext):
        pass


    # Enter a parse tree produced by CMPLParser#scope.
    def enterScope(self, ctx:CMPLParser.ScopeContext):
        pass

    # Exit a parse tree produced by CMPLParser#scope.
    def exitScope(self, ctx:CMPLParser.ScopeContext):
        pass


    # Enter a parse tree produced by CMPLParser#varStatement.
    def enterVarStatement(self, ctx:CMPLParser.VarStatementContext):
        pass

    # Exit a parse tree produced by CMPLParser#varStatement.
    def exitVarStatement(self, ctx:CMPLParser.VarStatementContext):
        pass


    # Enter a parse tree produced by CMPLParser#funct_call.
    def enterFunct_call(self, ctx:CMPLParser.Funct_callContext):
        pass

    # Exit a parse tree produced by CMPLParser#funct_call.
    def exitFunct_call(self, ctx:CMPLParser.Funct_callContext):
        pass


    # Enter a parse tree produced by CMPLParser#showStatement.
    def enterShowStatement(self, ctx:CMPLParser.ShowStatementContext):
        pass

    # Exit a parse tree produced by CMPLParser#showStatement.
    def exitShowStatement(self, ctx:CMPLParser.ShowStatementContext):
        pass


    # Enter a parse tree produced by CMPLParser#varExpr.
    def enterVarExpr(self, ctx:CMPLParser.VarExprContext):
        pass

    # Exit a parse tree produced by CMPLParser#varExpr.
    def exitVarExpr(self, ctx:CMPLParser.VarExprContext):
        pass


    # Enter a parse tree produced by CMPLParser#infixExpr.
    def enterInfixExpr(self, ctx:CMPLParser.InfixExprContext):
        pass

    # Exit a parse tree produced by CMPLParser#infixExpr.
    def exitInfixExpr(self, ctx:CMPLParser.InfixExprContext):
        pass


    # Enter a parse tree produced by CMPLParser#negationExpr.
    def enterNegationExpr(self, ctx:CMPLParser.NegationExprContext):
        pass

    # Exit a parse tree produced by CMPLParser#negationExpr.
    def exitNegationExpr(self, ctx:CMPLParser.NegationExprContext):
        pass


    # Enter a parse tree produced by CMPLParser#typeExpr.
    def enterTypeExpr(self, ctx:CMPLParser.TypeExprContext):
        pass

    # Exit a parse tree produced by CMPLParser#typeExpr.
    def exitTypeExpr(self, ctx:CMPLParser.TypeExprContext):
        pass


    # Enter a parse tree produced by CMPLParser#functionCall.
    def enterFunctionCall(self, ctx:CMPLParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CMPLParser#functionCall.
    def exitFunctionCall(self, ctx:CMPLParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CMPLParser#logicExpr.
    def enterLogicExpr(self, ctx:CMPLParser.LogicExprContext):
        pass

    # Exit a parse tree produced by CMPLParser#logicExpr.
    def exitLogicExpr(self, ctx:CMPLParser.LogicExprContext):
        pass


    # Enter a parse tree produced by CMPLParser#parensExpr.
    def enterParensExpr(self, ctx:CMPLParser.ParensExprContext):
        pass

    # Exit a parse tree produced by CMPLParser#parensExpr.
    def exitParensExpr(self, ctx:CMPLParser.ParensExprContext):
        pass


    # Enter a parse tree produced by CMPLParser#compareExpr.
    def enterCompareExpr(self, ctx:CMPLParser.CompareExprContext):
        pass

    # Exit a parse tree produced by CMPLParser#compareExpr.
    def exitCompareExpr(self, ctx:CMPLParser.CompareExprContext):
        pass


    # Enter a parse tree produced by CMPLParser#data_type.
    def enterData_type(self, ctx:CMPLParser.Data_typeContext):
        pass

    # Exit a parse tree produced by CMPLParser#data_type.
    def exitData_type(self, ctx:CMPLParser.Data_typeContext):
        pass


    # Enter a parse tree produced by CMPLParser#comparison_op.
    def enterComparison_op(self, ctx:CMPLParser.Comparison_opContext):
        pass

    # Exit a parse tree produced by CMPLParser#comparison_op.
    def exitComparison_op(self, ctx:CMPLParser.Comparison_opContext):
        pass


    # Enter a parse tree produced by CMPLParser#logic_op.
    def enterLogic_op(self, ctx:CMPLParser.Logic_opContext):
        pass

    # Exit a parse tree produced by CMPLParser#logic_op.
    def exitLogic_op(self, ctx:CMPLParser.Logic_opContext):
        pass



del CMPLParser