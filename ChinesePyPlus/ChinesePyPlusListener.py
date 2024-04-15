# Generated from ChinesePyPlus.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ChinesePyPlusParser import ChinesePyPlusParser
else:
    from ChinesePyPlusParser import ChinesePyPlusParser

# This class defines a complete listener for a parse tree produced by ChinesePyPlusParser.
class ChinesePyPlusListener(ParseTreeListener):

    # Enter a parse tree produced by ChinesePyPlusParser#program.
    def enterProgram(self, ctx:ChinesePyPlusParser.ProgramContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#program.
    def exitProgram(self, ctx:ChinesePyPlusParser.ProgramContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#code.
    def enterCode(self, ctx:ChinesePyPlusParser.CodeContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#code.
    def exitCode(self, ctx:ChinesePyPlusParser.CodeContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#var_type.
    def enterVar_type(self, ctx:ChinesePyPlusParser.Var_typeContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#var_type.
    def exitVar_type(self, ctx:ChinesePyPlusParser.Var_typeContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#varDeclaration.
    def enterVarDeclaration(self, ctx:ChinesePyPlusParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#varDeclaration.
    def exitVarDeclaration(self, ctx:ChinesePyPlusParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#varAssignment.
    def enterVarAssignment(self, ctx:ChinesePyPlusParser.VarAssignmentContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#varAssignment.
    def exitVarAssignment(self, ctx:ChinesePyPlusParser.VarAssignmentContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:ChinesePyPlusParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:ChinesePyPlusParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#functionCall.
    def enterFunctionCall(self, ctx:ChinesePyPlusParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#functionCall.
    def exitFunctionCall(self, ctx:ChinesePyPlusParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#expression.
    def enterExpression(self, ctx:ChinesePyPlusParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#expression.
    def exitExpression(self, ctx:ChinesePyPlusParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#value.
    def enterValue(self, ctx:ChinesePyPlusParser.ValueContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#value.
    def exitValue(self, ctx:ChinesePyPlusParser.ValueContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#stringExpression.
    def enterStringExpression(self, ctx:ChinesePyPlusParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#stringExpression.
    def exitStringExpression(self, ctx:ChinesePyPlusParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#booleanExpression.
    def enterBooleanExpression(self, ctx:ChinesePyPlusParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#booleanExpression.
    def exitBooleanExpression(self, ctx:ChinesePyPlusParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:ChinesePyPlusParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:ChinesePyPlusParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#printExpression.
    def enterPrintExpression(self, ctx:ChinesePyPlusParser.PrintExpressionContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#printExpression.
    def exitPrintExpression(self, ctx:ChinesePyPlusParser.PrintExpressionContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#forLoopExpression.
    def enterForLoopExpression(self, ctx:ChinesePyPlusParser.ForLoopExpressionContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#forLoopExpression.
    def exitForLoopExpression(self, ctx:ChinesePyPlusParser.ForLoopExpressionContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#whileLoopExpression.
    def enterWhileLoopExpression(self, ctx:ChinesePyPlusParser.WhileLoopExpressionContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#whileLoopExpression.
    def exitWhileLoopExpression(self, ctx:ChinesePyPlusParser.WhileLoopExpressionContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:ChinesePyPlusParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:ChinesePyPlusParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#elifExpression.
    def enterElifExpression(self, ctx:ChinesePyPlusParser.ElifExpressionContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#elifExpression.
    def exitElifExpression(self, ctx:ChinesePyPlusParser.ElifExpressionContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#elseExpression.
    def enterElseExpression(self, ctx:ChinesePyPlusParser.ElseExpressionContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#elseExpression.
    def exitElseExpression(self, ctx:ChinesePyPlusParser.ElseExpressionContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#listExpression.
    def enterListExpression(self, ctx:ChinesePyPlusParser.ListExpressionContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#listExpression.
    def exitListExpression(self, ctx:ChinesePyPlusParser.ListExpressionContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#listValue.
    def enterListValue(self, ctx:ChinesePyPlusParser.ListValueContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#listValue.
    def exitListValue(self, ctx:ChinesePyPlusParser.ListValueContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#valueList.
    def enterValueList(self, ctx:ChinesePyPlusParser.ValueListContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#valueList.
    def exitValueList(self, ctx:ChinesePyPlusParser.ValueListContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#fullValueList.
    def enterFullValueList(self, ctx:ChinesePyPlusParser.FullValueListContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#fullValueList.
    def exitFullValueList(self, ctx:ChinesePyPlusParser.FullValueListContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#argList.
    def enterArgList(self, ctx:ChinesePyPlusParser.ArgListContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#argList.
    def exitArgList(self, ctx:ChinesePyPlusParser.ArgListContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#fullArgList.
    def enterFullArgList(self, ctx:ChinesePyPlusParser.FullArgListContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#fullArgList.
    def exitFullArgList(self, ctx:ChinesePyPlusParser.FullArgListContext):
        pass


    # Enter a parse tree produced by ChinesePyPlusParser#loopCode.
    def enterLoopCode(self, ctx:ChinesePyPlusParser.LoopCodeContext):
        pass

    # Exit a parse tree produced by ChinesePyPlusParser#loopCode.
    def exitLoopCode(self, ctx:ChinesePyPlusParser.LoopCodeContext):
        pass



del ChinesePyPlusParser