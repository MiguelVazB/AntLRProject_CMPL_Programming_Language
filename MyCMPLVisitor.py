from CMPLParser import CMPLParser
from CMPLVisitor import CMPLVisitor


class MyCMPLVisitor(CMPLVisitor):
    def __init__(self):
        super(CMPLVisitor, self).__init__()
        self.stack = []  # Stack to evaluate the expression
        self.variables = {}  # Dictionary

    def visitVarStatement(self, ctx: CMPLParser.VarStatementContext):
        var = str(ctx.var.text)
        val = str(ctx.exp.getText())
        self.variables[var] = val

    def visitShowStatement(self, ctx: CMPLParser.ShowStatementContext):
        if ctx.expr():
            val = self.visit(ctx.expr())
            if ctx.PLUS_PLUS():
                try:
                    if int(val):
                        val = int(val)
                        val += 1
                except ValueError:
                    val = val+val
            else:
                if str(val) in self.variables:
                    val = self.variables[str(val)]
                    print(val)
            print(val)
        else:
            print("show statement has nothing to show!")

    def visitTypeExpr(self, ctx: CMPLParser.TypeExprContext):
        try:
            if int(ctx.getText()):
                self.stack.append(int(ctx.getText()))
                return int(ctx.getText())
        except ValueError:
            pass
        try:
            if float(ctx.getText()):
                self.stack.append(float(ctx.getText()))
                return float(ctx.getText())
        except ValueError:
            pass
        try:
            if str(ctx.getText()):
                self.stack.append(str(ctx.getText()[1:-1]))
                return str(ctx.getText()[1:-1])
        except ValueError:
            pass
        try:
            if bool(ctx.getText()):
                return ctx.BOOLEAN.getText() == "true"
        except ValueError:
            pass
        return 'null'

    def visitVarExpr(self, ctx: CMPLParser.VarExprContext):
        var = ctx.VAR().getText()
        if var in self.variables:
            return self.variables[var]
        else:
            print('Variable ', str(var), ' not defined!')

    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx: CMPLParser.InfixExprContext):
        self.visit(ctx.left)  # Evaluate the left  expression and push to stack
        self.visit(ctx.right)  # Evaluate the right expression and push to stack

        b = self.stack.pop()  # Why is ‘b’ the first popped item?
        a = self.stack.pop()
        c = None

        if str(b) in self.variables:
            b = self.variables[str(b)]
        if str(a) in self.variables:
            a = self.variables[str(a)]

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

        self.stack.append(c)
        return c

    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx: CMPLParser.ParensExprContext):
        return self.visit(ctx.expr())  # Since enclosed by parents, just visit expr
