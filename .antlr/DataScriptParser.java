// Generated from /Users/aleksandraignacyk/Studia/semestr3/Kompilatory/DataScript/kompilatory/DataScript.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class DataScriptParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, STRING=12, NUMBER=13, WS=14;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_loadDataStatement = 2, RULE_displayDataStatement = 3, 
		RULE_splitDataStatement = 4, RULE_linearRegressionStatement = 5, RULE_modelEvaluationStatement = 6, 
		RULE_meanStatement = 7, RULE_pointPlotStatement = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "loadDataStatement", "displayDataStatement", 
			"splitDataStatement", "linearRegressionStatement", "modelEvaluationStatement", 
			"meanStatement", "pointPlotStatement"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'wczytaj_dane'", "'('", "')'", "';'", "'wyswietl'", "','", "'podzial_danych'", 
			"'regresja_liniowa'", "'ocena_modelu'", "'srednia'", "'wykres_punktowy'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"STRING", "NUMBER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "DataScript.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DataScriptParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(DataScriptParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(18);
				statement();
				}
				}
				setState(21); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 4002L) != 0) );
			setState(23);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public LoadDataStatementContext loadDataStatement() {
			return getRuleContext(LoadDataStatementContext.class,0);
		}
		public DisplayDataStatementContext displayDataStatement() {
			return getRuleContext(DisplayDataStatementContext.class,0);
		}
		public SplitDataStatementContext splitDataStatement() {
			return getRuleContext(SplitDataStatementContext.class,0);
		}
		public LinearRegressionStatementContext linearRegressionStatement() {
			return getRuleContext(LinearRegressionStatementContext.class,0);
		}
		public ModelEvaluationStatementContext modelEvaluationStatement() {
			return getRuleContext(ModelEvaluationStatementContext.class,0);
		}
		public MeanStatementContext meanStatement() {
			return getRuleContext(MeanStatementContext.class,0);
		}
		public PointPlotStatementContext pointPlotStatement() {
			return getRuleContext(PointPlotStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(32);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(25);
				loadDataStatement();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(26);
				displayDataStatement();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 3);
				{
				setState(27);
				splitDataStatement();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 4);
				{
				setState(28);
				linearRegressionStatement();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 5);
				{
				setState(29);
				modelEvaluationStatement();
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 6);
				{
				setState(30);
				meanStatement();
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 7);
				{
				setState(31);
				pointPlotStatement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LoadDataStatementContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(DataScriptParser.STRING, 0); }
		public LoadDataStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loadDataStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).enterLoadDataStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).exitLoadDataStatement(this);
		}
	}

	public final LoadDataStatementContext loadDataStatement() throws RecognitionException {
		LoadDataStatementContext _localctx = new LoadDataStatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_loadDataStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			match(T__0);
			setState(35);
			match(T__1);
			setState(36);
			match(STRING);
			setState(37);
			match(T__2);
			setState(38);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DisplayDataStatementContext extends ParserRuleContext {
		public List<TerminalNode> STRING() { return getTokens(DataScriptParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(DataScriptParser.STRING, i);
		}
		public DisplayDataStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_displayDataStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).enterDisplayDataStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).exitDisplayDataStatement(this);
		}
	}

	public final DisplayDataStatementContext displayDataStatement() throws RecognitionException {
		DisplayDataStatementContext _localctx = new DisplayDataStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_displayDataStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			match(T__4);
			setState(41);
			match(STRING);
			setState(46);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(42);
				match(T__5);
				setState(43);
				match(STRING);
				}
				}
				setState(48);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(49);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SplitDataStatementContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(DataScriptParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(DataScriptParser.NUMBER, 0); }
		public SplitDataStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_splitDataStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).enterSplitDataStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).exitSplitDataStatement(this);
		}
	}

	public final SplitDataStatementContext splitDataStatement() throws RecognitionException {
		SplitDataStatementContext _localctx = new SplitDataStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_splitDataStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(T__6);
			setState(52);
			match(T__1);
			setState(53);
			match(STRING);
			setState(54);
			match(T__5);
			setState(55);
			match(NUMBER);
			setState(56);
			match(T__2);
			setState(57);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LinearRegressionStatementContext extends ParserRuleContext {
		public List<TerminalNode> STRING() { return getTokens(DataScriptParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(DataScriptParser.STRING, i);
		}
		public LinearRegressionStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_linearRegressionStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).enterLinearRegressionStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).exitLinearRegressionStatement(this);
		}
	}

	public final LinearRegressionStatementContext linearRegressionStatement() throws RecognitionException {
		LinearRegressionStatementContext _localctx = new LinearRegressionStatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_linearRegressionStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(T__7);
			setState(60);
			match(T__1);
			setState(61);
			match(STRING);
			setState(62);
			match(T__5);
			setState(63);
			match(STRING);
			setState(64);
			match(T__2);
			setState(65);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ModelEvaluationStatementContext extends ParserRuleContext {
		public List<TerminalNode> STRING() { return getTokens(DataScriptParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(DataScriptParser.STRING, i);
		}
		public ModelEvaluationStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modelEvaluationStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).enterModelEvaluationStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).exitModelEvaluationStatement(this);
		}
	}

	public final ModelEvaluationStatementContext modelEvaluationStatement() throws RecognitionException {
		ModelEvaluationStatementContext _localctx = new ModelEvaluationStatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_modelEvaluationStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(T__8);
			setState(68);
			match(T__1);
			setState(69);
			match(STRING);
			setState(70);
			match(T__5);
			setState(71);
			match(STRING);
			setState(72);
			match(T__2);
			setState(73);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MeanStatementContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(DataScriptParser.STRING, 0); }
		public MeanStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_meanStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).enterMeanStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).exitMeanStatement(this);
		}
	}

	public final MeanStatementContext meanStatement() throws RecognitionException {
		MeanStatementContext _localctx = new MeanStatementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_meanStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(T__9);
			setState(76);
			match(T__1);
			setState(77);
			match(STRING);
			setState(78);
			match(T__2);
			setState(79);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PointPlotStatementContext extends ParserRuleContext {
		public List<TerminalNode> STRING() { return getTokens(DataScriptParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(DataScriptParser.STRING, i);
		}
		public PointPlotStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pointPlotStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).enterPointPlotStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DataScriptListener ) ((DataScriptListener)listener).exitPointPlotStatement(this);
		}
	}

	public final PointPlotStatementContext pointPlotStatement() throws RecognitionException {
		PointPlotStatementContext _localctx = new PointPlotStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_pointPlotStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(T__10);
			setState(82);
			match(T__1);
			setState(83);
			match(STRING);
			setState(84);
			match(T__5);
			setState(85);
			match(STRING);
			setState(86);
			match(T__5);
			setState(87);
			match(STRING);
			setState(88);
			match(T__2);
			setState(89);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u000e\\\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0001\u0000\u0004\u0000\u0014\b\u0000\u000b\u0000\f\u0000\u0015"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001!\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003-\b\u0003\n\u0003\f\u0003"+
		"0\t\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0000\u0000\t\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0010\u0000\u0000Z\u0000\u0013\u0001\u0000"+
		"\u0000\u0000\u0002 \u0001\u0000\u0000\u0000\u0004\"\u0001\u0000\u0000"+
		"\u0000\u0006(\u0001\u0000\u0000\u0000\b3\u0001\u0000\u0000\u0000\n;\u0001"+
		"\u0000\u0000\u0000\fC\u0001\u0000\u0000\u0000\u000eK\u0001\u0000\u0000"+
		"\u0000\u0010Q\u0001\u0000\u0000\u0000\u0012\u0014\u0003\u0002\u0001\u0000"+
		"\u0013\u0012\u0001\u0000\u0000\u0000\u0014\u0015\u0001\u0000\u0000\u0000"+
		"\u0015\u0013\u0001\u0000\u0000\u0000\u0015\u0016\u0001\u0000\u0000\u0000"+
		"\u0016\u0017\u0001\u0000\u0000\u0000\u0017\u0018\u0005\u0000\u0000\u0001"+
		"\u0018\u0001\u0001\u0000\u0000\u0000\u0019!\u0003\u0004\u0002\u0000\u001a"+
		"!\u0003\u0006\u0003\u0000\u001b!\u0003\b\u0004\u0000\u001c!\u0003\n\u0005"+
		"\u0000\u001d!\u0003\f\u0006\u0000\u001e!\u0003\u000e\u0007\u0000\u001f"+
		"!\u0003\u0010\b\u0000 \u0019\u0001\u0000\u0000\u0000 \u001a\u0001\u0000"+
		"\u0000\u0000 \u001b\u0001\u0000\u0000\u0000 \u001c\u0001\u0000\u0000\u0000"+
		" \u001d\u0001\u0000\u0000\u0000 \u001e\u0001\u0000\u0000\u0000 \u001f"+
		"\u0001\u0000\u0000\u0000!\u0003\u0001\u0000\u0000\u0000\"#\u0005\u0001"+
		"\u0000\u0000#$\u0005\u0002\u0000\u0000$%\u0005\f\u0000\u0000%&\u0005\u0003"+
		"\u0000\u0000&\'\u0005\u0004\u0000\u0000\'\u0005\u0001\u0000\u0000\u0000"+
		"()\u0005\u0005\u0000\u0000).\u0005\f\u0000\u0000*+\u0005\u0006\u0000\u0000"+
		"+-\u0005\f\u0000\u0000,*\u0001\u0000\u0000\u0000-0\u0001\u0000\u0000\u0000"+
		".,\u0001\u0000\u0000\u0000./\u0001\u0000\u0000\u0000/1\u0001\u0000\u0000"+
		"\u00000.\u0001\u0000\u0000\u000012\u0005\u0004\u0000\u00002\u0007\u0001"+
		"\u0000\u0000\u000034\u0005\u0007\u0000\u000045\u0005\u0002\u0000\u0000"+
		"56\u0005\f\u0000\u000067\u0005\u0006\u0000\u000078\u0005\r\u0000\u0000"+
		"89\u0005\u0003\u0000\u00009:\u0005\u0004\u0000\u0000:\t\u0001\u0000\u0000"+
		"\u0000;<\u0005\b\u0000\u0000<=\u0005\u0002\u0000\u0000=>\u0005\f\u0000"+
		"\u0000>?\u0005\u0006\u0000\u0000?@\u0005\f\u0000\u0000@A\u0005\u0003\u0000"+
		"\u0000AB\u0005\u0004\u0000\u0000B\u000b\u0001\u0000\u0000\u0000CD\u0005"+
		"\t\u0000\u0000DE\u0005\u0002\u0000\u0000EF\u0005\f\u0000\u0000FG\u0005"+
		"\u0006\u0000\u0000GH\u0005\f\u0000\u0000HI\u0005\u0003\u0000\u0000IJ\u0005"+
		"\u0004\u0000\u0000J\r\u0001\u0000\u0000\u0000KL\u0005\n\u0000\u0000LM"+
		"\u0005\u0002\u0000\u0000MN\u0005\f\u0000\u0000NO\u0005\u0003\u0000\u0000"+
		"OP\u0005\u0004\u0000\u0000P\u000f\u0001\u0000\u0000\u0000QR\u0005\u000b"+
		"\u0000\u0000RS\u0005\u0002\u0000\u0000ST\u0005\f\u0000\u0000TU\u0005\u0006"+
		"\u0000\u0000UV\u0005\f\u0000\u0000VW\u0005\u0006\u0000\u0000WX\u0005\f"+
		"\u0000\u0000XY\u0005\u0003\u0000\u0000YZ\u0005\u0004\u0000\u0000Z\u0011"+
		"\u0001\u0000\u0000\u0000\u0003\u0015 .";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}