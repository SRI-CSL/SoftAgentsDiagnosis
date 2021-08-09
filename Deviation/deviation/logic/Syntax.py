import sys

from yices import Terms

from ..util.StringBuilder import StringBuilder

from .SymbolTable import SymbolTable

from .YicesSignature import YicesSignature

from .Configuration import Configuration

from .Space import Space


def thingTerm2Yices(term):
    assert isinstance(term, SyntacticOccurrence)
    if term.function.name == SymbolTable.B:
        return 'b{0}'.format(str(term.args[0]))
    if term.function.name == SymbolTable.OB:
        return 'ob{0}'.format(str(term.args[0]))
    return None

def pt2Term2Yices(term):
    assert isinstance(term, SyntacticOccurrence)
    if isinstance(term, Variable):
        return term.name
    assert term.function.name == SymbolTable.PT
    return 'pt_{0}_{1}'.format(str(term.args[0]), str(term.args[1]))

def integerTerm2Yices(term):
    if isinstance(term, Variable):
        return term.name
    if isinstance(term, Integer):
        return term.value
    return int(term)

class SyntacticOccurrence:

    def __init__(self, location):
        self.location = location
        self.fv = None
        # memoize the hash and the printing & use it for indiscerability
        self.hash = None
        self.printstring = None
        # the two forms of a term; an int or a string
        self.yices_term =  None
        self.yices_string = None

    def __hash__(self):
        assert self.printstring is not None
        if self.hash is None:
            self.hash = hash(self.printstring)
        return self.hash

    def __eq__(self, other):
        return self.__class__ == other.__class__ and hash(self) == hash(other) and self.printstring == other.printstring

    # repr's goal is to be unambiguous
    def __repr__(self):
        return '{0} ... {1}'.format(str(self), str(self.location))

    def FV(self):
        assert self.fv is not None
        return self.fv


class Event(SyntacticOccurrence):

    def __init__(self, expression, timestamp, location):
        super().__init__(location)
        self.expression = expression
        self.timestamp = timestamp
        self.printstring = '{0} @ {1}'.format(str(self.expression), self.timestamp)
        self.fv = expression.fv #timestamp has already been added to the expression
        self.yices_term = self.expression.yices_term
        self.yices_string = self.expression.yices_string


    # str's goal is to be readable
    def __str__(self):
        return self.printstring

    def toYicesAssertion(self):
        return '(assert {0})\n'.format(self.expression.yices_string)


class Invariant(SyntacticOccurrence):
    """ Invariants have two semantics. Quantified and Quantifier Free. The former is too hard for yices2,
    The latter seems to work OK.
    """

    def __init__(self, event, constraint, bv, location):
        super().__init__(location)
        self.event = event
        self.constraint = constraint
        self.fv = event.fv.union(constraint.fv)
        self.bv = [bv[key] for key in bv]
        self.printstring = '(forall ({0}) ({1} => {2}))'.format(' '.join([str(v) for v in self.bv]), str(event), str(constraint))

        self.var_types = []
        self.var_names = []
        for v in self.bv:
            self.var_names.append(v.name)
            yices_type = v.yices_type
            self.var_types.append(yices_type)

        self.space = None

        self.yices_term = self._toYicesTermQ()
        self.yices_string = self._toYicesStringQ()
        #print(self.yices_string)

    # str's goal is to be readable
    def __str__(self):
        return self.printstring


    def init_space(self, maxTimeStamp):
        if self.space is not None:
            self.space.reset()
        origin = []
        bounds = []
        for index, _ in enumerate(self.bv):
            type_range = SymbolTable.get_type_range(self.var_types[index], maxTimeStamp)
            origin.append(type_range[0])
            bounds.append(type_range[1])
        self.space = Space(bounds, origin)


    def toYicesAssertion(self, maxTimeStamp=None):
        if maxTimeStamp is not None:
            return '(assert {0})\n'.format(self.toYicesStringQF(maxTimeStamp))
        return '(assert {0})\n'.format(self.yices_string)

    def toYicesTerm(self, maxTimeStamp=None):
        if maxTimeStamp is not None:
            return self._toYicesTermQF(maxTimeStamp)
        return self.yices_term

    def _toYicesTermQ(self):
        variables = [ v.yices_term for v in self.bv ]
        antecedent = self.event.yices_term
        consequent = self.constraint.yices_term
        body = Terms.ite(antecedent, consequent, Terms.TRUE)
        return Terms.forall(variables, body)

    def _toYicesTermQF(self, maxTimeStamp):
        variables = [ v.yices_term for v in self.bv ]
        antecedent = self.event.yices_term
        consequent = self.constraint.yices_term
        conjuncts = []
        body = Terms.ite(antecedent, consequent, Terms.TRUE)
        #Terms.print_to_fd(1, body, 120, 40, 0)
        self.init_space(maxTimeStamp)
        while not self.space.finished():
            point = self.space.nextElement()
            values = []
            for index, elem in enumerate(point):
                values.append(SymbolTable.get_type_element_as_yices_term(elem, self.var_types[index]))
            conjunct = Terms.subst(variables, values, body)
            #Terms.print_to_fd(1, conjunct, 120, 40, 0)
            conjuncts.append(conjunct)
        return Terms.yand(conjuncts)


    def toYicesStringQF(self, maxTimeStamp):
        sb = StringBuilder()
        antecedent = self.event.yices_string
        consequent = self.constraint.yices_string
        self.init_space(maxTimeStamp)
        sb.append('(and ')
        while not self.space.finished():
            point = self.space.nextElement()
            bindings = StringBuilder()
            bindings.append('(')
            for index, elem in enumerate(point):
                if index > 0:
                    bindings.append(' ')
                bindings.append('(').append(self.var_names[index]).append(' ').append(SymbolTable.get_type_element_as_string(elem, self.var_types[index])).append(')')
            bindings.append(')')
            sb.append('(let ').append(bindings).append(' (if ').append(antecedent)
            sb.append(' ')
            sb.append(consequent)
            sb.append(' ')
            sb.append('true')
            sb.append(')')
            sb.append(')\n')
        sb.append(')') #(and
        return str(sb)

    def _toYicesStringQ(self):
        sb = StringBuilder()
        first = True
        antecedent = self.event.yices_string
        consequent = self.constraint.yices_string
        sb.append('(forall (')
        for v in self.bv:
            if not first:
                sb.append(' ')
            else:
                first = False
            sb.append(v.name)
            sb.append(' :: ')
            sb.append(v.vartype.name)

        sb.append(') ')
        sb.append('(if (and ')
        for v in self.bv:
            sb.append(v.toConstraintString(SymbolTable.MAXTIME))
            sb.append(' ')
        sb.append(antecedent)
        sb.append(')')
        sb.append(' ')
        sb.append(consequent)
        sb.append(' ')
        sb.append('true')
        sb.append(')')
        sb.append(')')
        return str(sb)


class Timeline(SyntacticOccurrence):

    def __init__(self, term, varlist, location):
        super().__init__(location)
        self.term = term
        self.varlist = varlist
        self.printstring = 'timeline({0}, {1})'.format(str(self.term), [str(var) for var in self.varlist])
        self.fv = set(self.varlist)
        self.length = len(varlist)
        self.yices_string = self._toYices()
        self.yices_term = self._toYicesTerm()

    # str's goal is to be readable
    def __str__(self):
        return self.printstring

    def _toYices(self):
        sb = StringBuilder()
        sb.append('(and ')
        for i in range(1, len(self.varlist)):
            sb.append('(< ').append(self.varlist[i -1].toYices()).append(' ').append(self.varlist[i].toYices()).append(')')
        sb.append(')')
        return str(sb)

    def _toYicesTerm(self):
        return self.toYicesTerm()

    def toYicesTerm(self, interpretation=None, height=None):
        if interpretation is None:
            interpretation = Configuration.timeline_interpretation
        else:
            assert interpretation <= 3
        if height is None:
            height = self.length + 1
        if interpretation == 0:
            return Terms.TRUE
        if interpretation == 1:
            return self.toYicesTermDistinct(height)
        if interpretation == 2:
            return self.toYicesTermNondecreasing(height)
        if interpretation == 3:
            return self.toYicesTermAscending(height)
        return None


    def toYicesTermDistinct(self, height):
        args = []
        varlist = self.varlist[0:height]
        for v in varlist:
            yv = v.toYicesTerm()
            args.append(yv)
        yterm = Terms.distinct(args)
        assert yterm is not None
        return yterm

    def toYicesTermAscending(self, height):
        retval = []
        args = []
        varlist = self.varlist[0:height]
        for v in varlist:
            yv = v.toYicesTerm()
            args.append(yv)
        for i, yarg in enumerate(args):
            if i > 0:
                yterm = Terms.arith_lt_atom(args[i - 1], yarg)
                assert yterm is not None
                retval.append(yterm)
        return Terms.yand(retval)

    def toYicesTermNondecreasing(self, height):
        retval = []
        args = []
        varlist = self.varlist[0:height]
        for v in varlist:
            yv = v.toYicesTerm()
            args.append(yv)
        for i, yarg in enumerate(args):
            if i > 0:
                yterm = Terms.arith_leq_atom(args[i - 1], yarg)
                assert yterm is not None
                retval.append(yterm)
        return Terms.yand(retval)

    def toYicesTermIncrementally(self, level):
        assert level in range(1, 4)
        retval = []
        if level >= 1:
            yterm = self.toYicesTermDistinct(height=None)
            retval.append(yterm)
        if level >= 2:
            yterm = self.toYicesTermAscending(height=None)
            retval.append(yterm)
        return Terms.yand(retval)

    def toYicesAssertion(self):
        return '(assert {0})\n'.format(self._toYices())



class Term(SyntacticOccurrence):

    def __init__(self, function, args, location):
        super().__init__(location)
        self.function = function
        self.args = args
        self.printstring = self.toString()
        self.fv = set()
        for arg in self.args:
            if isinstance(arg, SyntacticOccurrence):
                self.fv.update(arg.fv)
        self.yices_string = self._toYicesString()
        self.yices_term = self._toYicesTerm()

    # str's goal is to be readable
    def __str__(self):
        return self.printstring


    def _toYicesString(self):
        sb = StringBuilder()
        sb.append('(')
        sb.append(self.function)
        for term in self.args:
            sb.append(' ')
            sb.append(term.yices_string)
        sb.append(')')
        return str(sb)

    def _toYicesTerm(self):
        try:
            op = self.function.yices_term
            assert op is not None
            args = []
            for arg in self.args:
                assert arg.yices_term is not None
                args.append(arg.yices_term)
            return op(args)
        except Exception as e:
            print('Term._toYicesTerm: ', self, self.function, op, args, e)
            return None

    def toString(self):
        sb = StringBuilder()
        sb.append(self.function)
        sb.append('(')
        first = True
        for term in self.args:
            if first:
                first = False
            else:
                sb.append(', ')
            sb.append(str(term))
        sb.append(')')
        return str(sb)


    def toYicesTheory3(self, sb, op, arg0, arg1, arg2):
        if sb is not None:
            sb.append('(').append(op.toYices()).append(' ').append(arg0).append(' ')
            sb.append(arg1).append(' ').append(arg2).append(')')

    def toYicesTheory2(self, sb, op, arg0, arg1):
        if sb is not None:
            sb.append('(').append(op.toYices()).append(' ').append(arg0).append(' ')
            sb.append(arg1).append(')')


    def toYicesAssertion(self):
        return '(assert {0})\n'.format(self.yices_string)

class Variable(SyntacticOccurrence):

    def __init__(self, name, vartype, location, typename, bound_variables = None):
        super().__init__(location)
        assert typename is not None
        self.name = sys.intern(str(name))
        # currently this is the Maude type we read in when parsing
        self.vartype = vartype
        # in contrast to the above this is the yices type that we use to constrain it range.
        # it is a plain string (since mostly the actual type will be Types.INT)
        self.yices_type = typename
        self.printstring = '{0}:{1}'.format(self.name, self.vartype)
        self.bound = False
        # this will (re)set the bound flag if it is indeed bound
        self.yices_term = YicesSignature.declare_variable(self, bound_variables)
        assert self.yices_term is not None
        self.yices_string = self.name
        self.fv = set()
        self.fv.add(self)

    # str's goal is to be readable
    def __str__(self):
        return self.printstring

    def toYices(self):
        return self.name

    def toYicesTerm(self):
        return self.yices_term

    def toConstraintTerm(self, maxTimeStamp=None):

        if self.name == SymbolTable.MAXTIME:
            assert maxTimeStamp is not None
            yterm = Terms.get_by_name(SymbolTable.MAXTIME)
            assert yterm is not None
            return Terms.eq(yterm, YicesSignature.integer(maxTimeStamp))

        def constrainVariable(maxValue):
            if maxValue is not None:
                ymax = None
                if maxValue == SymbolTable.MAXTIME:
                    ymax = Terms.get_by_name(SymbolTable.MAXTIME)
                else:
                    ymax = YicesSignature.integer(maxValue)

                yterms = [ Terms.arith_leq_atom(YicesSignature.integer(0), self.yices_term),
                           Terms.arith_leq_atom(self.yices_term, ymax) ]
                return Terms.yand(yterms)
            return Terms.arith_leq_atom(YicesSignature.integer(0), self.yices_term)

        if self.vartype.name == SymbolTable.TIME:
            return constrainVariable(SymbolTable.MAXTIME)
        if self.vartype.name == SymbolTable.STAGE:
            return constrainVariable(Configuration.stage_count - 1)
        if self.vartype.name == SymbolTable.NAT:
            if self.yices_type == SymbolTable.BINDEX:
                return constrainVariable(Configuration.bot_count - 1)
            if self.yices_type == SymbolTable.OBINDEX:
                return constrainVariable(Configuration.obs_count - 1)
            if self.yices_type == SymbolTable.XAXIS:
                return constrainVariable(Configuration.grid_dimension[0] - 1)
            if self.yices_type == SymbolTable.YAXIS:
                return constrainVariable(Configuration.grid_dimension[1] - 1)
        return None


    def toConstraintString(self, maxTimeStamp=None):

        retval = None

        if self.name == SymbolTable.MAXTIME:
            assert maxTimeStamp is not None
            return '(= {0} {1})'.format(SymbolTable.MAXTIME, maxTimeStamp)

        def constrainVariable(maxValue):
            sb = StringBuilder()
            sb.append('(and (<= 0 ').append(self.name).append(')')
            if maxValue is not None:
                sb.append(' (<= ').append(self.name).append(' ').append(maxValue).append(')')
            sb.append(')')
            return str(sb)

        if self.vartype.name == SymbolTable.TIME:
            retval = constrainVariable(SymbolTable.MAXTIME)
        elif self.vartype.name == SymbolTable.STAGE:
            retval = constrainVariable(Configuration.stage_count - 1)
        elif self.vartype.name == SymbolTable.NAT:
            if self.yices_type == SymbolTable.BINDEX:
                retval = constrainVariable(Configuration.bot_count - 1)
            elif self.yices_type == SymbolTable.OBINDEX:
                retval = constrainVariable(Configuration.obs_count - 1)
            elif self.yices_type == SymbolTable.XAXIS:
                retval = constrainVariable(Configuration.grid_dimension[0])
            elif self.yices_type == SymbolTable.YAXIS:
                retval = constrainVariable(Configuration.grid_dimension[1])

        return retval




    def toConstraint(self, sb, maxTimeStamp):
        sb.append('(define ').append(self.name).append(' :: ').append(self.vartype).append(')\n')

        constraint = self.toConstraintString(maxTimeStamp)

        if constraint is not None:
            sb.append('(assert ').append(constraint).append(')\n')


class Operation(SyntacticOccurrence):

    def __init__(self, name, location):
        super().__init__(location)
        self.name = name
        self.printstring = name
        self.fv = set()
        self.signature = YicesSignature.signature_map[name]
        assert self.signature is not None
        # not an int but a closure that does the right thing
        self.yices_term = YicesSignature.get_yices_op(name)
        assert self.yices_term is not None
        self.yices_string = name

    # str's goal is to be readable
    def __str__(self):
        return self.printstring

    def toYices(self):
        return self.name

class Type(SyntacticOccurrence):

    def __init__(self, name, location):
        super().__init__(location)
        self.name = name
        self.printstring = name
        self.fv = set()
        self.yices_term = YicesSignature.get_yices_type(name)
        assert self.yices_term is not None
        self.yices_string = name

    # str's goal is to be readable
    def __str__(self):
        return self.printstring

    def toYices(self):
        return self.name



class Integer(SyntacticOccurrence):

    def __init__(self, valuestr, typestr, location):
        super().__init__(location)
        self.value = int(valuestr)
        self.printstring = valuestr
        self.fv = set()
        self.yices_term = YicesSignature.integer(self.value)
        self.yices_string = valuestr
        self.typestr = typestr

    # str's goal is to be readable
    def __str__(self):
        return self.printstring

    def toYices(self):
        return self.yices_string
