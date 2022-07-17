import argparse

from ..config.constants import Constants


def make_args_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument('file',
                        help='path to the source file')

    parser.add_argument('--initial-delay', '-i',
                        default=Constants.INITIAL_DELAY,
                        help='initial time (in seconds) to print the first line')

    parser.add_argument('--line-delay', '-l',
                        default=Constants.LINE_DELAY,
                        help='time (in seconds) to print each line')

    parser.add_argument('--max-lines', '-m',
                        default=Constants.MAX_LINES,
                        help='maximum lines to be printed out')

    return parser
