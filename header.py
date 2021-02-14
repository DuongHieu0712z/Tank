import pygame
from pygame import Vector2
from pygame.locals import *
from enum import Enum

# Size
WIDTH = 480
HEIGHT = 320
SCREEN = (WIDTH, HEIGHT)

SIZE_IMG = 16

# Color
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
CYAN = Color(0, 255, 255)
MAGENTA = Color(255, 0, 255)
YELLOW = Color(255, 255, 0)
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)

SPEED_TANK = 1

FPS = 10

MAX_FRAMES = 5


class AutoNumber(Enum):
    def __new__(cls):
        value = len(cls.__members__)
        obj = object.__new__(cls)
        obj._value_ = value
        return obj


class Direction(Enum):
    UP = Vector2(0, -1)
    DOWN = Vector2(0, 1)
    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)
