
from __future__ import print_function

import sys

from yices.Context import Context
from yices.Model import Model
from yices.Terms import Terms
from yices.Status import Status
from yices.Yices import Yices

from .Configuration import Configuration
from .SymbolTable import SymbolTable
#from .Semantics import Semantics
from .Syntax import YicesSignature
from .Space import Space

from ..util.StringBuffer import StringBuffer
from ..util.Util import string2File


DEBUG = False

#smt_stat = self.context.check_context()
#if smt_stat != Status.SAT:
#    print('No solution: smt_stat = {0}\n'.format(smt_stat))

def yassert_formula(solver, formula):
    if DEBUG:
        Terms.print_to_fd(1, formula, 120, 40, 0)
    errcode = solver.context.assert_formula(formula)
    if DEBUG:
        smt_stat = solver.context.check_context()
        if smt_stat != Status.SAT:
            print('Not SAT: {0}\n'.format(smt_stat))
    return errcode

def yassert_formulas(solver, formulas):
    if DEBUG:
        for formula in formulas:
            Terms.print_to_fd(1, formula, 120, 40, 0)
    errcode = solver.context.assert_formulas(formulas)
    if DEBUG:
        smt_stat = solver.context.check_context()
        if smt_stat != Status.SAT:
            print('Not SAT: {0}\n'.format(smt_stat))
    return errcode



class Solver(object):

    def __init__(self, diagram, protocol, verbose):
        self.diagram = diagram
        self.protocol = protocol
        self.verbose = verbose
        self.maxTimeStamp = diagram.max_timestamp
        print('Maximum time = {0}'.format(self.maxTimeStamp))
        self.context = Context()
        # assert that (b i) = b_i and (pt x y) = pt_x_y
        yassert_formulas(self, YicesSignature.toYicesTerms())


    def addFacts(self):
        if not self.addModel():
            return False
        self.protocol.constrainVariablesAPI(self.context)
        if not self.addProtocol():
            return False
        return True

    def addModel(self):
        # The last argument indicates that the theory should be completed.
        # Anything not asserted is asserted to be False.
        assertions = self.diagram.toYicesTerms(point=None, completeMe=True)
        if assertions is None:
            assertions = []
        retval =  yassert_formulas(self, assertions)
        if not retval:
            sys.stderr.write('addModel() failed\n')
        return retval

    def addProtocol(self):
        assertions = self.protocol.toYicesTerms(None, None, self.maxTimeStamp)
        if assertions is None:
            assertions = []
        retval = yassert_formulas(self, assertions)
        if not retval:
            sys.stderr.write('addProtocol() failed\n')
        return retval


    def getProtocolIncrementally(self, level):
        return self.protocol.toYicesTermsIncrementally(level)

    def writeTheory(self, theory_file):
        sb = StringBuffer()
        SymbolTable.toYices(sb)
        self.diagram.toYices(sb, None, True)
        self.protocol.toYices(sb, self.maxTimeStamp, False)
        theory = str(sb)
        string2File(theory, theory_file, False)
        string2File("(check)\n(show-model)\n", theory_file, True)



    def consistency_check(self):
        assertions = self.diagram.toYicesTerms(point=None, completeMe=True)
        alen = len(assertions)
        if alen:
            smt_stat = self.context.check_context_with_assumptions(None, assertions)
            sys.stderr.write('context.check_context_with_assumptions returned {0}\n'.format(Status.name(smt_stat)))
            if smt_stat == Status.SAT:
                #sys.stderr.write('Calling unsat_core on a satisfiable theory is user error\n')
                retcode = 0
            elif smt_stat == Status.UNSAT:
                unsat_core = self.context.get_unsat_core()
                if not unsat_core:
                    sys.stderr.write('unsat_core is empty\n')
                else:
                    print("\nUnsat core:\n")
                    for term in unsat_core:
                        Terms.print_to_fd(1, term, 80, 100, 0)
                    print("\n")
            else:
                retcode = 1
            retcode = 0
        self._cleanUp()
        return retcode


    # a retcode of 0 means the problem is SAT
    # a retcode of 1 means the problem is UNSAT
    # a retcode of 2 means there was an error somewhere
    def solve(self, theory_file):
        retcode = 2
        if not self.addFacts():
            return retcode
        if theory_file is not None:
            self.writeTheory(theory_file)
        smt_stat = self.context.check_context()
        if smt_stat != Status.SAT:
            print('No solution: smt_stat = {0}\n'.format(smt_stat))
            retcode = 1
        else:
            print('\nSatisfiable.')
            #get the model
            model = Model.from_context(self.context, 1)
            self.print_solution(model)
            model.dispose()
            retcode = 0
        self._cleanUp()
        return retcode




    def incrementally_solve(self):
        retcode = 2
        if not self.addModel():
            return retcode
        self.protocol.constrainVariablesAPI(self.context)
        if self.context.status() == Status.UNSAT:
            print('The model appears to be UNSAT: smt_stat = {}\n'.format(self.context.status()))
            print('For more information use the --consistency option.\n')
            return retcode
        # The meaning of the levels:
        #
        # 0.  Just the events
        # 1.  The events plus the distinctness of each timeline:  distinct(varlist) for timeline(bot, varlist) in facts.
        # 2.  The events plus the ascendingness of each timeline
        for level in range(0, 4):
            #print('context status: ', Status.name(self.context.status()))
            self.context.push()
            assertions = self.getProtocolIncrementally(level)
            alen = len(assertions)
            if alen:
                smt_stat = self.context.check_context_with_assumptions(None, assertions)
                sys.stderr.write('Level {0}: context.check_context_with_assumptions returned {1}\n'.format(level, Status.name(smt_stat)))
                if smt_stat == Status.SAT:
                    #get the model
                    model = Model.from_context(self.context, 1)
                    print('Level {0} has a solution: smt_stat = {1}\n'.format(level, smt_stat))
                    self.print_solution(model)
                    model.dispose()
                elif smt_stat == Status.UNSAT:
                    unsat_core = self.context.get_unsat_core()
                    if not unsat_core:
                        sys.stderr.write('unsat_core is empty\n')
                    else:
                        print('Level {0} unsat core is:\n'.format(level))
                        for term in unsat_core:
                            Terms.print_to_fd(1, term, 80, 100, 0)
                        print('')
                    return 0
                else:
                    sys.stderr.write('context.check_context_with_assumptions returned {0}\n'.format(Status.name(smt_stat)))
            self.context.pop()
        self._cleanUp()
        return 0


    def exhaust(self):
        result = 0
        self.context.push()
        if not self.addFacts():
            print('Bummer')
            return 2
        # BD says: this is complete but crude
        # another way would be to use 'yices_assert_blocking_clause'
        while  self.context.check_context() == Status.SAT:
            model = Model.from_context(self.context, 1)
            self.print_solution(model, 'Model #{0}:'.format(result))
            diagram = YicesSignature.model2term(model)
            self.context.assert_formula(Terms.ynot(diagram))
            model.dispose()
            result += 1
            if result == Configuration.aleph_nought:
                break
        self.context.pop()
        print("I found {1} distinct model{2} (using an upper limit of {0})".format(Configuration.aleph_nought, result, "" if result == 1 else "s"))
        return result



    def unsat_core(self):
        retcode = 2
        if not self.addModel():
            sys.stderr.write('addModel failed\n')
            return retcode
        self.protocol.constrainVariablesAPI(self.context)
        smt_stat = self.context.check_context()
        #sys.stderr.write('context.check_context returned {0}\n'.format(Status.name(smt_stat)))
        if smt_stat == Status.UNSAT:
            sys.stderr.write('The model is UNSAT: something is rotten in the State\n')
            retcode = 1
            return retcode
        assertions = self.protocol.toYicesTerms()
        alen = len(assertions)
        if alen:
            smt_stat = self.context.check_context_with_assumptions(None, assertions)
            sys.stderr.write('context.check_context_with_assumptions returned {0}\n'.format(Status.name(smt_stat)))
            if smt_stat == Status.SAT:
                sys.stderr.write('Calling unsat_core on a satisfiable theory is user error\n')
                retcode = 1
            elif smt_stat == Status.UNSAT:
                unsat_core = self.context.get_unsat_core()
                if not unsat_core:
                    sys.stderr.write('unsat_core is empty\n')
                else:
                    for term in unsat_core:
                        Terms.print_to_fd(1, term, 80, 100, 0)
            else:
                retcode = 1
            retcode = 0
        self._cleanUp()
        return retcode


    def missing(self):
        retcode = 2
        if not self.addModel():
            sys.stderr.write('addModel failed\n')
            return retcode
        self.protocol.constrainVariablesAPI(self.context)
        timelines = self.protocol.timelines
        tlen = len(timelines)
        interpretation = Configuration.timeline_interpretation
        tint_text = Configuration.INTERPRETATIONS[interpretation]
        print('There are {0} timelines ({1})\n'.format(tlen, tint_text))
        if not timelines:
            return retcode
        for timeline in timelines:
            formula = timeline.toYicesTerm(interpretation)
            yassert_formula(self, formula)
        smt_stat = self.context.check_context()
        if smt_stat == Status.UNSAT:
            sys.stderr.write('The model is UNSAT: something is rotten in the State\n')
            retcode = 1
            return retcode
        for timeline in timelines:
            satisfiable = True
            yevents = [ ]
            for eindex, timevar in enumerate(timeline.varlist):
                events = self.protocol.event_map[timevar]
                for e in events:
                    yevents.append(e.yices_term)
                smt_stat = self.context.check_context_with_assumptions(None, yevents)
                if smt_stat == Status.UNSAT:
                    satisfiable = False
                    print('UNSAT at level {0}, i.e. timestamp {1}'.format(eindex, timevar))
                    unsat_core = self.context.get_unsat_core()
                    print("\nUnsat core :\n")
                    for term in unsat_core:
                        Terms.print_to_fd(1, term, 80, 100, 0)
                    print("\n")
                    break
                elif self.verbose and smt_stat == Status.SAT:
                    print('SAT at level {0}, i.e. timestamp {1}'.format(eindex, timevar))
                    model = Model.from_context(self.context, 1)
                    self.print_solution(model, header=None, frees=timeline.fv)
                    model.dispose()
            if satisfiable:
                print('Timeline of {0} OK ({1}):\n'.format(timeline.term, tint_text))  #print a model
                model = Model.from_context(self.context, 1)
                self.print_solution(model, header=None, frees=timeline.fv)
                model.dispose()
        retcode = 0
        self._cleanUp()
        return retcode



    def print_solution(self, model, header=None, frees=None):

        def print_int(v):
            ytvar = v.yices_term
            ytval = model.get_value(ytvar)
            print('\t{0} is {1}'.format(v.name, ytval))


        if header is not None:
            print(header)

        if frees is None:
            nv = YicesSignature.get_vars(SymbolTable.NAT)
            for nvar in nv:
                print_int(nvar)
            tv = YicesSignature.get_vars(SymbolTable.TIME)
            for tvar in tv:
                if tvar.name == SymbolTable.MAXTIME:
                    continue
                print_int(tvar)
            pv = YicesSignature.get_vars(SymbolTable.PT2)
            for ptvar in pv:
                if ptvar.name == SymbolTable.NOLOC:
                    continue
                ytvar = ptvar.yices_term
                ytval = model.get_value(ytvar)
                val = YicesSignature.pt2_invmap[ytval]
                print('\t{0} is {1}'.format(ptvar.name, val))
        else:
            frees = list(frees)
            frees.sort()
            for var in frees:
                ytvar = var.yices_term
                ytval = model.get_value(ytvar)
                if var.vartype.name == 'Pt2':
                    ytval = YicesSignature.pt2_invmap[ytval]
                print('\t{0} is {1}'.format(var.name, ytval))


    def frontier(self):
        retcode = 2
        if not self.addModel():
            return retcode
        self.protocol.constrainVariablesAPI(self.context)
        searchSpace = Frontier(self.protocol)
        interpretation = Configuration.timeline_interpretation
        tint_text = Configuration.INTERPRETATIONS[interpretation]
        print('The timeline interpretation is: {0}\n'.format(tint_text))
        while not searchSpace.finished():
            point = searchSpace.nextElement()
            if point is None:
                break
            if self.verbose:
                print(point)
            assertions = self.protocol.toYicesTerms(point)
            alen = len(assertions)
            if alen:
                smt_stat = self.context.check_context_with_assumptions(None, assertions)
                if smt_stat == Status.SAT:
                    if self.verbose:
                        print('SAT')
                        #get the model
                        model = Model.from_context(self.context, 1)
                        self.print_solution(model, header=None, frees=self.protocol.FV(point))
                        model.dispose()
                elif smt_stat == Status.UNSAT:
                    searchSpace.addUnsat(point)
                    if self.verbose:
                        print('UNSAT')
                        unsat_core = self.context.get_unsat_core()
                        print("\nUnsat core:\n")
                        for term in unsat_core:
                            Terms.print_to_fd(1, term, 80, 100, 0)
                        print("\n")
            else:
                sys.stderr.write('context.check_context_with_assumptions returned {0}\n', smt_stat)
        print('Frontier: {0}'.format(searchSpace.frontier))
        self._cleanUp()
        return retcode


    def entire(self):
        retcode = 2
        if not self.addModel():
            return retcode
        self.protocol.constrainVariablesAPI(self.context)
        searchSpace = Frontier(self.protocol)
        tower = list(searchSpace.tower())
        tower.sort()
        for point in tower:
            print(point)
            assertions = self.protocol.toYicesTerms(point)
            alen = len(assertions)
            if alen:
                smt_stat = self.context.check_context_with_assumptions(None, assertions)
                if smt_stat == Status.SAT:
                    print('SAT')
                    #get the model
                    model = Model.from_context(self.context, 1)
                    self.print_solution(model, header=None, frees=self.protocol.FV(point))
                    model.dispose()
                elif smt_stat == Status.UNSAT:
                    print('UNSAT')
                    unsat_core = self.context.get_unsat_core()
                    print("\nUnsat core:\n")
                    for term in unsat_core:
                        Terms.print_to_fd(1, term, 80, 100, 0)
                    print("\n")
                else:
                    sys.stderr.write('context.check_context_with_assumptions returned {0}\n', smt_stat)
        self._cleanUp()
        return retcode




    def _cleanUp(self):
        self.context.dispose()
        Yices.exit()


class Frontier(object):

    def __init__(self, facts):
        self.frontier = set()
        self.unsat = set()
        self.search_space = Space(self.compute_dimension(facts))


    def compute_dimension(self, facts):
        N = len(facts.timelines)
        assert N > 0
        dimension = [None] * N
        for i in range(N):
            dimension[i] = facts.timelines[i].length
        return dimension


    def finished(self):
        return self.search_space.finished()

    def nextElement(self):
        while True:
            elem = self.search_space.nextElement()
            if elem is None or not elem in self.unsat:
                return elem

    def addUnsat(self, elem):
        self.frontier.add(elem)
        tower = self.tower(elem)
        self.unsat.update(tower)


    # computes the set of all tuples above point.
    def tower(self, point=None):
        return self.search_space.tower(point)
