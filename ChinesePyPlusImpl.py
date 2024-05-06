from ChinesePyPlus import ChinesePyPlusListener, ChinesePyPlusParser, ChinesePyPlusLexer
import antlr4 as antlr
from antlr4.tree import Tree as t

class ChinesePyPlusImpl(ChinesePyPlusListener.ChinesePyPlusListener):

    def __init__(self):
        self.code = ""
        self.indent_level = 0
        self.complement_for = False

    def addIndent(self):
        indent_string = ""
        for i in range(0, self.indent_level):
            indent_string += "\t"
        return indent_string

    def deleteIndent(self, i):
        self.code = self.code[:-i]

    def enterVar_type(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.Var_typeContext):
        pass

    def exitVar_type(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.Var_typeContext):
        pass

    def enterListValue(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ListValueContext):
        pass

    def exitListValue(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ListValueContext):
        pass

    def enterListExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ListExpressionContext):
        pass

    def exitListExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ListExpressionContext):
        pass

    def enterValue(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ValueContext):
        pass

    def exitValue(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ValueContext):
        pass

    def enterVarDeclaration(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.VarDeclarationContext):
        pass

    def exitVarDeclaration(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.VarDeclarationContext):
        pass

    def enterVarAssignment(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.VarAssignmentContext):
        pass

    def exitVarAssignment(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.VarAssignmentContext):
        pass

    def enterArithmeticExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ArithmeticExpressionContext):
        pass

    def exitArithmeticExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ArithmeticExpressionContext):
        pass

    def enterStringExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.StringExpressionContext):
        pass

    def exitStringExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.StringExpressionContext):
        pass

    def enterBooleanExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.BooleanExpressionContext):
        pass

    def exitBooleanExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.BooleanExpressionContext):
        pass

    def enterPrintExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.PrintExpressionContext):
        pass

    def exitPrintExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.PrintExpressionContext):
        pass

    def enterExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ExpressionContext):
        pass

    def exitExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ExpressionContext):
        pass

    def enterCode(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.CodeContext):
        pass

    def exitCode(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.CodeContext):
        pass

    def enterProgram(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ProgramContext):
        pass

    def exitProgram(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ProgramContext):
        pass

    def enterForLoopExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ForLoopExpressionContext):
        pass

    def exitForLoopExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ForLoopExpressionContext):
        pass

    def enterWhileLoopExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.WhileLoopExpressionContext):
        pass

    def exitWhileLoopExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.WhileLoopExpressionContext):
        pass

    def enterLoopCode(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.LoopCodeContext):
        pass

    def exitLoopCode(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.LoopCodeContext):
        pass

    def enterConditionalExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ConditionalExpressionContext):
        pass

    def exitConditionalExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ConditionalExpressionContext):
        pass

    def enterElifExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ElifExpressionContext):
        pass

    def exitElifExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ElifExpressionContext):
        pass

    def enterElseExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ElseExpressionContext):
        pass

    def exitElseExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ElseExpressionContext):
        pass

    def enterFunctionDeclaration(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FunctionDeclarationContext):
        pass

    def exitFunctionDeclaration(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FunctionDeclarationContext):
        pass

    def enterArgList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ArgListContext):
        pass

    def exitArgList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ArgListContext):
        pass

    def enterFullArgList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FullArgListContext):
        pass

    def exitFullArgList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FullArgListContext):
        pass

    def enterFunctionCall(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FunctionCallContext):
        pass

    def exitFunctionCall(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FunctionCallContext):
        pass

    def enterValueList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ValueListContext):
        pass

    def exitValueList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ValueListContext):
        pass

    def enterFullValueList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FullValueListContext):
        pass

    def exitFullValueList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FullValueListContext):
        pass

    def visitTerminal(self, node: t.TerminalNode):
        ttype = node.getSymbol().type
        parser = ChinesePyPlusParser.ChinesePyPlusParser

        immutable_values = [parser.TKN_VAR_ID, parser.TKN_NUMBER_VAL, parser.TKN_STRING_VAL, parser.TKN_LSQUARE,
                            parser.TKN_RSQUARE, parser.TKN_LBRACKET, parser.TKN_RBRACKET]
        immutable_ops = [parser.TKN_PLUS, parser.TKN_MINUS, parser.TKN_MUL, parser.TKN_DIV, parser.TKN_G, parser.TKN_L,
                         parser.TKN_GEQ, parser.TKN_LEQ]
        tokens = {
            parser.TKN_DOTS: ":\n",
            parser.TKN_END_LINE: "\n",
            parser.TKN_POW: " ** ",
            parser.TKN_CONCAT: " + ",
            parser.TKN_ASSIGN: " = ",
            parser.TKN_EQ: " == ",
            parser.TKN_NEQ: " != ",
            parser.TKN_COMMA: ", ",
            parser.TKN_NOT: " not ",
            parser.TKN_AND: " and ",
            parser.TKN_OR: " or ",
            parser.TKN_TRUE: "True",
            parser.TKN_FALSE: "False",
            parser.TKN_WHILE: "while ",
            parser.TKN_PRINT: "print",
            parser.TKN_FOR: "for ",
            parser.TKN_FROM: " in range(",
            parser.TKN_TO: ", ",
            parser.TKN_BREAK: "break",
            parser.TKN_CONTINUE: "continue",
            parser.TKN_RETURN: "return ",
            parser.TKN_FUNCTION: "def ",
            parser.TKN_IF: "if ",
            parser.TKN_ELIF: "elif ",
            parser.TKN_ELSE: "else"
        }

        if ttype in immutable_ops:
            self.code += " " + node.getText() + " "
        if ttype in immutable_values:
            self.code += node.getText()
        if ttype in tokens.keys():

            if ttype == parser.TKN_DOTS and self.complement_for:
                self.complement_for = False
                self.code += ")"
            if ttype == parser.TKN_ELIF or ttype == parser.TKN_ELSE:
                self.indent_level -= 1
                self.deleteIndent(1)

            self.code += tokens[ttype]

            if ttype == parser.TKN_FOR:
                self.complement_for = True
            if ttype == parser.TKN_DOTS:
                self.indent_level += 1
                self.code += self.addIndent()

            if ttype == parser.TKN_END_LINE:
                self.code += self.addIndent()
        if ttype == parser.TKN_END:
            self.indent_level -= 1
        if ttype == parser.TKN_COMMENT:
            self.code += node.getText() + "\n"
