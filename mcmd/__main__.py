import logging
import signal
import sys

from mcmd import io
from mcmd.arguments import parse_args
from mcmd.commands.run import run
from mcmd.executor import execute
from mcmd.io import set_debug
from mcmd.logging import set_level


def main():
    # setup friendly interrupt message
    signal.signal(signal.SIGINT, interrupt_handler)

    # show help when no arguments are supplied
    if len(sys.argv) == 1:
        sys.argv.append('--help')

    args = parse_args()
    setattr(args, 'arg_string', ' '.join(sys.argv[1:]))
    set_log_level(args)

    if args.command == 'run':
        run(args)
    else:
        execute(args)


def set_log_level(args):
    if args.verbose:
        verbosity = int(args.verbose)
        if verbosity > 0:
            set_level(logging.DEBUG)
            set_debug()
    else:
        set_level(logging.INFO)


# noinspection PyUnusedLocal
def interrupt_handler(sig, frame):
    io.warn('Interrupted by user.')
    sys.exit(0)


if __name__ == '__main__':
    main()
