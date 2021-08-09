from __future__ import print_function

import sys


from yices.Terms import Terms

import deviation.logic.Syntax as Syntax

from .Configuration import Configuration
from .SymbolTable import SymbolTable
from .YicesSignature import YicesSignature

#from .Semantics import Semantics

class State:
    """ The State object is used to complete the logs.


    """

    inited    = False
    bots      = []   #None
    obstacles = []   #None
    pts       = []   #None
    stages    = []   #None


    @staticmethod
    def init():
        if not State.inited:
            State.inited = True
            State.bots = [ SymbolTable.bot_name(i) for i in range(0, Configuration.bot_count) ]
            State.obstacles = []
            State.pts = [ SymbolTable.pt2_name(i) for i in range(0, Configuration.pt2_count) ]
            State.stages = list(range(0, Configuration.stage_count))



    def __init__(self):
        State.init()
        # maps a bot to it a tuple consisting of its last known location, and when it got there
        self.bot_state = {}
        for b in State.bots:
            self.bot_state[b] = (None, None)
        # maps a pt2 to it a tuple consisting of its last known treatState, and when it got treated
        self.pt_state = {}
        for pt in State.pts:
            self.pt_state[pt] = (None, None)
        self.current_timestamp = None

    def addEvents(self, ts, event_set):
        self.current_timestamp = ts
        if not event_set:
            return
        for ev in event_set:
            assert ts == ev.timestamp.value
            self.addEvent(ev)

    def addEvent(self, ev):
        expr = ev.expression
        op = expr.function.name
        args = expr.args
        if op == SymbolTable.ATLOC:
            thing = args[0]
            if thing.function.name == SymbolTable.B:
                if not isinstance(args[1], Syntax.Variable):
                    bot = Syntax.thingTerm2Yices(args[0])
                    pt = Syntax.pt2Term2Yices(args[1])
                    ts = Syntax.integerTerm2Yices(args[2])
                    self.bot_state[bot] = (pt, ts)
                else:
                    # should not happen any more
                    print('Skipping variable {0}'.format(args[1]))
            elif thing.function.name == SymbolTable.OB:
                pt = Syntax.pt2Term2Yices(args[1])
                self.obstacles.append(pt)
            else:
                print('Unexpected atloc argument {0}'.format(thing))
                return
        elif op == SymbolTable.TREATSTAGE:
            pt = Syntax.pt2Term2Yices(args[0])
            stage = Syntax.integerTerm2Yices(args[1])
            ts = Syntax.integerTerm2Yices(args[2])
            self.pt_state[pt] = (stage, ts)
        else:
            sys.stderr.write('Surprising event: {0}.\n'.format(ev))

    def toYicesTerms(self, ts):
        retval = []

        for botname in self.bots:
            (bot_pt, bot_ts) = self.bot_state[botname]
            all_other_pts = self.pts
            if bot_ts == ts:
                all_other_pts = [ pt for pt in self.pts if pt != bot_pt]
            for ptname in all_other_pts:
                atloc_term = YicesSignature.mkatloc(botname, ptname, self.current_timestamp)
                assert atloc_term is not None
                not_atloc_term = Terms.ynot(atloc_term)
                retval.append(not_atloc_term)

        for ptname in self.pts:
            (pt_stage, pt_ts) = self.pt_state[ptname]
            all_other_stages = self.stages
            if pt_ts == ts:
                all_other_stages = [ stage for stage in self.stages if stage != pt_stage ]
            #Semantics.assert_not_treatstages(context, ptname, all_other_stages, self.current_timestamp)
            for stage in all_other_stages:
                treatstage_term = YicesSignature.mktreatstage(ptname, stage, self.current_timestamp)
                assert treatstage_term is not None
                not_treatstage_term = Terms.ynot(treatstage_term)
                retval.append(not_treatstage_term)

        return retval


    def toYices(self, sb, ts):
        for botname in self.bots:
            (bot_pt, bot_ts) = self.bot_state[botname]
            all_other_pts = self.pts
            if bot_ts == ts:
                all_other_pts = [ pt for pt in self.pts if pt != bot_pt]
            if sb is not None:
                for pt in all_other_pts:
                    sb.append('(assert (not (atloc ').append(botname).append(' ').append(pt).append(' ').append(self.current_timestamp).append(')))\n')
        for ptname in self.pts:
            (pt_stage, pt_ts) = self.pt_state[ptname]
            all_other_stages = self.stages
            if pt_ts == ts:
                all_other_stages = [ stage for stage in self.stages if stage != pt_stage ]
            if sb is not None:
                for stage in all_other_stages:
                    sb.append('(assert (not (treatStage ').append(ptname).append(' ').append(stage).append(' ').append(self.current_timestamp).append(')))\n')
