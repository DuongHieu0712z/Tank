import pygame
from pygame.locals import *
from enum import Enum

# Screen
WIDTH = 400
HEIGHT = 300
SCREEN = (WIDTH, HEIGHT)

# Cell
SIZE_CELL = 10

# Color
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
CYAN = pygame.Color(0, 255, 255)
MAGENTA = pygame.Color(255, 0, 255)
YELLOW = pygame.Color(255, 255, 0)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)


class AutoNumber(Enum):
    def __new__(cls, *args, **kwargs):
        value = len(cls.__members__)
        obj = object.__new__(cls)
        obj._value_ = value
        return obj


class Direction(AutoNumber):
    UP = ()
    DOWN = ()
    LEFT = ()
    RIGHT = ()
