# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by DeviationParser.

class DeviationVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DeviationParser#unit.
    def visitUnit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#fact.
    def visitFact(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#constraint.
    def visitConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#event.
    def visitEvent(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#timeline.
    def visitTimeline(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#invariant.
    def visitInvariant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#term.
    def visitTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#termlist.
    def visitTermlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#timestamp.
    def visitTimestamp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#variable.
    def visitVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#varlist.
    def visitVarlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#vartype.
    def visitVartype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#configuration.
    def visitConfiguration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeviationParser#setting.
    def visitSetting(self, ctx):
        return self.visitChildren(ctx)


