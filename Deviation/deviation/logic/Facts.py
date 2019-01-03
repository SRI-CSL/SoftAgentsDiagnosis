from __future__ import print_function

import sys

from .State import State

from .Syntax import Integer

from ..visitor.Visitor import Visitor

class Facts(object):


    def __init__(self):
        # I guess the choice of set was to eliminate duplicates
        self.event_set = set()
        self.event_map = {}
        self.constraints = set()
        self.fv = set()
        self.timestamps = set()
        self.sorted_timestamps = None
        # why not maintain the "no duplicates" methodology?
        self.timelines = []

        self.invariants = set()

        self.non_timeline_fv = None
        self.max_timestamp = None

    def addEvent(self, event):
        self.event_set.add(event)
        ts = event.timestamp
        if isinstance(ts, Integer):
            ts = ts.value
        if not ts in self.event_map:
            self.event_map[ts] = set()
        self.event_map[ts].add(event)

    def addConstraint(self, constraint):
        self.constraints.add(constraint)

    def addInvariant(self, invariant):
        self.invariants.add(invariant)

    def addTimeline(self, timeline):
        self.timelines.append(timeline)

    def addFV(self, variable):
        self.fv.add(variable)

    def addTimeStamp(self, ts):
        if isinstance(ts, Integer):
            value = ts.value
            if (self.max_timestamp) is None or (value > self.max_timestamp):
                self.max_timestamp = value
            self.timestamps.add(value)
        else:
            self.timestamps.add(ts)

    def timeStamps(self):
        if not self.sorted_timestamps:
            self.sorted_timestamps = sorted(self.timestamps)
        return self.sorted_timestamps

    def dump(self):

        if bool(self.event_set):
            print('Event Set:')
            for c in self.event_set:
                print(str(c))

        if bool(self.timelines):
            print('Timelines:')
            for tl in self.timelines:
                print(str(tl))

        if bool(self.constraints):
            print('Constraints:')
            for c in self.constraints:
                print(str(c))

        if bool(self.fv):
            print('FVs:')
            for v in self.fv:
                print(str(v))

        if bool(self.timestamps):
            print('timeStamps:')
            print([ str(ts) for ts in self.timeStamps()])

        if bool(self.invariants):
            print('Invariants:')
            for inv in self.invariants:
                print(str(inv))

    def constrainVariables(self, sb, maxTimeStamp):
        for v in self.fv:
            v.toConstraint(sb, maxTimeStamp)

    def constrainVariablesAPI(self, context):
        for v in self.fv:
            yt = v.toConstraintTerm()
            if yt is not None:
                context.assert_formula(yt)

    def toYices(self, sb, maxTimeStamp=None, completeMe=False):
        # FIXME: still not kosher with the maximum time
        # if we are the log we should assert the max time constraints.
        if completeMe:
            Visitor.MAXTIME.toConstraint(sb, self.max_timestamp)

        self.constrainVariables(sb, maxTimeStamp)
        for ev in self.event_set:
            sb.append(ev.toYicesAssertion())
        for tl in self.timelines:
            sb.append(tl.toYicesAssertion())
        for c in self.constraints:
            sb.append(c.toYicesAssertion())
        for i in self.invariants:
            sb.append(i.toYicesAssertion(maxTimeStamp))

        if completeMe:
            self.completeMe(sb)

    def completeMe(self, sb):
        state = State()
        timestamps = self.timeStamps()
        for ts in range(timestamps[0], timestamps[-1] + 1):
            events = self.event_map.get(ts, None)
            state.addEvents(ts, events)
            state.toYices(sb, ts)

    def completionYicesTerms(self):
        retval = []
        state = State()
        timestamps = self.timeStamps()
        no_events = []
        for ts in range(timestamps[0], timestamps[-1] + 1):
            events = self.event_map.get(ts, None)
            if not events:
                no_events.append(ts)
            state.addEvents(ts, events)
            negations = state.toYicesTerms(ts)
            retval.extend(negations)
        sys.stderr.write('FYI: no events at {0}.\n'.format(no_events))
        return retval


    def toYicesTermsIncrementally(self, level):
        retval = []
        assert level in range(0, 4)
        for ev in self.event_set:
            term  = ev.expression
            yterm = term.yices_term
            assert yterm is not None
            retval.append(yterm)
        if level == 0:
            return retval
        for tl in self.timelines:
            retval.append(tl.toYicesTermIncrementally(level))
        if level < 3:
            return retval
        for c in self.constraints:
            yterm = c.yices_term
            retval.append(yterm)

        return retval



    def toYicesTerms(self, point=None, completeMe=False, maxTimeStamp=None):
        if point is not None:
            assert not completeMe
            return self.toYicesTermsRestricted(point)

        retval = []
        # if we are the log we should assert the max time constraints.
        if completeMe:
            retval.append(Visitor.MAXTIME.toConstraintTerm(self.max_timestamp))

        for ev in self.event_set:
            term  = ev.expression
            yterm = term.yices_term
            assert yterm is not None
            retval.append(yterm)
        if completeMe:
            assert not self.timelines
            assert not self.constraints
            retval.extend(self.completionYicesTerms())
        else:
            for tl in self.timelines:
                retval.append(tl.yices_term)
            for c in self.constraints:
                yterm = c.yices_term
                retval.append(yterm)
            for i in self.invariants:
                retval.append(i.toYicesTerm(maxTimeStamp))

        return retval

    def toYicesTermsRestricted(self, point):
        """ returns the yices terms whose free variables are contained in the initial segments of the timelines given by the point.
        """
        frees = self.FV(point)
        retval = []
        for ev in self.event_set:
            term  = ev.expression
            if term.fv.issubset(frees):
                yterm = term.yices_term
                retval.append(yterm)
        for ti, tl in enumerate(self.timelines):
            height = point[ti] + 1
            retval.append(tl.toYicesTerm(height=height))
        for c in self.constraints:
            if c.fv.issubset(frees):
                yterm = c.yices_term
                retval.append(yterm)
        return retval


    def FV(self, point=None):
        if point is None:
            return self.fv
        # we want to restrict the variables to the
        # timeline levels indicated by point.
        count = len(point)
        assert count == len(self.timelines)
        retval = set()
        for i in range(count):
            for j in range(0, point[i] + 1):
                timeline_var = self.timelines[i].varlist[j]
                events = self.event_map[timeline_var]
                for event in events:
                    retval |= event.fv
        return retval
