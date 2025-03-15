# Generated from MiGramatica.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("N\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\6\16?\n\16\r\16")
        buf.write("\16\16@\3\17\6\17D\n\17\r\17\16\17E\3\20\6\20I\n\20\r")
        buf.write("\20\16\20J\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2\5")
        buf.write("\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2P\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7\'\3\2\2\2\t)\3")
        buf.write("\2\2\2\13+\3\2\2\2\r-\3\2\2\2\17/\3\2\2\2\21\61\3\2\2")
        buf.write("\2\23\63\3\2\2\2\25\65\3\2\2\2\278\3\2\2\2\31;\3\2\2\2")
        buf.write("\33>\3\2\2\2\35C\3\2\2\2\37H\3\2\2\2!\"\7=\2\2\"\4\3\2")
        buf.write("\2\2#$\7h\2\2$%\7q\2\2%&\7t\2\2&\6\3\2\2\2\'(\7*\2\2(")
        buf.write("\b\3\2\2\2)*\7+\2\2*\n\3\2\2\2+,\7}\2\2,\f\3\2\2\2-.\7")
        buf.write("\177\2\2.\16\3\2\2\2/\60\7?\2\2\60\20\3\2\2\2\61\62\7")
        buf.write("@\2\2\62\22\3\2\2\2\63\64\7>\2\2\64\24\3\2\2\2\65\66\7")
        buf.write("?\2\2\66\67\7?\2\2\67\26\3\2\2\289\7#\2\29:\7?\2\2:\30")
        buf.write("\3\2\2\2;<\7-\2\2<\32\3\2\2\2=?\t\2\2\2>=\3\2\2\2?@\3")
        buf.write("\2\2\2@>\3\2\2\2@A\3\2\2\2A\34\3\2\2\2BD\t\3\2\2CB\3\2")
        buf.write("\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\36\3\2\2\2GI\t\4\2")
        buf.write("\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2KL\3\2\2\2L")
        buf.write("M\b\20\2\2M \3\2\2\2\6\2@EJ\3\b\2\2")
        return buf.getvalue()


class MiGramaticaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    ID = 13
    INT = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'for'", "'('", "')'", "'{'", "'}'", "'='", "'>'", "'<'", 
            "'=='", "'!='", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "ID", "INT", 
                  "WS" ]

    grammarFileName = "MiGramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


