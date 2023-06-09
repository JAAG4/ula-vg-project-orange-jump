"""
This module was autogenerated by gale.
"""
import settings
from src.OrangeJump import OrangeJump
import logging
from sys import stdout

logging.basicConfig(level=logging.DEBUG, stream=stdout)

if __name__ == "__main__":
    game = OrangeJump(
        "Orange Jump",
        settings.WINDOW_WIDTH,
        settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH,
        settings.VIRTUAL_HEIGHT,
        fps=30,
    )
    game.exec()
