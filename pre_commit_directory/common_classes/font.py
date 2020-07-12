#!/usr/bin/python3
from enum import Enum


class Font:
    BLACK_FONT = '\33[30m'
    RED_FONT = '\33[31m'
    GREEN_FONT = '\33[32m'
    BLUE_FONT = "\33[44m"
    CEND = '\33[0m'

    def __init__(self, color):
        None

    @staticmethod
    def get_color(color, text):
        result = "{0}" + text + Font.CEND

        if color == Color.RED:
            return result.format(Font.RED_FONT)
        elif color == Color.GREEN:
            return result.format(Font.GREEN_FONT)
        elif color == Color.BLUE:
            return result.format(Font.BLUE_FONT)
        else:
            return result.format(Font.BLACK_FONT)


class Color(Enum):
    RED = 1
    GREEN = 2
    ORANGE = 3
    YELLOW = 4
    BLACK = 5
    BLUE = 6
