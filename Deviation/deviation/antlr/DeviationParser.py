# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .DeviationListener import DeviationListener
    from .DeviationVisitor import DeviationVisitor
else:
    from DeviationListener import DeviationListener
    from DeviationVisitor import DeviationVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\20\u0091\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\6\2\"\n\2\r\2\16")
        buf.write(u"\2#\3\3\3\3\3\3\3\3\5\3*\n\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\5\4\66\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\5\5B\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write(u"\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write(u"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tc\n\t\3")
        buf.write(u"\t\3\t\3\t\7\th\n\t\f\t\16\tk\13\t\3\n\3\n\3\n\7\np\n")
        buf.write(u"\n\f\n\16\ns\13\n\3\13\3\13\5\13w\n\13\3\f\3\f\3\f\3")
        buf.write(u"\f\3\r\3\r\3\r\7\r\u0080\n\r\f\r\16\r\u0083\13\r\3\16")
        buf.write(u"\3\16\3\17\6\17\u0088\n\17\r\17\16\17\u0089\3\20\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\2\3\20\21\2\4\6\b\n\f\16\20\22\24")
        buf.write(u"\26\30\32\34\36\2\2\u0090\2!\3\2\2\2\4)\3\2\2\2\6\65")
        buf.write(u"\3\2\2\2\bA\3\2\2\2\nC\3\2\2\2\fJ\3\2\2\2\16N\3\2\2\2")
        buf.write(u"\20b\3\2\2\2\22l\3\2\2\2\24v\3\2\2\2\26x\3\2\2\2\30|")
        buf.write(u"\3\2\2\2\32\u0084\3\2\2\2\34\u0087\3\2\2\2\36\u008b\3")
        buf.write(u"\2\2\2 \"\5\4\3\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3")
        buf.write(u"\2\2\2$\3\3\2\2\2%*\5\6\4\2&*\5\b\5\2\'*\5\n\6\2(*\5")
        buf.write(u"\f\7\2)%\3\2\2\2)&\3\2\2\2)\'\3\2\2\2)(\3\2\2\2*\5\3")
        buf.write(u"\2\2\2+,\5\20\t\2,-\7\f\2\2-.\5\20\t\2.\66\3\2\2\2/\60")
        buf.write(u"\7\6\2\2\60\61\5\20\t\2\61\62\7\f\2\2\62\63\5\20\t\2")
        buf.write(u"\63\64\7\7\2\2\64\66\3\2\2\2\65+\3\2\2\2\65/\3\2\2\2")
        buf.write(u"\66\7\3\2\2\2\678\7\6\2\289\5\16\b\29:\7\3\2\2:;\5\24")
        buf.write(u"\13\2;<\7\7\2\2<B\3\2\2\2=>\5\16\b\2>?\7\3\2\2?@\5\24")
        buf.write(u"\13\2@B\3\2\2\2A\67\3\2\2\2A=\3\2\2\2B\t\3\2\2\2CD\7")
        buf.write(u"\n\2\2DE\7\6\2\2EF\5\20\t\2FG\7\4\2\2GH\5\30\r\2HI\7")
        buf.write(u"\7\2\2I\13\3\2\2\2JK\5\b\5\2KL\7\13\2\2LM\5\6\4\2M\r")
        buf.write(u"\3\2\2\2NO\7\f\2\2OP\7\6\2\2PQ\5\22\n\2QR\7\7\2\2R\17")
        buf.write(u"\3\2\2\2ST\b\t\1\2Tc\7\r\2\2Uc\7\t\2\2Vc\5\26\f\2WX\7")
        buf.write(u"\f\2\2XY\7\6\2\2YZ\5\22\n\2Z[\7\7\2\2[c\3\2\2\2\\]\7")
        buf.write(u"\6\2\2]^\5\20\t\2^_\7\b\2\2_`\5\20\t\2`a\7\7\2\2ac\3")
        buf.write(u"\2\2\2bS\3\2\2\2bU\3\2\2\2bV\3\2\2\2bW\3\2\2\2b\\\3\2")
        buf.write(u"\2\2ci\3\2\2\2de\f\4\2\2ef\7\b\2\2fh\5\20\t\5gd\3\2\2")
        buf.write(u"\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2j\21\3\2\2\2ki\3\2\2")
        buf.write(u"\2lq\5\20\t\2mn\7\4\2\2np\5\20\t\2om\3\2\2\2ps\3\2\2")
        buf.write(u"\2qo\3\2\2\2qr\3\2\2\2r\23\3\2\2\2sq\3\2\2\2tw\7\r\2")
        buf.write(u"\2uw\5\26\f\2vt\3\2\2\2vu\3\2\2\2w\25\3\2\2\2xy\7\f\2")
        buf.write(u"\2yz\7\5\2\2z{\5\32\16\2{\27\3\2\2\2|\u0081\5\26\f\2")
        buf.write(u"}~\7\4\2\2~\u0080\5\26\f\2\177}\3\2\2\2\u0080\u0083\3")
        buf.write(u"\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\31")
        buf.write(u"\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0085\7\f\2\2\u0085")
        buf.write(u"\33\3\2\2\2\u0086\u0088\5\36\20\2\u0087\u0086\3\2\2\2")
        buf.write(u"\u0088\u0089\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a")
        buf.write(u"\3\2\2\2\u008a\35\3\2\2\2\u008b\u008c\7\f\2\2\u008c\u008d")
        buf.write(u"\7\6\2\2\u008d\u008e\7\r\2\2\u008e\u008f\7\7\2\2\u008f")
        buf.write(u"\37\3\2\2\2\f#)\65Abiqv\u0081\u0089")
        return buf.getvalue()


class DeviationParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'@'", u"','", u"':'", u"'('", u"')'", 
                     u"<INVALID>", u"'noLoc'", u"'timeline'", u"'=>'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"LPAREN", u"RPAREN", u"INFIX", u"NOLOC", u"TIMELINE", 
                      u"IMPLIES", u"ID", u"INTEGER", u"STRING", u"LINE_COMMENT", 
                      u"WHITE_SPACE" ]

    RULE_unit = 0
    RULE_fact = 1
    RULE_constraint = 2
    RULE_event = 3
    RULE_timeline = 4
    RULE_invariant = 5
    RULE_expression = 6
    RULE_term = 7
    RULE_termlist = 8
    RULE_timestamp = 9
    RULE_variable = 10
    RULE_varlist = 11
    RULE_vartype = 12
    RULE_configuration = 13
    RULE_setting = 14

    ruleNames =  [ u"unit", u"fact", u"constraint", u"event", u"timeline", 
                   u"invariant", u"expression", u"term", u"termlist", u"timestamp", 
                   u"variable", u"varlist", u"vartype", u"configuration", 
                   u"setting" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    LPAREN=4
    RPAREN=5
    INFIX=6
    NOLOC=7
    TIMELINE=8
    IMPLIES=9
    ID=10
    INTEGER=11
    STRING=12
    LINE_COMMENT=13
    WHITE_SPACE=14

    def __init__(self, input):
        super(DeviationParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class UnitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.UnitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def fact(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DeviationParser.FactContext)
            else:
                return self.getTypedRuleContext(DeviationParser.FactContext,i)


        def getRuleIndex(self):
            return DeviationParser.RULE_unit

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterUnit(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitUnit(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitUnit(self)
            else:
                return visitor.visitChildren(self)




    def unit(self):

        localctx = DeviationParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.fact()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DeviationParser.LPAREN) | (1 << DeviationParser.NOLOC) | (1 << DeviationParser.TIMELINE) | (1 << DeviationParser.ID) | (1 << DeviationParser.INTEGER))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.FactContext, self).__init__(parent, invokingState)
            self.parser = parser

        def constraint(self):
            return self.getTypedRuleContext(DeviationParser.ConstraintContext,0)


        def event(self):
            return self.getTypedRuleContext(DeviationParser.EventContext,0)


        def timeline(self):
            return self.getTypedRuleContext(DeviationParser.TimelineContext,0)


        def invariant(self):
            return self.getTypedRuleContext(DeviationParser.InvariantContext,0)


        def getRuleIndex(self):
            return DeviationParser.RULE_fact

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterFact(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitFact(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitFact(self)
            else:
                return visitor.visitChildren(self)




    def fact(self):

        localctx = DeviationParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fact)
        try:
            self.state = 39
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.constraint()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.event()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.timeline()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.invariant()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.ConstraintContext, self).__init__(parent, invokingState)
            self.parser = parser

        def term(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DeviationParser.TermContext)
            else:
                return self.getTypedRuleContext(DeviationParser.TermContext,i)


        def ID(self):
            return self.getToken(DeviationParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DeviationParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(DeviationParser.RPAREN, 0)

        def getRuleIndex(self):
            return DeviationParser.RULE_constraint

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterConstraint(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitConstraint(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitConstraint(self)
            else:
                return visitor.visitChildren(self)




    def constraint(self):

        localctx = DeviationParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_constraint)
        try:
            self.state = 51
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.term(0)
                self.state = 42
                self.match(DeviationParser.ID)
                self.state = 43
                self.term(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(DeviationParser.LPAREN)
                self.state = 46
                self.term(0)
                self.state = 47
                self.match(DeviationParser.ID)
                self.state = 48
                self.term(0)
                self.state = 49
                self.match(DeviationParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EventContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.EventContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(DeviationParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(DeviationParser.ExpressionContext,0)


        def timestamp(self):
            return self.getTypedRuleContext(DeviationParser.TimestampContext,0)


        def RPAREN(self):
            return self.getToken(DeviationParser.RPAREN, 0)

        def getRuleIndex(self):
            return DeviationParser.RULE_event

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterEvent(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitEvent(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitEvent(self)
            else:
                return visitor.visitChildren(self)




    def event(self):

        localctx = DeviationParser.EventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_event)
        try:
            self.state = 63
            token = self._input.LA(1)
            if token in [DeviationParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(DeviationParser.LPAREN)
                self.state = 54
                self.expression()
                self.state = 55
                self.match(DeviationParser.T__0)
                self.state = 56
                self.timestamp()
                self.state = 57
                self.match(DeviationParser.RPAREN)

            elif token in [DeviationParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.expression()
                self.state = 60
                self.match(DeviationParser.T__0)
                self.state = 61
                self.timestamp()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimelineContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.TimelineContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TIMELINE(self):
            return self.getToken(DeviationParser.TIMELINE, 0)

        def LPAREN(self):
            return self.getToken(DeviationParser.LPAREN, 0)

        def term(self):
            return self.getTypedRuleContext(DeviationParser.TermContext,0)


        def varlist(self):
            return self.getTypedRuleContext(DeviationParser.VarlistContext,0)


        def RPAREN(self):
            return self.getToken(DeviationParser.RPAREN, 0)

        def getRuleIndex(self):
            return DeviationParser.RULE_timeline

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterTimeline(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitTimeline(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitTimeline(self)
            else:
                return visitor.visitChildren(self)




    def timeline(self):

        localctx = DeviationParser.TimelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_timeline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(DeviationParser.TIMELINE)
            self.state = 66
            self.match(DeviationParser.LPAREN)
            self.state = 67
            self.term(0)
            self.state = 68
            self.match(DeviationParser.T__1)
            self.state = 69
            self.varlist()
            self.state = 70
            self.match(DeviationParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InvariantContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.InvariantContext, self).__init__(parent, invokingState)
            self.parser = parser

        def event(self):
            return self.getTypedRuleContext(DeviationParser.EventContext,0)


        def IMPLIES(self):
            return self.getToken(DeviationParser.IMPLIES, 0)

        def constraint(self):
            return self.getTypedRuleContext(DeviationParser.ConstraintContext,0)


        def getRuleIndex(self):
            return DeviationParser.RULE_invariant

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterInvariant(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitInvariant(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitInvariant(self)
            else:
                return visitor.visitChildren(self)




    def invariant(self):

        localctx = DeviationParser.InvariantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_invariant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.event()
            self.state = 73
            self.match(DeviationParser.IMPLIES)
            self.state = 74
            self.constraint()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeviationParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DeviationParser.LPAREN, 0)

        def termlist(self):
            return self.getTypedRuleContext(DeviationParser.TermlistContext,0)


        def RPAREN(self):
            return self.getToken(DeviationParser.RPAREN, 0)

        def getRuleIndex(self):
            return DeviationParser.RULE_expression

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = DeviationParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(DeviationParser.ID)
            self.state = 77
            self.match(DeviationParser.LPAREN)
            self.state = 78
            self.termlist()
            self.state = 79
            self.match(DeviationParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.TermContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(DeviationParser.INTEGER, 0)

        def NOLOC(self):
            return self.getToken(DeviationParser.NOLOC, 0)

        def variable(self):
            return self.getTypedRuleContext(DeviationParser.VariableContext,0)


        def ID(self):
            return self.getToken(DeviationParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DeviationParser.LPAREN, 0)

        def termlist(self):
            return self.getTypedRuleContext(DeviationParser.TermlistContext,0)


        def RPAREN(self):
            return self.getToken(DeviationParser.RPAREN, 0)

        def term(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DeviationParser.TermContext)
            else:
                return self.getTypedRuleContext(DeviationParser.TermContext,i)


        def INFIX(self):
            return self.getToken(DeviationParser.INFIX, 0)

        def getRuleIndex(self):
            return DeviationParser.RULE_term

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterTerm(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitTerm(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DeviationParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 82
                self.match(DeviationParser.INTEGER)
                pass

            elif la_ == 2:
                self.state = 83
                self.match(DeviationParser.NOLOC)
                pass

            elif la_ == 3:
                self.state = 84
                self.variable()
                pass

            elif la_ == 4:
                self.state = 85
                self.match(DeviationParser.ID)
                self.state = 86
                self.match(DeviationParser.LPAREN)
                self.state = 87
                self.termlist()
                self.state = 88
                self.match(DeviationParser.RPAREN)
                pass

            elif la_ == 5:
                self.state = 90
                self.match(DeviationParser.LPAREN)
                self.state = 91
                self.term(0)
                self.state = 92
                self.match(DeviationParser.INFIX)
                self.state = 93
                self.term(0)
                self.state = 94
                self.match(DeviationParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 103
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DeviationParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 98
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 99
                    self.match(DeviationParser.INFIX)
                    self.state = 100
                    self.term(3) 
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TermlistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.TermlistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def term(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DeviationParser.TermContext)
            else:
                return self.getTypedRuleContext(DeviationParser.TermContext,i)


        def getRuleIndex(self):
            return DeviationParser.RULE_termlist

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterTermlist(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitTermlist(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitTermlist(self)
            else:
                return visitor.visitChildren(self)




    def termlist(self):

        localctx = DeviationParser.TermlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_termlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.term(0)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DeviationParser.T__1:
                self.state = 107
                self.match(DeviationParser.T__1)
                self.state = 108
                self.term(0)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimestampContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.TimestampContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(DeviationParser.INTEGER, 0)

        def variable(self):
            return self.getTypedRuleContext(DeviationParser.VariableContext,0)


        def getRuleIndex(self):
            return DeviationParser.RULE_timestamp

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterTimestamp(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitTimestamp(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitTimestamp(self)
            else:
                return visitor.visitChildren(self)




    def timestamp(self):

        localctx = DeviationParser.TimestampContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_timestamp)
        try:
            self.state = 116
            token = self._input.LA(1)
            if token in [DeviationParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(DeviationParser.INTEGER)

            elif token in [DeviationParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.variable()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.VariableContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeviationParser.ID, 0)

        def vartype(self):
            return self.getTypedRuleContext(DeviationParser.VartypeContext,0)


        def getRuleIndex(self):
            return DeviationParser.RULE_variable

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterVariable(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitVariable(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = DeviationParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(DeviationParser.ID)
            self.state = 119
            self.match(DeviationParser.T__2)
            self.state = 120
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarlistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.VarlistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DeviationParser.VariableContext)
            else:
                return self.getTypedRuleContext(DeviationParser.VariableContext,i)


        def getRuleIndex(self):
            return DeviationParser.RULE_varlist

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterVarlist(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitVarlist(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitVarlist(self)
            else:
                return visitor.visitChildren(self)




    def varlist(self):

        localctx = DeviationParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.variable()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DeviationParser.T__1:
                self.state = 123
                self.match(DeviationParser.T__1)
                self.state = 124
                self.variable()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VartypeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.VartypeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeviationParser.ID, 0)

        def getRuleIndex(self):
            return DeviationParser.RULE_vartype

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterVartype(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitVartype(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = DeviationParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_vartype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(DeviationParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConfigurationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.ConfigurationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def setting(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DeviationParser.SettingContext)
            else:
                return self.getTypedRuleContext(DeviationParser.SettingContext,i)


        def getRuleIndex(self):
            return DeviationParser.RULE_configuration

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterConfiguration(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitConfiguration(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitConfiguration(self)
            else:
                return visitor.visitChildren(self)




    def configuration(self):

        localctx = DeviationParser.ConfigurationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_configuration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 132
                self.setting()
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==DeviationParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SettingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DeviationParser.SettingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeviationParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DeviationParser.LPAREN, 0)

        def INTEGER(self):
            return self.getToken(DeviationParser.INTEGER, 0)

        def RPAREN(self):
            return self.getToken(DeviationParser.RPAREN, 0)

        def getRuleIndex(self):
            return DeviationParser.RULE_setting

        def enterRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.enterSetting(self)

        def exitRule(self, listener):
            if isinstance( listener, DeviationListener ):
                listener.exitSetting(self)

        def accept(self, visitor):
            if isinstance( visitor, DeviationVisitor ):
                return visitor.visitSetting(self)
            else:
                return visitor.visitChildren(self)




    def setting(self):

        localctx = DeviationParser.SettingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_setting)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(DeviationParser.ID)
            self.state = 138
            self.match(DeviationParser.LPAREN)
            self.state = 139
            self.match(DeviationParser.INTEGER)
            self.state = 140
            self.match(DeviationParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def term_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         



