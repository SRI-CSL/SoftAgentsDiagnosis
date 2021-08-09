import sys

from yices.Terms import Terms

from .Configuration import Configuration


class SymbolTable:


    # operations
    ATLOC         = sys.intern('atloc')
    TREATSTAGE    = sys.intern('treatStage')
    PT            = sys.intern('pt')
    B             = sys.intern('b')
    OB            = sys.intern('ob')
    NOLOC         = sys.intern('noLoc')


    # constraint operations
    LT            = sys.intern('<')
    LEQ           = sys.intern('<=')
    GT            = sys.intern('>')
    GEQ           = sys.intern('>=')
    EQ            = sys.intern('=')
    NEQ           = sys.intern('/=')
    ADD           = sys.intern('+')
    MINUS         = sys.intern('-')
    MUL           = sys.intern('*')
    ABS           = sys.intern('abs')

    #types
    ATOM          = sys.intern('Atom')  # a wild card for the lhs and rhs of the infix boolean operations
    BOOL          = sys.intern('Bool')
    NAT           = sys.intern('Nat')
    TIME          = sys.intern('Time')
    PT2           = sys.intern('Pt2')
    THING         = sys.intern('Thing')  # a bot or an obstacle
    STAGE         = sys.intern('Stage')

    #pseudo types (used as the yices_type field of variables to indicate sutype of Nat)
    BINDEX        = sys.intern('BI')
    OBINDEX       = sys.intern('OBI')
    XAXIS         = sys.intern('X')
    YAXIS         = sys.intern('Y')


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
        sys.stderr.write(f'SymbolTable.get_type_range: unrecognized type {yices_type}\n')
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
        sys.stderr.write(f'SymbolTable.get_type_element_as_string: unrecognized type {yices_type}\n')
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
        sys.stderr.write(f'SymbolTable.get_type_element_as_string: unrecognized type {yices_type}\n')
        return None



    # the maximum timestamp

    MAXTIME  =  sys.intern('maxTime')

    #maude mismatches
    MAUDE_NEQ     = sys.intern('=/=')


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
        return f'b{i}'

    @staticmethod
    def obs_name(i):
        return f'ob{i}'

    @staticmethod
    def thing_names():
        bots = [ SymbolTable.bot_name(i) for i in range(0, Configuration.bot_count) ]
        obstacles = [ SymbolTable.obs_name(i) for i in range(0, Configuration.obs_count) ]
        bots.extend(obstacles)
        return bots

    @staticmethod
    def pt2_name(i):
        return f'pt_{i//Configuration.grid_dimension[1]}_{i % Configuration.grid_dimension[1]}'

    @staticmethod
    def pt2_names():
        return [ SymbolTable.pt2_name(i) for i in range(0, Configuration.pt2_count) ]

    @staticmethod
    def canonicalize(name):
        retval = SymbolTable.symbol_table.get(name)
        if retval is None:
            sys.stderr.write(f'Warning: {name} not in the SymbolTable\n')
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
            sb.append(f'(assert (= (b {i}) b{i}))\n')
        for x in range(0, Configuration.grid_dimension[0]):
            for y in range(0, Configuration.grid_dimension[1]):
                sb.append(f'(assert (= (pt {x} {y}) pt_{x}_{y}))\n')
