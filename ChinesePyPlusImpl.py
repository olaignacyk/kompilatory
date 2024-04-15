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
        # Exit a parse tree produced by ChinesePyPlusParser#var_type.


    def exitVar_type(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.Var_typeContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#value.

    def enterListValue(self, ctx:ChinesePyPlusParser.ChinesePyPlusParser.ListValueContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#listValue.
    def exitListValue(self, ctx:ChinesePyPlusParser.ChinesePyPlusParser.ListValueContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#listExpression.
    def enterListExpression(self, ctx:ChinesePyPlusParser.ChinesePyPlusParser.ListExpressionContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#listExpression.
    def exitListExpression(self, ctx:ChinesePyPlusParser.ChinesePyPlusParser.ListExpressionContext):
        pass

    def enterValue(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ValueContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#value.


    def exitValue(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ValueContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#varDeclaration.

    def enterVarDeclaration(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.VarDeclarationContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#varDeclaration.


    def exitVarDeclaration(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.VarDeclarationContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#varAssignment.


    def enterVarAssignment(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.VarAssignmentContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#varAssignment.


    def exitVarAssignment(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.VarAssignmentContext):
        pass

    def enterArithmeticExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ArithmeticExpressionContext):
        pass

        # Exit a parse tree produced by ChinesePyPlusParser#arithmeticExpression.

    def exitArithmeticExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ArithmeticExpressionContext):
        pass

        # Enter a parse tree produced by ChinesePyPlusParser#stringExpression.

    def enterStringExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.StringExpressionContext):
        pass

        # Exit a parse tree produced by ChinesePyPlusParser#stringExpression.

    def exitStringExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.StringExpressionContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#booleanExpression.

    def enterBooleanExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.BooleanExpressionContext):
        pass

        # Exit a parse tree produced by ChinesePyPlusParser#booleanExpression.

    def exitBooleanExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.BooleanExpressionContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#printExpression.

    def enterPrintExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.PrintExpressionContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#printExpression.

    def exitPrintExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.PrintExpressionContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#expression.

    def enterExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ExpressionContext):
        pass

        # Exit a parse tree produced by ChinesePyPlusParser#expression.
    def exitExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ExpressionContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#code.

    def enterCode(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.CodeContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#code.

    def exitCode(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.CodeContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#program.

    def enterProgram(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ProgramContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#program.

    def exitProgram(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ProgramContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#forLoopExpression.

    def enterForLoopExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ForLoopExpressionContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#forLoopExpression.

    def exitForLoopExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ForLoopExpressionContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#whileLoopExpression.

    def enterWhileLoopExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.WhileLoopExpressionContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#whileLoopExpression.

    def exitWhileLoopExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.WhileLoopExpressionContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#loopCode.

    def enterLoopCode(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.LoopCodeContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#loopCode.

    def exitLoopCode(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.LoopCodeContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#conditionalExpression.

    def enterConditionalExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ConditionalExpressionContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#conditionalExpression.

    def exitConditionalExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ConditionalExpressionContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#elifExpression.

    def enterElifExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ElifExpressionContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#elifExpression.

    def exitElifExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ElifExpressionContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#elseExpression.

    def enterElseExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ElseExpressionContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#elseExpression.

    def exitElseExpression(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ElseExpressionContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#functionDeclaration.

    def enterFunctionDeclaration(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FunctionDeclarationContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#functionDeclaration.

    def exitFunctionDeclaration(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FunctionDeclarationContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#argList.

    def enterArgList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ArgListContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#argList.

    def exitArgList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ArgListContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#fullArgList.

    def enterFullArgList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FullArgListContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#fullArgList.

    def exitFullArgList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FullArgListContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#functionCall.

    def enterFunctionCall(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FunctionCallContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#functionCall.

    def exitFunctionCall(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FunctionCallContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#valueList.

    def enterValueList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ValueListContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#valueList.

    def exitValueList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.ValueListContext):
        pass
        # Enter a parse tree produced by ChinesePyPlusParser#fullValueList.

    def enterFullValueList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FullValueListContext):
        pass
        # Exit a parse tree produced by ChinesePyPlusParser#fullValueList.

    def exitFullValueList(self, ctx: ChinesePyPlusParser.ChinesePyPlusParser.FullValueListContext):
        pass

    def visitTerminal(self, node:t.TerminalNode):

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
            parser.TKN_FROM: " in range (",
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




