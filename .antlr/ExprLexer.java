// Generated from d:/.cosas/.universidad/.Teoria de Compiladores/compilador/Expr.g4 by ANTLR 4.13.1
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
		T__0=1, T__1=2, T__2=3, T__3=4, AND=5, OR=6, NOT=7, IF=8, DEF=9, EQ=10, 
		COMMA=11, SEMI=12, LPAREN=13, RPAREN=14, LCURLY=15, RCURLY=16, INT=17, 
		WS=18, ID=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "AND", "OR", "NOT", "IF", "DEF", "EQ", 
			"COMMA", "SEMI", "LPAREN", "RPAREN", "LCURLY", "RCURLY", "INT", "WS", 
			"ID"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'return'", "'=='", "'+'", "'-'", "'and'", "'or'", "'not'", "'if'", 
			"'def'", "'='", "','", "';'", "'('", "')'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "AND", "OR", "NOT", "IF", "DEF", "EQ", 
			"COMMA", "SEMI", "LPAREN", "RPAREN", "LCURLY", "RCURLY", "INT", "WS", 
			"ID"
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
		"\u0004\u0000\u0013h\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u0010\u0004\u0010W\b\u0010\u000b\u0010\f\u0010"+
		"X\u0001\u0011\u0004\u0011\\\b\u0011\u000b\u0011\f\u0011]\u0001\u0011\u0001"+
		"\u0011\u0001\u0012\u0001\u0012\u0005\u0012d\b\u0012\n\u0012\f\u0012g\t"+
		"\u0012\u0000\u0000\u0013\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004"+
		"\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017"+
		"\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\u0001"+
		"\u0000\u0004\u0001\u000009\u0003\u0000\t\n\f\r  \u0003\u0000AZ__az\u0004"+
		"\u000009AZ__azj\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001"+
		"\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001"+
		"\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000"+
		"\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000"+
		"\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000"+
		"\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000"+
		"\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000"+
		"\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000"+
		"%\u0001\u0000\u0000\u0000\u0001\'\u0001\u0000\u0000\u0000\u0003.\u0001"+
		"\u0000\u0000\u0000\u00051\u0001\u0000\u0000\u0000\u00073\u0001\u0000\u0000"+
		"\u0000\t5\u0001\u0000\u0000\u0000\u000b9\u0001\u0000\u0000\u0000\r<\u0001"+
		"\u0000\u0000\u0000\u000f@\u0001\u0000\u0000\u0000\u0011C\u0001\u0000\u0000"+
		"\u0000\u0013G\u0001\u0000\u0000\u0000\u0015I\u0001\u0000\u0000\u0000\u0017"+
		"K\u0001\u0000\u0000\u0000\u0019M\u0001\u0000\u0000\u0000\u001bO\u0001"+
		"\u0000\u0000\u0000\u001dQ\u0001\u0000\u0000\u0000\u001fS\u0001\u0000\u0000"+
		"\u0000!V\u0001\u0000\u0000\u0000#[\u0001\u0000\u0000\u0000%a\u0001\u0000"+
		"\u0000\u0000\'(\u0005r\u0000\u0000()\u0005e\u0000\u0000)*\u0005t\u0000"+
		"\u0000*+\u0005u\u0000\u0000+,\u0005r\u0000\u0000,-\u0005n\u0000\u0000"+
		"-\u0002\u0001\u0000\u0000\u0000./\u0005=\u0000\u0000/0\u0005=\u0000\u0000"+
		"0\u0004\u0001\u0000\u0000\u000012\u0005+\u0000\u00002\u0006\u0001\u0000"+
		"\u0000\u000034\u0005-\u0000\u00004\b\u0001\u0000\u0000\u000056\u0005a"+
		"\u0000\u000067\u0005n\u0000\u000078\u0005d\u0000\u00008\n\u0001\u0000"+
		"\u0000\u00009:\u0005o\u0000\u0000:;\u0005r\u0000\u0000;\f\u0001\u0000"+
		"\u0000\u0000<=\u0005n\u0000\u0000=>\u0005o\u0000\u0000>?\u0005t\u0000"+
		"\u0000?\u000e\u0001\u0000\u0000\u0000@A\u0005i\u0000\u0000AB\u0005f\u0000"+
		"\u0000B\u0010\u0001\u0000\u0000\u0000CD\u0005d\u0000\u0000DE\u0005e\u0000"+
		"\u0000EF\u0005f\u0000\u0000F\u0012\u0001\u0000\u0000\u0000GH\u0005=\u0000"+
		"\u0000H\u0014\u0001\u0000\u0000\u0000IJ\u0005,\u0000\u0000J\u0016\u0001"+
		"\u0000\u0000\u0000KL\u0005;\u0000\u0000L\u0018\u0001\u0000\u0000\u0000"+
		"MN\u0005(\u0000\u0000N\u001a\u0001\u0000\u0000\u0000OP\u0005)\u0000\u0000"+
		"P\u001c\u0001\u0000\u0000\u0000QR\u0005{\u0000\u0000R\u001e\u0001\u0000"+
		"\u0000\u0000ST\u0005}\u0000\u0000T \u0001\u0000\u0000\u0000UW\u0007\u0000"+
		"\u0000\u0000VU\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000XV\u0001"+
		"\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000Y\"\u0001\u0000\u0000\u0000"+
		"Z\\\u0007\u0001\u0000\u0000[Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000"+
		"\u0000][\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^_\u0001\u0000"+
		"\u0000\u0000_`\u0006\u0011\u0000\u0000`$\u0001\u0000\u0000\u0000ae\u0007"+
		"\u0002\u0000\u0000bd\u0007\u0003\u0000\u0000cb\u0001\u0000\u0000\u0000"+
		"dg\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000"+
		"\u0000f&\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000\u0004\u0000"+
		"X]e\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}