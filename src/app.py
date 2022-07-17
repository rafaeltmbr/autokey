import time
from pynput.keyboard import Controller, Key

from src.constants import Constants


def app(
    filename: str = Constants.FILENAME,
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
