// Generated from /Users/aleksandraignacyk/Studia/semestr3/Kompilatory/DataScript/kompilatory/DataScript.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link DataScriptParser}.
 */
public interface DataScriptListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link DataScriptParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(DataScriptParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link DataScriptParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(DataScriptParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link DataScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(DataScriptParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DataScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(DataScriptParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DataScriptParser#loadDataStatement}.
	 * @param ctx the parse tree
	 */
	void enterLoadDataStatement(DataScriptParser.LoadDataStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DataScriptParser#loadDataStatement}.
	 * @param ctx the parse tree
	 */
	void exitLoadDataStatement(DataScriptParser.LoadDataStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DataScriptParser#displayDataStatement}.
	 * @param ctx the parse tree
	 */
	void enterDisplayDataStatement(DataScriptParser.DisplayDataStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DataScriptParser#displayDataStatement}.
	 * @param ctx the parse tree
	 */
	void exitDisplayDataStatement(DataScriptParser.DisplayDataStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DataScriptParser#splitDataStatement}.
	 * @param ctx the parse tree
	 */
	void enterSplitDataStatement(DataScriptParser.SplitDataStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DataScriptParser#splitDataStatement}.
	 * @param ctx the parse tree
	 */
	void exitSplitDataStatement(DataScriptParser.SplitDataStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DataScriptParser#linearRegressionStatement}.
	 * @param ctx the parse tree
	 */
	void enterLinearRegressionStatement(DataScriptParser.LinearRegressionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DataScriptParser#linearRegressionStatement}.
	 * @param ctx the parse tree
	 */
	void exitLinearRegressionStatement(DataScriptParser.LinearRegressionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DataScriptParser#modelEvaluationStatement}.
	 * @param ctx the parse tree
	 */
	void enterModelEvaluationStatement(DataScriptParser.ModelEvaluationStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DataScriptParser#modelEvaluationStatement}.
	 * @param ctx the parse tree
	 */
	void exitModelEvaluationStatement(DataScriptParser.ModelEvaluationStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DataScriptParser#meanStatement}.
	 * @param ctx the parse tree
	 */
	void enterMeanStatement(DataScriptParser.MeanStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DataScriptParser#meanStatement}.
	 * @param ctx the parse tree
	 */
	void exitMeanStatement(DataScriptParser.MeanStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DataScriptParser#pointPlotStatement}.
	 * @param ctx the parse tree
	 */
	void enterPointPlotStatement(DataScriptParser.PointPlotStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DataScriptParser#pointPlotStatement}.
	 * @param ctx the parse tree
	 */
	void exitPointPlotStatement(DataScriptParser.PointPlotStatementContext ctx);
}