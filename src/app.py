import time
from pynput.keyboard import Controller, Key

from .config.constants import Constants
from .util.make_args_parser import make_args_parser


def app(
    filename,
    initial_delay: int = Constants.INITIAL_DELAY,
    line_delay: int = Constants.LINE_DELAY,
    max_lines: int = Constants.MAX_LINES
) -> None:
    # wait for the cursor to be manually focused
    time.sleep(initial_delay)

    with open(filename) as file:
        keyboard = Controller()
        max_limit = max_lines

        for line in file:
            keyboard.type(line)
            keyboard.tap(Key.enter)

            max_limit -= 1
            if not max_limit:
                break

            time.sleep(line_delay)


if __name__ == '__main__':
    args = make_args_parser().parse_args()

    app(
        filename=args.file,
        initial_delay=int(args.initial_delay),
        line_delay=int(args.line_delay),
        max_lines=args.max_lines if type(
            args.max_lines) == float else int(args.max_lines)
    )
