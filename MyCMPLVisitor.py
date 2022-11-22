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
        if ctx.PLUS_PLUS():
            var = ctx.expr().getText()
            var = int(self.variables[var])
            var += 1
            print(var)
        else:
            in_show = str(ctx.expr().getText())
            try:
                print(int(in_show))
            except ValueError:
                pass
                if in_show in self.variables:
                    print(self.variables[in_show])
                else:
                    print(self.visit(ctx.expr()))

    def visitTypeExpr(self, ctx: CMPLParser.TypeExprContext):
        if int(ctx.getText()):
            self.stack.append(int(ctx.getText()))
            return int(ctx.getText())
        if float(ctx.getText()):
            return float(ctx.getText())
        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        if ctx.BOOLEAN():
            return ctx.BOOLEAN.getText() == "true"
        if ctx.NULL():
            return

    def visitVarExpr(self, ctx: CMPLParser.VarExprContext):
        var = str(ctx.VAR().getText())
        if var in self.variables:
            self.stack.append(int(self.variables[var]))
        else:
            raise Exception("Variable ", var, " not defined!")

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
