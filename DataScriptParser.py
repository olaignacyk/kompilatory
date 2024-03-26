# Generated from DataScript.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,5,3,45,8,3,10,3,12,3,48,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,0,90,0,19,1,0,0,0,2,32,
        1,0,0,0,4,34,1,0,0,0,6,40,1,0,0,0,8,51,1,0,0,0,10,59,1,0,0,0,12,
        67,1,0,0,0,14,75,1,0,0,0,16,81,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,
        0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,24,
        5,0,0,1,24,1,1,0,0,0,25,33,3,4,2,0,26,33,3,6,3,0,27,33,3,8,4,0,28,
        33,3,10,5,0,29,33,3,12,6,0,30,33,3,14,7,0,31,33,3,16,8,0,32,25,1,
        0,0,0,32,26,1,0,0,0,32,27,1,0,0,0,32,28,1,0,0,0,32,29,1,0,0,0,32,
        30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,0,34,35,5,1,0,0,35,36,5,2,0,
        0,36,37,5,12,0,0,37,38,5,3,0,0,38,39,5,4,0,0,39,5,1,0,0,0,40,41,
        5,5,0,0,41,46,5,12,0,0,42,43,5,6,0,0,43,45,5,12,0,0,44,42,1,0,0,
        0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,
        1,0,0,0,49,50,5,4,0,0,50,7,1,0,0,0,51,52,5,7,0,0,52,53,5,2,0,0,53,
        54,5,12,0,0,54,55,5,6,0,0,55,56,5,13,0,0,56,57,5,3,0,0,57,58,5,4,
        0,0,58,9,1,0,0,0,59,60,5,8,0,0,60,61,5,2,0,0,61,62,5,12,0,0,62,63,
        5,6,0,0,63,64,5,12,0,0,64,65,5,3,0,0,65,66,5,4,0,0,66,11,1,0,0,0,
        67,68,5,9,0,0,68,69,5,2,0,0,69,70,5,12,0,0,70,71,5,6,0,0,71,72,5,
        12,0,0,72,73,5,3,0,0,73,74,5,4,0,0,74,13,1,0,0,0,75,76,5,10,0,0,
        76,77,5,2,0,0,77,78,5,12,0,0,78,79,5,3,0,0,79,80,5,4,0,0,80,15,1,
        0,0,0,81,82,5,11,0,0,82,83,5,2,0,0,83,84,5,12,0,0,84,85,5,6,0,0,
        85,86,5,12,0,0,86,87,5,6,0,0,87,88,5,12,0,0,88,89,5,3,0,0,89,90,
        5,4,0,0,90,17,1,0,0,0,3,21,32,46
    ]

class DataScriptParser ( Parser ):

    grammarFileName = "DataScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'wczytaj_dane'", "'('", "')'", "';'", 
                     "'wyswietl'", "','", "'podzial_danych'", "'regresja_liniowa'", 
                     "'ocena_modelu'", "'srednia'", "'wykres_punktowy'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STRING", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_loadDataStatement = 2
    RULE_displayDataStatement = 3
    RULE_splitDataStatement = 4
    RULE_linearRegressionStatement = 5
    RULE_modelEvaluationStatement = 6
    RULE_meanStatement = 7
    RULE_pointPlotStatement = 8

    ruleNames =  [ "program", "statement", "loadDataStatement", "displayDataStatement", 
                   "splitDataStatement", "linearRegressionStatement", "modelEvaluationStatement", 
                   "meanStatement", "pointPlotStatement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    STRING=12
    NUMBER=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DataScriptParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(DataScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return DataScriptParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = DataScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4002) != 0)):
                    break

            self.state = 23
            self.match(DataScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadDataStatement(self):
            return self.getTypedRuleContext(DataScriptParser.LoadDataStatementContext,0)


        def displayDataStatement(self):
            return self.getTypedRuleContext(DataScriptParser.DisplayDataStatementContext,0)


        def splitDataStatement(self):
            return self.getTypedRuleContext(DataScriptParser.SplitDataStatementContext,0)


        def linearRegressionStatement(self):
            return self.getTypedRuleContext(DataScriptParser.LinearRegressionStatementContext,0)


        def modelEvaluationStatement(self):
            return self.getTypedRuleContext(DataScriptParser.ModelEvaluationStatementContext,0)


        def meanStatement(self):
            return self.getTypedRuleContext(DataScriptParser.MeanStatementContext,0)


        def pointPlotStatement(self):
            return self.getTypedRuleContext(DataScriptParser.PointPlotStatementContext,0)


        def getRuleIndex(self):
            return DataScriptParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = DataScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.loadDataStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.displayDataStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.splitDataStatement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.linearRegressionStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                self.modelEvaluationStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 30
                self.meanStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 7)
                self.state = 31
                self.pointPlotStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadDataStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DataScriptParser.STRING, 0)

        def getRuleIndex(self):
            return DataScriptParser.RULE_loadDataStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadDataStatement" ):
                listener.enterLoadDataStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadDataStatement" ):
                listener.exitLoadDataStatement(self)




    def loadDataStatement(self):

        localctx = DataScriptParser.LoadDataStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(DataScriptParser.T__0)
            self.state = 35
            self.match(DataScriptParser.T__1)
            self.state = 36
            self.match(DataScriptParser.STRING)
            self.state = 37
            self.match(DataScriptParser.T__2)
            self.state = 38
            self.match(DataScriptParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisplayDataStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(DataScriptParser.STRING)
            else:
                return self.getToken(DataScriptParser.STRING, i)

        def getRuleIndex(self):
            return DataScriptParser.RULE_displayDataStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplayDataStatement" ):
                listener.enterDisplayDataStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplayDataStatement" ):
                listener.exitDisplayDataStatement(self)




    def displayDataStatement(self):

        localctx = DataScriptParser.DisplayDataStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_displayDataStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(DataScriptParser.T__4)
            self.state = 41
            self.match(DataScriptParser.STRING)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 42
                self.match(DataScriptParser.T__5)
                self.state = 43
                self.match(DataScriptParser.STRING)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(DataScriptParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SplitDataStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DataScriptParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(DataScriptParser.NUMBER, 0)

        def getRuleIndex(self):
            return DataScriptParser.RULE_splitDataStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSplitDataStatement" ):
                listener.enterSplitDataStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSplitDataStatement" ):
                listener.exitSplitDataStatement(self)




    def splitDataStatement(self):

        localctx = DataScriptParser.SplitDataStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_splitDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(DataScriptParser.T__6)
            self.state = 52
            self.match(DataScriptParser.T__1)
            self.state = 53
            self.match(DataScriptParser.STRING)
            self.state = 54
            self.match(DataScriptParser.T__5)
            self.state = 55
            self.match(DataScriptParser.NUMBER)
            self.state = 56
            self.match(DataScriptParser.T__2)
            self.state = 57
            self.match(DataScriptParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinearRegressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(DataScriptParser.STRING)
            else:
                return self.getToken(DataScriptParser.STRING, i)

        def getRuleIndex(self):
            return DataScriptParser.RULE_linearRegressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinearRegressionStatement" ):
                listener.enterLinearRegressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinearRegressionStatement" ):
                listener.exitLinearRegressionStatement(self)




    def linearRegressionStatement(self):

        localctx = DataScriptParser.LinearRegressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_linearRegressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(DataScriptParser.T__7)
            self.state = 60
            self.match(DataScriptParser.T__1)
            self.state = 61
            self.match(DataScriptParser.STRING)
            self.state = 62
            self.match(DataScriptParser.T__5)
            self.state = 63
            self.match(DataScriptParser.STRING)
            self.state = 64
            self.match(DataScriptParser.T__2)
            self.state = 65
            self.match(DataScriptParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelEvaluationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(DataScriptParser.STRING)
            else:
                return self.getToken(DataScriptParser.STRING, i)

        def getRuleIndex(self):
            return DataScriptParser.RULE_modelEvaluationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelEvaluationStatement" ):
                listener.enterModelEvaluationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelEvaluationStatement" ):
                listener.exitModelEvaluationStatement(self)




    def modelEvaluationStatement(self):

        localctx = DataScriptParser.ModelEvaluationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_modelEvaluationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(DataScriptParser.T__8)
            self.state = 68
            self.match(DataScriptParser.T__1)
            self.state = 69
            self.match(DataScriptParser.STRING)
            self.state = 70
            self.match(DataScriptParser.T__5)
            self.state = 71
            self.match(DataScriptParser.STRING)
            self.state = 72
            self.match(DataScriptParser.T__2)
            self.state = 73
            self.match(DataScriptParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MeanStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DataScriptParser.STRING, 0)

        def getRuleIndex(self):
            return DataScriptParser.RULE_meanStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeanStatement" ):
                listener.enterMeanStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeanStatement" ):
                listener.exitMeanStatement(self)




    def meanStatement(self):

        localctx = DataScriptParser.MeanStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_meanStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(DataScriptParser.T__9)
            self.state = 76
            self.match(DataScriptParser.T__1)
            self.state = 77
            self.match(DataScriptParser.STRING)
            self.state = 78
            self.match(DataScriptParser.T__2)
            self.state = 79
            self.match(DataScriptParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointPlotStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(DataScriptParser.STRING)
            else:
                return self.getToken(DataScriptParser.STRING, i)

        def getRuleIndex(self):
            return DataScriptParser.RULE_pointPlotStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointPlotStatement" ):
                listener.enterPointPlotStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointPlotStatement" ):
                listener.exitPointPlotStatement(self)




    def pointPlotStatement(self):

        localctx = DataScriptParser.PointPlotStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pointPlotStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(DataScriptParser.T__10)
            self.state = 82
            self.match(DataScriptParser.T__1)
            self.state = 83
            self.match(DataScriptParser.STRING)
            self.state = 84
            self.match(DataScriptParser.T__5)
            self.state = 85
            self.match(DataScriptParser.STRING)
            self.state = 86
            self.match(DataScriptParser.T__5)
            self.state = 87
            self.match(DataScriptParser.STRING)
            self.state = 88
            self.match(DataScriptParser.T__2)
            self.state = 89
            self.match(DataScriptParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





