from CMPLParser import CMPLParser
from CMPLVisitor import CMPLVisitor


class MyCMPLVisitor(CMPLVisitor):
    def __init__(self):
        super(CMPLVisitor, self).__init__()
        self.stack = []  # Stack to evaluate the expression
        self.variables = {}  # Dictionary

    def visitVarStatement(self, ctx: CMPLParser.VarStatementContext):
        var = str(ctx.var.text)
        val = self.visit(ctx.exp)
        self.variables[var] = val

    def visitShowStatement(self, ctx: CMPLParser.ShowStatementContext):
        if ctx.expr():
            val = self.visit(ctx.expr())
            if val != 'null' or val is not None:
                if ctx.plus_plus_minus_minus():
                    if val != 'null':
                        val = self.visit(ctx.plus_plus_minus_minus())
                else:
                    if str(val) in self.variables:
                        val = self.variables[str(val)]
                print(val)
        else:
            print("show statement has nothing to show!")

    def visitTypeExpr(self, ctx: CMPLParser.TypeExprContext):
        try:
            return int(ctx.getText())
        except ValueError:
            pass
        try:
            return float(ctx.getText())
        except ValueError:
            pass
        try:
            if ctx.getText() == "true":
                return "true"
            elif ctx.getText() == "false":
                return "false"
            else:
                return str(ctx.getText()[1:-1])
        except ValueError:
            pass
        return 'null'

    def visitVarExpr(self, ctx: CMPLParser.VarExprContext):
        var = ctx.VAR().getText()
        if str(var) in self.variables:
            if ctx.plus_plus_minus_minus():
                currentValue = self.variables[str(var)]
                self.stack.append(currentValue)
                self.variables[str(var)] = self.visit(ctx.plus_plus_minus_minus())
            return self.variables[str(var)]
        else:
            return 'null'

    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx: CMPLParser.InfixExprContext):
        a = self.visit(ctx.left)
        b = self.visit(ctx.right)
        c = ''

        if a == 'null' or b == 'null':
            return "One of the variables is not defined!"

        if str(b) in self.variables:
            b = self.variables[str(b)]
        if str(a) in self.variables:
            a = self.variables[str(a)]

        if isinstance(a, str) or isinstance(b, str):
            if ctx.OP_ADD():
                return str(a) + str(b)
            else:
                return "invalid operation!"
        else:
            if ctx.OP_POW():
                c = a ** b
            elif ctx.OP_ADD():
                c = a + b
            elif ctx.OP_SUB():
                c = a - b
            elif ctx.OP_MUL():
                c = a * b
            elif ctx.OP_DIV():
                c = a / b

        return c

    def visitPlus_plus_minus_minus(self, ctx: CMPLParser.Plus_plus_minus_minusContext):
        if ctx.PLUS_PLUS():
            return self.stack.pop() + 1
        elif ctx.MINUS_MINUS():
            return self.stack.pop() - 1
        else:
            return "invalid operation!"

    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx: CMPLParser.ParensExprContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        return "null"

    def visitWhile_scope(self, ctx: CMPLParser.While_scopeContext):
        if ctx.WHILE():
            expr = self.visit(ctx.expr())
            if expr == 'null':
                print("Invalid operation!")
            else:
                while expr == "true":
                    self.visit(ctx.scope())
                    expr = self.visit(ctx.expr())

    def visitCompareExpr(self, ctx: CMPLParser.CompareExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        if left == 'null' or right == 'null':
            return "null"

        operation = ctx.op.getText()

        if operation == 'equals':
            if left == right:
                return 'true'
            else:
                return 'false'
        elif operation == 'not equals':
            if left != right:
                return 'true'
            else:
                return 'false'
        elif operation == 'greater':
            if left > right:
                return 'true'
            else:
                return 'false'
        elif operation == 'smaller':
            if left < right:
                return 'true'
            else:
                return 'false'
        elif operation == 'greater or equal':
            if left >= right:
                return 'true'
            else:
                return 'false'
        elif operation == 'smaller or equal':
            if left <= right:
                return 'true'
            else:
                return 'false'
        else:
            return "null"

    def visitLogicExpr(self, ctx: CMPLParser.LogicExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        logic_op = ctx.op.getText()
        if logic_op == "and":
            if left == "true" and right == "true":
                return "true"
            else:
                return "false"
        elif logic_op == "or":
            if left == "true" or right == "true":
                return "true"
            else:
                return "false"
        else:
            print("Invalid logical expression!")

    def visitIf_scope(self, ctx: CMPLParser.If_scopeContext):
        condition = self.visit(ctx.expr())
        if condition != 'null':
            if condition == 'true':
                self.visit(ctx.scope())
            else:
                self.visit(ctx.else_if_scope())
        else:
            return 'null'
