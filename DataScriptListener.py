# Generated from DataScript.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DataScriptParser import DataScriptParser
else:
    from DataScriptParser import DataScriptParser

# This class defines a complete listener for a parse tree produced by DataScriptParser.
class DataScriptListener(ParseTreeListener):

    # Enter a parse tree produced by DataScriptParser#program.
    def enterProgram(self, ctx:DataScriptParser.ProgramContext):
        pass

    # Exit a parse tree produced by DataScriptParser#program.
    def exitProgram(self, ctx:DataScriptParser.ProgramContext):
        pass


    # Enter a parse tree produced by DataScriptParser#statement.
    def enterStatement(self, ctx:DataScriptParser.StatementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#statement.
    def exitStatement(self, ctx:DataScriptParser.StatementContext):
        pass


    # Enter a parse tree produced by DataScriptParser#loadDataStatement.
    def enterLoadDataStatement(self, ctx:DataScriptParser.LoadDataStatementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#loadDataStatement.
    def exitLoadDataStatement(self, ctx:DataScriptParser.LoadDataStatementContext):
        pass


    # Enter a parse tree produced by DataScriptParser#displayDataStatement.
    def enterDisplayDataStatement(self, ctx:DataScriptParser.DisplayDataStatementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#displayDataStatement.
    def exitDisplayDataStatement(self, ctx:DataScriptParser.DisplayDataStatementContext):
        pass


    # Enter a parse tree produced by DataScriptParser#splitDataStatement.
    def enterSplitDataStatement(self, ctx:DataScriptParser.SplitDataStatementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#splitDataStatement.
    def exitSplitDataStatement(self, ctx:DataScriptParser.SplitDataStatementContext):
        pass


    # Enter a parse tree produced by DataScriptParser#linearRegressionStatement.
    def enterLinearRegressionStatement(self, ctx:DataScriptParser.LinearRegressionStatementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#linearRegressionStatement.
    def exitLinearRegressionStatement(self, ctx:DataScriptParser.LinearRegressionStatementContext):
        pass


    # Enter a parse tree produced by DataScriptParser#modelEvaluationStatement.
    def enterModelEvaluationStatement(self, ctx:DataScriptParser.ModelEvaluationStatementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#modelEvaluationStatement.
    def exitModelEvaluationStatement(self, ctx:DataScriptParser.ModelEvaluationStatementContext):
        pass


    # Enter a parse tree produced by DataScriptParser#meanStatement.
    def enterMeanStatement(self, ctx:DataScriptParser.MeanStatementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#meanStatement.
    def exitMeanStatement(self, ctx:DataScriptParser.MeanStatementContext):
        pass


    # Enter a parse tree produced by DataScriptParser#pointPlotStatement.
    def enterPointPlotStatement(self, ctx:DataScriptParser.PointPlotStatementContext):
        pass

    # Exit a parse tree produced by DataScriptParser#pointPlotStatement.
    def exitPointPlotStatement(self, ctx:DataScriptParser.PointPlotStatementContext):
        pass



del DataScriptParser