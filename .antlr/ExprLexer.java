// Generated from d:/.cosas/.universidad/.Teoria de Compiladores/HydraCompiler/HydraCompiler/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ExprLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		AND=10, OR=11, NOT=12, IF=13, DEF=14, EQ=15, COMMA=16, SEMI=17, LPAREN=18, 
		RPAREN=19, LCURLY=20, RCURLY=21, INT=22, FLOAT=23, WS=24, ID=25;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"AND", "OR", "NOT", "IF", "DEF", "EQ", "COMMA", "SEMI", "LPAREN", "RPAREN", 
			"LCURLY", "RCURLY", "INT", "FLOAT", "WS", "ID"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'int'", "'float'", "'return'", "'=='", "'*'", "'/'", "'+'", "'-'", 
			"':'", "'and'", "'or'", "'not'", "'if'", "'def'", "'='", "','", "';'", 
			"'('", "')'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "AND", "OR", 
			"NOT", "IF", "DEF", "EQ", "COMMA", "SEMI", "LPAREN", "RPAREN", "LCURLY", 
			"RCURLY", "INT", "FLOAT", "WS", "ID"
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


	public ExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0019\u008f\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f"+
		"\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015"+
		"\u0004\u0015s\b\u0015\u000b\u0015\f\u0015t\u0001\u0016\u0004\u0016x\b"+
		"\u0016\u000b\u0016\f\u0016y\u0001\u0016\u0001\u0016\u0004\u0016~\b\u0016"+
		"\u000b\u0016\f\u0016\u007f\u0001\u0017\u0004\u0017\u0083\b\u0017\u000b"+
		"\u0017\f\u0017\u0084\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0005"+
		"\u0018\u008b\b\u0018\n\u0018\f\u0018\u008e\t\u0018\u0000\u0000\u0019\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d"+
		"\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/"+
		"\u00181\u0019\u0001\u0000\u0005\u0001\u000009\u0001\u0000..\u0003\u0000"+
		"\t\n\f\r  \u0003\u0000AZ__az\u0004\u000009AZ__az\u0093\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000"+
		"\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000"+
		"\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000"+
		"\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000"+
		"\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'"+
		"\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000"+
		"\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000"+
		"\u00001\u0001\u0000\u0000\u0000\u00013\u0001\u0000\u0000\u0000\u00037"+
		"\u0001\u0000\u0000\u0000\u0005=\u0001\u0000\u0000\u0000\u0007D\u0001\u0000"+
		"\u0000\u0000\tG\u0001\u0000\u0000\u0000\u000bI\u0001\u0000\u0000\u0000"+
		"\rK\u0001\u0000\u0000\u0000\u000fM\u0001\u0000\u0000\u0000\u0011O\u0001"+
		"\u0000\u0000\u0000\u0013Q\u0001\u0000\u0000\u0000\u0015U\u0001\u0000\u0000"+
		"\u0000\u0017X\u0001\u0000\u0000\u0000\u0019\\\u0001\u0000\u0000\u0000"+
		"\u001b_\u0001\u0000\u0000\u0000\u001dc\u0001\u0000\u0000\u0000\u001fe"+
		"\u0001\u0000\u0000\u0000!g\u0001\u0000\u0000\u0000#i\u0001\u0000\u0000"+
		"\u0000%k\u0001\u0000\u0000\u0000\'m\u0001\u0000\u0000\u0000)o\u0001\u0000"+
		"\u0000\u0000+r\u0001\u0000\u0000\u0000-w\u0001\u0000\u0000\u0000/\u0082"+
		"\u0001\u0000\u0000\u00001\u0088\u0001\u0000\u0000\u000034\u0005i\u0000"+
		"\u000045\u0005n\u0000\u000056\u0005t\u0000\u00006\u0002\u0001\u0000\u0000"+
		"\u000078\u0005f\u0000\u000089\u0005l\u0000\u00009:\u0005o\u0000\u0000"+
		":;\u0005a\u0000\u0000;<\u0005t\u0000\u0000<\u0004\u0001\u0000\u0000\u0000"+
		"=>\u0005r\u0000\u0000>?\u0005e\u0000\u0000?@\u0005t\u0000\u0000@A\u0005"+
		"u\u0000\u0000AB\u0005r\u0000\u0000BC\u0005n\u0000\u0000C\u0006\u0001\u0000"+
		"\u0000\u0000DE\u0005=\u0000\u0000EF\u0005=\u0000\u0000F\b\u0001\u0000"+
		"\u0000\u0000GH\u0005*\u0000\u0000H\n\u0001\u0000\u0000\u0000IJ\u0005/"+
		"\u0000\u0000J\f\u0001\u0000\u0000\u0000KL\u0005+\u0000\u0000L\u000e\u0001"+
		"\u0000\u0000\u0000MN\u0005-\u0000\u0000N\u0010\u0001\u0000\u0000\u0000"+
		"OP\u0005:\u0000\u0000P\u0012\u0001\u0000\u0000\u0000QR\u0005a\u0000\u0000"+
		"RS\u0005n\u0000\u0000ST\u0005d\u0000\u0000T\u0014\u0001\u0000\u0000\u0000"+
		"UV\u0005o\u0000\u0000VW\u0005r\u0000\u0000W\u0016\u0001\u0000\u0000\u0000"+
		"XY\u0005n\u0000\u0000YZ\u0005o\u0000\u0000Z[\u0005t\u0000\u0000[\u0018"+
		"\u0001\u0000\u0000\u0000\\]\u0005i\u0000\u0000]^\u0005f\u0000\u0000^\u001a"+
		"\u0001\u0000\u0000\u0000_`\u0005d\u0000\u0000`a\u0005e\u0000\u0000ab\u0005"+
		"f\u0000\u0000b\u001c\u0001\u0000\u0000\u0000cd\u0005=\u0000\u0000d\u001e"+
		"\u0001\u0000\u0000\u0000ef\u0005,\u0000\u0000f \u0001\u0000\u0000\u0000"+
		"gh\u0005;\u0000\u0000h\"\u0001\u0000\u0000\u0000ij\u0005(\u0000\u0000"+
		"j$\u0001\u0000\u0000\u0000kl\u0005)\u0000\u0000l&\u0001\u0000\u0000\u0000"+
		"mn\u0005{\u0000\u0000n(\u0001\u0000\u0000\u0000op\u0005}\u0000\u0000p"+
		"*\u0001\u0000\u0000\u0000qs\u0007\u0000\u0000\u0000rq\u0001\u0000\u0000"+
		"\u0000st\u0001\u0000\u0000\u0000tr\u0001\u0000\u0000\u0000tu\u0001\u0000"+
		"\u0000\u0000u,\u0001\u0000\u0000\u0000vx\u0007\u0000\u0000\u0000wv\u0001"+
		"\u0000\u0000\u0000xy\u0001\u0000\u0000\u0000yw\u0001\u0000\u0000\u0000"+
		"yz\u0001\u0000\u0000\u0000z{\u0001\u0000\u0000\u0000{}\u0007\u0001\u0000"+
		"\u0000|~\u0007\u0000\u0000\u0000}|\u0001\u0000\u0000\u0000~\u007f\u0001"+
		"\u0000\u0000\u0000\u007f}\u0001\u0000\u0000\u0000\u007f\u0080\u0001\u0000"+
		"\u0000\u0000\u0080.\u0001\u0000\u0000\u0000\u0081\u0083\u0007\u0002\u0000"+
		"\u0000\u0082\u0081\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000"+
		"\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0084\u0085\u0001\u0000\u0000"+
		"\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u0087\u0006\u0017\u0000"+
		"\u0000\u00870\u0001\u0000\u0000\u0000\u0088\u008c\u0007\u0003\u0000\u0000"+
		"\u0089\u008b\u0007\u0004\u0000\u0000\u008a\u0089\u0001\u0000\u0000\u0000"+
		"\u008b\u008e\u0001\u0000\u0000\u0000\u008c\u008a\u0001\u0000\u0000\u0000"+
		"\u008c\u008d\u0001\u0000\u0000\u0000\u008d2\u0001\u0000\u0000\u0000\u008e"+
		"\u008c\u0001\u0000\u0000\u0000\u0006\u0000ty\u007f\u0084\u008c\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}