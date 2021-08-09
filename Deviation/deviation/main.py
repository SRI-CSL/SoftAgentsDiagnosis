import argparse

from .visitor.Parser import (configurationFromFile, parseFromFile)

from .logic.Configuration import Configuration

from .logic.Facts import Facts

from .logic.Solver import Solver

from .logic.YicesSignature import YicesSignature


VERBOSE = False

def main():

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('--verbose', '-v',
                        dest='verbose',
                        help='Run the solving in verbose mode',
                        action="store_true")

    parser.add_argument('--debug', '-d',
                        dest='debug',
                        help='Run the solving in debug mode',
                        action="store_true")

    parser.add_argument('--all', '-a',
                        dest='all_solutions',
                        help='Find all solutions, rather than just the first.',
                        action='store_true')

    parser.add_argument('--incremental', '-i',
                        dest='incrementally_solve',
                        help='Incrementally check the protocol against the log.',
                        action='store_true')

    parser.add_argument('--frontier', '-f',
                        dest='frontier',
                        help='Compute the frontier.',
                        action='store_true')

    parser.add_argument('--timeline', '-l',
                        dest='timeline',
                        help='Fix the iterpretation of the timeline (overrides what is in the config file).',
                        default=None)

    parser.add_argument('--entire', '-e',
                        dest='entire',
                        help='Compute the entire tree.',
                        action='store_true')

    parser.add_argument('--missing', '-m',
                        dest='missing',
                        help='Check for missing protocol events in the log, per timeline.',
                        action='store_true')

    parser.add_argument('--unsat', '-u',
                        dest='unsat_core',
                        help='Find the unsat core.',
                        action='store_true')

    parser.add_argument('--consistency', '-c',
                        dest='consistency_check',
                        help='Check the model for consistency.',
                        action='store_true')

    parser.add_argument('--configuration', '-g',
                        dest='cfg_file',
                        help='The configuration file. If none supplied, then we use the defaults.',
                        default=None)

    parser.add_argument('--theory', '-t',
                        dest='theory_file',
                        help='The theory file. If given will write out the theory to the file.',
                        default=None)

    parser.add_argument('log_file',
                        help='The log file.',
                        default=None)


    parser.add_argument('constraint_file',
                        help='The constraint file.',
                        default=None)


    args = parser.parse_args()

    if args.cfg_file:
        print(args.cfg_file)
        configurationFromFile(args.cfg_file)

    # Need to declare the types we will be using
    if not YicesSignature.configure_yices():
        return 2

    if args.timeline:
        value = int(args.timeline)
        print('timeline_interpretation = {0}'.format(value))
        Configuration.configure('timeline_interpretation', value)

    model = Facts()
    requirements = None

    parseFromFile(model, args.log_file)

    if args.debug:
        print('\nModel:\n')
        model.dump()

    requirements = Facts()

    parseFromFile(requirements, args.constraint_file)

    if args.debug:
        print('\nProtocol:\n')
        requirements.dump()

    retcode = 0

    # When solving (not exhausting)
    # a retcode of 0 means the problem is SAT
    # a retcode of 1 means the problem is UNSAT
    # a retcode of 2 means there was an error somewhere


    if args.consistency_check:
        Solver(model, requirements, args.verbose).consistency_check()
    elif args.all_solutions:
        Solver(model, requirements, args.verbose).exhaust()
    elif args.unsat_core:
        Solver(model, requirements, args.verbose).unsat_core()
    elif args.incrementally_solve:
        Solver(model, requirements, args.verbose).incrementally_solve()
    elif args.frontier:
        Solver(model, requirements, args.verbose).frontier()
    elif args.entire:
        Solver(model, requirements, args.verbose).entire()
    elif args.missing:
        Solver(model, requirements, args.verbose).missing()
    else:
        retcode =  Solver(model, requirements, args.verbose).solve(args.theory_file)

    return retcode
