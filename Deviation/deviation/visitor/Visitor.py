""" The Visitor class that calls into antlr.
"""

from ..logic.SymbolTable import (SymbolTable, Configuration)

from ..logic.Syntax import (Event, Invariant, Timeline, Operation, Term, Type, Variable, Integer)


class Visitor:

    NOLOC = None

    # rather than pass around the maximum time stamp; we use a term and assert its value
    MAXTIME = None


    def __init__(self, facts, filename):
        self.facts = facts
        self.filename = filename

        if facts is not None:
            if Visitor.NOLOC  is None:
                Visitor.NOLOC = Variable(SymbolTable.NOLOC, Type(SymbolTable.PT2, None), None, SymbolTable.PT2)
            if Visitor.MAXTIME is None:
                Visitor.MAXTIME = Variable(SymbolTable.MAXTIME, Type(SymbolTable.TIME, None), None, SymbolTable.TIME)


    def visitUnit(self, ctx):
        for f in ctx.fact():
            self.visitFact(f)

    def visitFact(self, ctx):
        if ctx.event() is not None:
            self.visitEvent(ctx.event())
        elif ctx.timeline() is not None:
            self.visitTimeline(ctx.timeline())
        elif ctx.constraint() is not None:
            self.visitConstraint(ctx.constraint())
        else:
            self.visitInvariant(ctx.invariant())


    def visitInvariant(self, ctx):
        # maps the name of the bound variable to the first occurrence seen
        bound_variables = {}
        sym = ctx.IMPLIES().getSymbol()
        location = Location(self.filename, sym.line)
        event = self.visitEvent(ctx.event(), bound_variables)
        constraint = self.visitConstraint(ctx.constraint(), bound_variables)
        invariant = Invariant(event, constraint, bound_variables, location)
        self.facts.addInvariant(invariant)
        return invariant


    def visitEvent(self, ctx, bound_variables = None):
        timestamp = self.visitTimestamp(ctx.timestamp(), bound_variables)
        expression = self.visitExpression(ctx.expression(), timestamp, bound_variables)
        function = expression.function
        event = Event(expression, timestamp, function.location)
        if bound_variables is None:
            # parsing a naked event; it gets added to the facts
            if Visitor.NOLOC in expression.fv:
                print('Skipping noLoc event {0}'.format(event))
            else:
                self.facts.addEvent(event)
        else:
            # better see if the timestamp is a bound variable (it could also be free)
            if isinstance(timestamp, Variable) and timestamp.bound:
                bound_variables[timestamp.name] = timestamp
        return event

    def visitTimeline(self, ctx):
        sym = ctx.TIMELINE().getSymbol()
        location = Location(self.filename, sym.line)
        term = self.visitTerm(ctx.term(), SymbolTable.THING)
        varlist = self.visitVarlist(ctx.varlist())
        timeline = Timeline(term, varlist, location)
        self.facts.addTimeline(timeline)
        return timeline

    def visitConstraint(self, ctx, bound_variables = None):
        op = self.visitOperation(ctx)
        args = []
        for t in ctx.term():
            ts = self.visitTerm(t, SymbolTable.ATOM, bound_variables)
            args.append(ts)
        term = Term(op, args, op.location)
        if bound_variables is None:
            # parsing a naked constraint; it gets added to the facts
            self.facts.addConstraint(term)
        return term

    def visitExpression(self, ctx, timestamp, bound_variables = None):
        # N.B. we are adding the timestamp explicitly to the event; so that
        # the timestamp aspect of the event is conceptually redundant; though
        # we still use it to map timestamps to events in the Facts class.
        function = self.visitOperation(ctx)
        termlist = self.visitTermlist(ctx.termlist(), function, bound_variables)
        termlist.append(timestamp)
        return Term(function, termlist, function.location)

    def visitTimestamp(self, ctx, bound_variables = None):
        if ctx.INTEGER() is not None:
            integer = self.visitInteger(ctx, SymbolTable.TIME)
            self.facts.addTimeStamp(integer)
            return integer
        var = self.visitVariable(ctx.variable(), SymbolTable.TIME, bound_variables)
        self.facts.addTimeStamp(var)
        return var

    def visitOperation(self, ctx):
        sym = ctx.ID().getSymbol()
        location = Location(self.filename, sym.line)
        return Operation(SymbolTable.canonicalize(sym.text), location)

    def visitTypeConstant(self, ctx):
        sym = ctx.ID().getSymbol()
        location = Location(self.filename, sym.line)
        return Type(SymbolTable.canonicalize(sym.text), location)

    def visitInfixOperation(self, ctx):
        sym = ctx.INFIX().getSymbol()
        location = Location(self.filename, sym.line)
        operation = Operation(SymbolTable.canonicalize(sym.text), location)
        return operation

    def visitInteger(self, ctx, typename):
        sym = ctx.INTEGER().getSymbol()
        location = Location(self.filename, sym.line)
        return Integer(sym.text, typename, location)

    def visitTerm(self, ctx, typename, bound_variables = None):
        if ctx.INTEGER():
            return self.visitInteger(ctx, typename)
        if ctx.NOLOC():
            return self.visitNoLoc(ctx.NOLOC())
        if ctx.variable():
            return self.visitVariable(ctx.variable(), typename, bound_variables)
        if  ctx.INFIX():
            function = self.visitInfixOperation(ctx)
            args = [self.visitTerm(ctx.term(0), SymbolTable.NAT, bound_variables), self.visitTerm(ctx.term(1), SymbolTable.NAT, bound_variables)]
            return Term(function, args, function.location)
        termlist = ctx.termlist()
        #if termlist is None:
        #    return self.visitVariable(ctx)
        function = self.visitOperation(ctx)
        args = self.visitTermlist(termlist, function, bound_variables)
        retval = Term(function, args, function.location)
        return retval

    def visitTermlist(self, ctx, function, bound_variables = None):
        retval = []
        signature = function.signature
        argtypes = signature[0]
        for ti, term in enumerate(ctx.term()):
            if ti >= len(argtypes):
                print('Incorrect arity of {0}: {1}\n'.format(function.name, ti + 1))
                return None
            retval.append(self.visitTerm(term, argtypes[ti], bound_variables))
        return retval

    def visitNoLoc(self, noloc):
        sym = noloc.getSymbol()
        location = Location(self.filename, sym.line)
        #varname = '{0}{1}'.format(SymbolTable.NOLOC, self.noLocCounter)
        varname = SymbolTable.NOLOC
        #self.noLocCounter += 1
        retval = Variable(varname, Type(SymbolTable.PT2, location), location, SymbolTable.PT2)
        self.facts.addFV(retval)
        return retval

    def visitVariable(self, ctx, typename, bound_variables = None):
        varname = ctx.ID()
        t = varname.getSymbol()
        vartype = self.visitTypeConstant(ctx.vartype())
        location = Location(self.filename, t.line)
        retval = Variable(t.text, vartype, location, typename, bound_variables)
        # the variable could be bound; so we should not assume that it is free
        if not retval.bound:
            self.facts.addFV(retval)
        return retval

    def visitVarlist(self, ctx):
        retval = []
        for v in ctx.variable():
            retval.append(self.visitVariable(v, SymbolTable.TIME))
        return retval

    def visitConfiguration(self, ctx):
        for setting in ctx.setting():
            if not self.visitSetting(setting):
                return False
        return True

    def visitSetting(self, ctx):
        key = ctx.ID().getSymbol().text
        value = int(ctx.INTEGER().getSymbol().text)
        return Configuration.configure(key, value)


class Location:

    def __init__(self, filename, lineno):
        self.filename = filename
        self.lineno = lineno


    def __str__(self):
        return '[{0}:{1}]'.format(self.filename, self.lineno)
