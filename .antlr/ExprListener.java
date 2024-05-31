// Generated from d:/.cosas/.universidad/.Teoria de Compiladores/HydraCompiler/HydraCompiler/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ExprParser}.
 */
public interface ExprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ExprParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ExprParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ExprParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#statment}.
	 * @param ctx the parse tree
	 */
	void enterStatment(ExprParser.StatmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#statment}.
	 * @param ctx the parse tree
	 */
	void exitStatment(ExprParser.StatmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#ifstat}.
	 * @param ctx the parse tree
	 */
	void enterIfstat(ExprParser.IfstatContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#ifstat}.
	 * @param ctx the parse tree
	 */
	void exitIfstat(ExprParser.IfstatContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#funcstat}.
	 * @param ctx the parse tree
	 */
	void enterFuncstat(ExprParser.FuncstatContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#funcstat}.
	 * @param ctx the parse tree
	 */
	void exitFuncstat(ExprParser.FuncstatContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(ExprParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(ExprParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#func}.
	 * @param ctx the parse tree
	 */
	void enterFunc(ExprParser.FuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#func}.
	 * @param ctx the parse tree
	 */
	void exitFunc(ExprParser.FuncContext ctx);
}