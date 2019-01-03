import sys

from yices.Terms import Terms

from ..crap.py import deviation_intern

from .Configuration import Configuration


class SymbolTable(object):


    # operations
    ATLOC         = deviation_intern('atloc')
    TREATSTAGE    = deviation_intern('treatStage')
    PT            = deviation_intern('pt')
    B             = deviation_intern('b')
    OB            = deviation_intern('ob')
    NOLOC         = deviation_intern('noLoc')


    # constraint operations
    LT            = deviation_intern('<')
    LEQ           = deviation_intern('<=')
    GT            = deviation_intern('>')
    GEQ           = deviation_intern('>=')
    EQ            = deviation_intern('=')
    NEQ           = deviation_intern('/=')
    ADD           = deviation_intern('+')
    MINUS         = deviation_intern('-')
    MUL           = deviation_intern('*')
    ABS           = deviation_intern('abs')

    #types
    ATOM          = deviation_intern('Atom')  # a wild card for the lhs and rhs of the infix boolean operations
    BOOL          = deviation_intern('Bool')
    NAT           = deviation_intern('Nat')
    TIME          = deviation_intern('Time')
    PT2           = deviation_intern('Pt2')
    THING         = deviation_intern('Thing')  # a bot or an obstacle
    STAGE         = deviation_intern('Stage')

    #pseudo types (used as the yices_type field of variables to indicate sutype of Nat)
    BINDEX        = deviation_intern('BI')
    OBINDEX       = deviation_intern('OBI')
    XAXIS         = deviation_intern('X')
    YAXIS         = deviation_intern('Y')


    @staticmethod
    def get_type_range(yices_type, maxTimeStamp):
        if yices_type == SymbolTable.TIME:
            return (0, maxTimeStamp)
        if yices_type == SymbolTable.PT2:
            return (0, Configuration.pt2_count)
        if yices_type == SymbolTable.XAXIS:
            return (0, Configuration.grid_dimension[0])
        if yices_type == SymbolTable.YAXIS:
            return (0, Configuration.grid_dimension[1])
        if yices_type == SymbolTable.STAGE:
            return (0, Configuration.stage_count)
        if yices_type == SymbolTable.BINDEX:
            return (0, Configuration.bot_count)
        if yices_type == SymbolTable.OBINDEX:
            return (0, Configuration.obs_count)
        sys.stderr.write('SymbolTable.get_type_range: unrecognized type {0}\n'.format(yices_type))
        return None

    @staticmethod
    def get_type_element_as_string(i, yices_type):
        if yices_type == SymbolTable.TIME:
            return str(i)
        if yices_type == SymbolTable.PT2:
            return SymbolTable.pt2_name(i)
        if yices_type == SymbolTable.XAXIS:
            return str(i)
        if yices_type == SymbolTable.YAXIS:
            return str(i)
        if yices_type == SymbolTable.STAGE:
            return str(i)
        if yices_type == SymbolTable.BINDEX:
            return SymbolTable.bot_name(i)
        if yices_type == SymbolTable.OBINDEX:
            return  SymbolTable.obs_name(i)
        sys.stderr.write('SymbolTable.get_type_element_as_string: unrecognized type {0}\n'.format(yices_type))
        return None

    @staticmethod
    def get_type_element_as_yices_term(i, yices_type):
        if yices_type == SymbolTable.TIME:
            return Terms.integer(i)
        if yices_type == SymbolTable.PT2:
            return Terms.get_by_name(SymbolTable.pt2_name(i))
        if yices_type == SymbolTable.XAXIS:
            return Terms.integer(i)
        if yices_type == SymbolTable.YAXIS:
            return Terms.integer(i)
        if yices_type == SymbolTable.STAGE:
            return Terms.integer(i)
        if yices_type == SymbolTable.BINDEX:
            return Terms.get_by_name(SymbolTable.bot_name(i))
        if yices_type == SymbolTable.OBINDEX:
            return  Terms.get_by_name(SymbolTable.obs_name(i)) # could do all enums like this
        sys.stderr.write('SymbolTable.get_type_element_as_string: unrecognized type {0}\n'.format(yices_type))
        return None



    # the maximum timestamp

    MAXTIME  =  deviation_intern('maxTime')

    #maude mismatches
    MAUDE_NEQ     = deviation_intern('=/=')


    translate     = { MAUDE_NEQ: NEQ }


    # binary boolean operations
    BINOPS = (LT, LEQ, GT, GEQ, EQ, NEQ)

    # infix arithmetic operations
    INFIX = (ADD, MINUS, MUL)

    binop_map = {
        LT:  Terms.arith_lt_atom,
        LEQ: Terms.arith_leq_atom,
        GT:  Terms.arith_gt_atom,
        GEQ: Terms.arith_geq_atom,
        EQ:  Terms.eq,
        NEQ: Terms.neq,
    }

    infix_map = {
        ADD:   Terms.add,
        MINUS: Terms.sub,
        MUL:   Terms.mul,
        }


    symbol_table = {

        #operations
        ATLOC:           ATLOC,
        TREATSTAGE:      TREATSTAGE,
        PT:              PT,
        B:               B,
        OB:              OB,
        NOLOC:           NOLOC,
        LT:              LT,
        LEQ:             LEQ,
        GT:              GT,
        GEQ:             GEQ,
        NEQ:             NEQ,
        EQ:              EQ,
        ADD:             ADD,
        MINUS:           MINUS,
        MUL:             MUL,
        ABS:             ABS,

        #types
        TIME:            TIME,
        PT2:             PT2,
        THING:           THING,
        STAGE:           STAGE,
        NAT:             NAT,

        #translations
        MAUDE_NEQ: NEQ,

        #maximum timestamp
        MAXTIME: MAXTIME,
    }

    @staticmethod
    def bot_name(i):
        return 'b{0}'.format(i)

    @staticmethod
    def obs_name(i):
        return 'ob{0}'.format(i)

    @staticmethod
    def thing_names():
        bots = [ SymbolTable.bot_name(i) for i in range(0, Configuration.bot_count) ]
        obstacles = [ SymbolTable.obs_name(i) for i in range(0, Configuration.obs_count) ]
        bots.extend(obstacles)
        return bots

    @staticmethod
    def pt2_name(i):
        return 'pt_{0}_{1}'.format(i/Configuration.grid_dimension[1], i % Configuration.grid_dimension[1])

    @staticmethod
    def pt2_names():
        return [ SymbolTable.pt2_name(i) for i in range(0, Configuration.pt2_count) ]

    @staticmethod
    def canonicalize(name):
        retval = SymbolTable.symbol_table.get(name)
        if retval is None:
            sys.stderr.write('Warning: {0} not in the SymbolTable\n'.format(name))
        return retval

    @staticmethod
    def scalar2Yices(sb, name, count, elements):
        sb.append('(define-type ').append(name).append(' (scalar ')
        for i in range(0, count):
            sb.append(elements[i])
            if i < count - 1:
                sb.append(' ')
        sb.append('))\n')

    @staticmethod
    def ops2Yices(sb):
        sb.append('(define b :: (-> BI Thing))\n')
        sb.append('(define ob :: (-> OBI Thing))\n')
        sb.append('(define pt :: (-> X Y Pt2))\n')
        sb.append('(define atloc :: (-> Thing Pt2 Time bool))\n')
        sb.append('(define treatStage :: (-> Pt2 Stage Time bool))\n')

    @staticmethod
    def toYices(sb):
        SymbolTable.scalar2Yices(sb, SymbolTable.THING, Configuration.thing_count, SymbolTable.thing_names())
        SymbolTable.scalar2Yices(sb, SymbolTable.PT2, Configuration.pt2_count, SymbolTable.pt2_names())
        sb.append('(define-type Stage int)\n')
        sb.append('(define-type Time int)\n')
        sb.append('(define-type BI int)\n')
        sb.append('(define-type OBI int)\n')
        sb.append('(define-type X int)\n')
        sb.append('(define-type Y int)\n')
        sb.append('(define-type Nat int)\n')
        SymbolTable.ops2Yices(sb)
        SymbolTable.enums2Yices(sb)

    @staticmethod
    def enums2Yices(sb):
        for i in range(0, Configuration.bot_count):
            sb.append('(assert (= (b {0}) b{0}))\n'.format(i))
        for x in range(0, Configuration.grid_dimension[0]):
            for y in range(0, Configuration.grid_dimension[1]):
                sb.append('(assert (= (pt {0} {1}) pt_{0}_{1}))\n'.format(x, y))
