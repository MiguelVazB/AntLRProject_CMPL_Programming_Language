# Generated from CMPL.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CMPLParser import CMPLParser
else:
    from CMPLParser import CMPLParser

# This class defines a complete generic visitor for a parse tree produced by CMPLParser.

class CMPLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CMPLParser#prog.
    def visitProg(self, ctx:CMPLParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#stmts.
    def visitStmts(self, ctx:CMPLParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#stmt.
    def visitStmt(self, ctx:CMPLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#if_scope.
    def visitIf_scope(self, ctx:CMPLParser.If_scopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#else_if_scope.
    def visitElse_if_scope(self, ctx:CMPLParser.Else_if_scopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#while_scope.
    def visitWhile_scope(self, ctx:CMPLParser.While_scopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#scope.
    def visitScope(self, ctx:CMPLParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#varStatement.
    def visitVarStatement(self, ctx:CMPLParser.VarStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#funct_call.
    def visitFunct_call(self, ctx:CMPLParser.Funct_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#showStatement.
    def visitShowStatement(self, ctx:CMPLParser.ShowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#varExpr.
    def visitVarExpr(self, ctx:CMPLParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#infixExpr.
    def visitInfixExpr(self, ctx:CMPLParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#negationExpr.
    def visitNegationExpr(self, ctx:CMPLParser.NegationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#typeExpr.
    def visitTypeExpr(self, ctx:CMPLParser.TypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#functionCall.
    def visitFunctionCall(self, ctx:CMPLParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#logicExpr.
    def visitLogicExpr(self, ctx:CMPLParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#parensExpr.
    def visitParensExpr(self, ctx:CMPLParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#compareExpr.
    def visitCompareExpr(self, ctx:CMPLParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#data_type.
    def visitData_type(self, ctx:CMPLParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#comparison_op.
    def visitComparison_op(self, ctx:CMPLParser.Comparison_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMPLParser#logic_op.
    def visitLogic_op(self, ctx:CMPLParser.Logic_opContext):
        return self.visitChildren(ctx)



del CMPLParser