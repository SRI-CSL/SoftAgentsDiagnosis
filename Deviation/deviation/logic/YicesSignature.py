import sys

from yices import (Constructor, Terms, Types, Yices)

from .Configuration import Configuration
from .SymbolTable import SymbolTable

class YicesSignature:
    """ Maintains the connection between the Maude language and the Yices2 language.
    """

    # the yices types
    int_type        = Types.INT
    bool_type       = Types.BOOL

    thing_type      = None
    pt2_type        = None
    stage_type      = None  # just Types.INT; probably do not need this if we are careful with types
    time_type       = None  # just Types.INT; probably do not need this if we are careful with types
    nat_type        = None  # just Types.INT; probably do not need this if we are careful with types

    # the yices operation types
    b_type          = None
    ob_type         = None
    pt_type         = None
    atloc_type      = None
    treatstage_type = None

    abs_type        = None

    # a prototype is a tuple: (argument_types, return_type)
    b_prototype          = (None, None)
    ob_prototype         = (None, None)
    pt_prototype         = (None, None)
    atloc_prototype      = (None, None)
    treatstage_prototype = (None, None)
    abs_prototype        = (None, None)

    # the yices terms (operations)
    b_op            = None
    ob_op           = None
    pt_op           = None
    atloc_op        = None
    treatstage_op   = None

    abs_op          = None

   # maps a type name to the list of variables of that type
    types_to_variables = {
        SymbolTable.NAT           : set(),
        SymbolTable.TIME          : set(),
        SymbolTable.PT2           : set(),
        SymbolTable.THING         : set(),
        SymbolTable.STAGE         : set(),
        SymbolTable.BINDEX        : set(),
        SymbolTable.OBINDEX       : set(),
        SymbolTable.XAXIS         : set(),
        SymbolTable.YAXIS         : set(),
    }

    @staticmethod
    def get_vars(typename):
        assert typename in YicesSignature.types_to_variables
        return sorted(list(YicesSignature.types_to_variables[typename]),  key=lambda var: var.name)

    # maps the op name to the yices operation corresponding to it
    # one day we will need to know arities.
    op_map = {}

    # signature map maps the op name to it's prototype using the NAMES of the types
    signature_map = {}

    thing_names  = None
    thing_terms  = None

    pt2_names = None
    pt2_terms = None

    # map the name to the yices term denoting it
    thing_map = {}
    pt2_map = {}

    # map the yices term to it's name
    thing_invmap = {}
    pt2_invmap = {}


    @staticmethod
    def configure_yices():

        #these are delayed until after we have read in the configuration file
        YicesSignature.thing_names  = SymbolTable.thing_names()
        YicesSignature.pt2_names = SymbolTable.pt2_names()

        if not YicesSignature.declare_types():
            sys.stderr.write('YicesSignature.declare_types() failed\n')
            return False
        if not YicesSignature.declare_functions():
            sys.stderr.write('YicesSignature.declare_functions() failed\n')
            return False

        return True


    @staticmethod
    def declare_types():

        def update_maps(names, terms, n2t_map, t2m_map):
            for i, name in enumerate(names):
                n2t_map[name] = terms[i]
                t2m_map[terms[i]] = name

        # ENUM TYPES

        (YicesSignature.thing_type, YicesSignature.thing_terms) = Types.declare_enum(SymbolTable.THING, YicesSignature.thing_names)
        if YicesSignature.thing_type is None:
            return False
        update_maps(YicesSignature.thing_names, YicesSignature.thing_terms, YicesSignature.thing_map, YicesSignature.thing_invmap)
        # doing the same thing two different ways. Need to to ditch one. The C version is probably way faster.

        (YicesSignature.pt2_type, YicesSignature.pt2_terms) = Types.declare_enum(SymbolTable.PT2, YicesSignature.pt2_names)
        if YicesSignature.pt2_type is None:
            return False
        update_maps(YicesSignature.pt2_names, YicesSignature.pt2_terms, YicesSignature.pt2_map, YicesSignature.pt2_invmap)

        # NON ENUM TYPES

        YicesSignature.nat_type = Types.int_type(SymbolTable.NAT)
        if YicesSignature.nat_type is None:
            return False

        YicesSignature.time_type = Types.int_type(SymbolTable.TIME)
        if YicesSignature.time_type is None:
            return False

        YicesSignature.stage_type = Types.int_type(SymbolTable.STAGE)
        if YicesSignature.stage_type is None:
            return False


        # OPERATIONS

        YicesSignature.b_prototype     = ([YicesSignature.int_type], YicesSignature.thing_type)
        YicesSignature.b_type          = Types.new_function_type(*YicesSignature.b_prototype)
        if YicesSignature.b_type == -1:
            return False
        YicesSignature.signature_map[SymbolTable.B] = ([SymbolTable.BINDEX], SymbolTable.THING)

        YicesSignature.ob_signature     = ([SymbolTable.BINDEX], SymbolTable.THING)
        YicesSignature.ob_prototype     = ([YicesSignature.int_type], YicesSignature.thing_type)
        YicesSignature.ob_type          = Types.new_function_type(*YicesSignature.ob_prototype)
        if YicesSignature.ob_type == -1:
            return False
        YicesSignature.signature_map[SymbolTable.OB] = ([SymbolTable.OBINDEX], SymbolTable.THING)

        YicesSignature.pt_prototype     = ([YicesSignature.int_type, YicesSignature.int_type], YicesSignature.pt2_type)
        YicesSignature.pt_type          = Types.new_function_type(*YicesSignature.pt_prototype)
        if YicesSignature.pt_type == -1:
            return False
        YicesSignature.signature_map[SymbolTable.PT] = ([SymbolTable.XAXIS, SymbolTable.YAXIS], SymbolTable.PT2)

        YicesSignature.atloc_prototype = ([YicesSignature.thing_type, YicesSignature.pt2_type, YicesSignature.time_type], YicesSignature.bool_type)
        YicesSignature.atloc_type = Types.new_function_type(*YicesSignature.atloc_prototype)
        if YicesSignature.atloc_type == -1:
            return False
        YicesSignature.signature_map[SymbolTable.ATLOC] = ([SymbolTable.THING, SymbolTable.PT2, SymbolTable.TIME], SymbolTable.BOOL)

        YicesSignature.treatstage_prototype = ([YicesSignature.pt2_type, YicesSignature.stage_type, YicesSignature.time_type], YicesSignature.bool_type)
        YicesSignature.treatstage_type = Types.new_function_type(*YicesSignature.treatstage_prototype)
        if YicesSignature.treatstage_type == -1:
            return False
        YicesSignature.signature_map[SymbolTable.TREATSTAGE] = ([SymbolTable.PT2, SymbolTable.STAGE, SymbolTable.TIME], SymbolTable.BOOL)

        YicesSignature.abs_prototype = ([YicesSignature.int_type], YicesSignature.int_type)
        YicesSignature.abs_type = Types.new_function_type(*YicesSignature.abs_prototype)
        if YicesSignature.abs_type == -1:
            return False
        YicesSignature.signature_map[SymbolTable.ABS] = ([SymbolTable.ATOM], SymbolTable.ATOM)


        for infix in SymbolTable.INFIX:
            YicesSignature.signature_map[infix] = ([SymbolTable.ATOM, SymbolTable.ATOM], SymbolTable.ATOM)

        for binop in SymbolTable.BINOPS:
            YicesSignature.signature_map[binop] = ([SymbolTable.ATOM, SymbolTable.ATOM], SymbolTable.BOOL)


        return True

    @staticmethod
    def declare_functions():
        assert None not in ( YicesSignature.thing_type, YicesSignature.pt2_type, YicesSignature.stage_type, YicesSignature.time_type, YicesSignature.stage_type )

        YicesSignature.b_op = Terms.new_uninterpreted_term(YicesSignature.b_type, SymbolTable.B)
        if YicesSignature.b_op is None:
            sys.stderr.write('declare_functions: YicesSignature.b_op is none {0}\n', Yices.error_string())
        YicesSignature.op_map[SymbolTable.B] = YicesSignature.b_op

        YicesSignature.ob_op = Terms.new_uninterpreted_term(YicesSignature.ob_type, SymbolTable.OB)
        if YicesSignature.ob_op is None:
            sys.stderr.write('declare_functions: YicesSignature.ob_op is none {0}\n', Yices.error_string())
        YicesSignature.op_map[SymbolTable.OB] = YicesSignature.ob_op

        YicesSignature.pt_op = Terms.new_uninterpreted_term(YicesSignature.pt_type, SymbolTable.PT)
        if YicesSignature.pt_op is None:
            sys.stderr.write('declare_functions: YicesSignature.pt_op is none {0}\n', Yices.error_string())
        YicesSignature.op_map[SymbolTable.PT] = YicesSignature.pt_op

        YicesSignature.atloc_op = Terms.new_uninterpreted_term(YicesSignature.atloc_type, SymbolTable.ATLOC)
        if YicesSignature.atloc_op is None:
            sys.stderr.write('declare_functions: YicesSignature.atloc_op is none {0}\n', Yices.error_string())
        YicesSignature.op_map[SymbolTable.ATLOC] = YicesSignature.atloc_op

        YicesSignature.treatstage_op = Terms.new_uninterpreted_term(YicesSignature.treatstage_type, SymbolTable.TREATSTAGE)
        if YicesSignature.treatstage_op is None:
            sys.stderr.write('declare_functions: YicesSignature.treatstage_op is none {0}\n', Yices.error_string())
        YicesSignature.op_map[SymbolTable.TREATSTAGE] = YicesSignature.treatstage_op

        # DANGER: python2 crazyness! Enter at own risk!!
        YicesSignature.abs_op = Terms.abs
        YicesSignature.op_map[SymbolTable.ABS] = Terms.abs # cannot use YicesSignature.abs_op because it has been mangled into an "unbound method"!!!!
        #print(f'YicesSignature.abs_op = {YicesSignature.abs_op}')
        #print(f'YicesSignature.op_map[SymbolTable.ABS] = {YicesSignature.op_map[SymbolTable.ABS]}')


        return True


    @staticmethod
    def declare_variable(var, bound_variables):
        """ constructs the yices term associated with the logical variable.

        In the case that bound_variables is not None, we are parsing an invariant,
        so that any NEW variables that we see are taken to be bound by the implicit universal
        quantifiers.
        """
        varname = var.name
        vartype = var.vartype

        # check if it is bound and has already been seen
        if bound_variables is not None and varname in bound_variables:
            yvar = bound_variables[varname].yices_term
            var.bound = True
            return yvar

        # check if it has already been seen
        yvar = Terms.get_by_name(varname)
        if yvar is not None:
            #now we need to see if it is free or bound
            tag = Terms.constructor(yvar)
            if tag == Constructor.VARIABLE:
                var.bound = True
                bound_variables[varname] = var
            return yvar

        type_term = vartype.yices_term
        type_name = vartype.name

        var_term = None

        if bound_variables is not None:
            # we need to make a yices variable not an uninterpreted term
            var_term = Terms.new_variable(type_term, varname)
            if var_term is None:
                sys.stderr.write(f'declare_variable: Term.new_variable failed {Yices.error_string()}\n')
                return None
            bound_variables[varname] = var
            var.bound = True
        else:
            var_term = Terms.new_uninterpreted_term(type_term, varname)
            if var_term is None:
                sys.stderr.write(f'declare_variable: Term.new_uninterpreted_term failed {Yices.error_string()}\n')
                return None

            YicesSignature.types_to_variables[type_name].add(var)

        return var_term

    integer_map = {}

    @staticmethod
    def integer(i):
        i = int(i)
        retval = YicesSignature.integer_map.get(i, None)
        if retval is None:
            retval = Terms.integer(i)
            YicesSignature.integer_map[i] = retval
        return retval

    @staticmethod
    def model2term(model):
        termlist = []
        #do the times
        for tvar in YicesSignature.get_vars(SymbolTable.TIME):
            ytvar = tvar.yices_term
            ytval = model.get_value_as_term(ytvar)
            termlist.append(Terms.arith_eq_atom(ytvar, ytval))

        #do the points
        for ptvar in YicesSignature.get_vars(SymbolTable.PT2):
            ytvar = ptvar.yices_term
            ytval = model.get_value(ytvar)
            termlist.append(Terms.eq(ytvar, ytval))

        #do the stages
        # FIXME:  more stuff needed here

        return Terms.yand(termlist)


    @staticmethod
    def get_yices_op(name):
        yices_term = None
        # treat abs a bit differently because it maps directly to a yices op, just like the infix ops.
        if name == SymbolTable.ABS:
            op_term = YicesSignature.op_map[name]
            yices_term = lambda args: op_term(args[0])
        elif name in YicesSignature.op_map:
            op_term = YicesSignature.op_map[name]
            yices_term = lambda args: Terms.application(op_term, args)
        elif name in SymbolTable.binop_map:
            yices_term = lambda args: SymbolTable.binop_map[name](args[0], args[1])
        elif name in SymbolTable.infix_map:
            yices_term = lambda args: SymbolTable.infix_map[name](args[0], args[1])
        assert yices_term is not None
        return yices_term

    @staticmethod
    def get_yices_type(name):
        return Types.get_by_name(name)

    @staticmethod
    def mkatloc(bot, pt, timestamp):

        bot_term = YicesSignature.thing_map.get(bot, None)
        if bot_term is None:
            sys.stderr.write(f'mkatloc: no bot called {bot}\n')
            return None

        pt_term = YicesSignature.pt2_map.get(pt, None)
        if pt_term is None:
            sys.stderr.write(f'mkatloc: no pt called {pt}\n')
            return None

        time_term = YicesSignature.integer(timestamp)

        application = Terms.application(YicesSignature.atloc_op, [bot_term, pt_term, time_term])
        if application is None:
            sys.stderr.write(f'mkatloc: Terms.application failed {Yices.error_string()}\n')
            return None

        return application


    @staticmethod
    def mktreatstage(pt, stage, timestamp):

        pt_term = YicesSignature.pt2_map.get(pt, None)
        if pt_term is None:
            sys.stderr.write(f'assert_atloc: no pt called {pt}\n')
            return None

        stage_term = YicesSignature.integer(stage)

        time_term = YicesSignature.integer(timestamp)

        application = Terms.application(YicesSignature.treatstage_op, [pt_term, stage_term, time_term])
        if application is None:
            sys.stderr.write(f'assert_atloc: Terms.application failed {Yices.error_string()}\n')
            return None

        return application

    @staticmethod
    def toYicesTerms():

        retval = []

        for i in range(0, Configuration.bot_count):
            retval.append(Terms.eq(Terms.application(YicesSignature.b_op, [YicesSignature.integer(i)]),
                                   YicesSignature.thing_map[SymbolTable.bot_name(i)]))
            #sb.append(f'(assert (= (b {i}) b{i}))\n')


        for i in range(0, Configuration.pt2_count):
            x = i/Configuration.grid_dimension[1]
            y = i % Configuration.grid_dimension[1]
            retval.append(Terms.eq(Terms.application(YicesSignature.pt_op, [YicesSignature.integer(x), YicesSignature.integer(y)]),
                                   YicesSignature.pt2_map[SymbolTable.pt2_name(i)]))

                #sb.append(f'(assert (= (pt {x} {y}) pt_{x}_{y}))\n')

        return retval
