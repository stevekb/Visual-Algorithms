import numpy as np
from enum import Enum

Direction = Enum("Direction", ("LEFT", "RIGHT", "UP", "DOWN"))


class SnakeGame:

    #grid initiate and has snake locations
    #initiate snake position var
    #initiate apple position var
    #initiate snake direction var
    def __init__(self, size):
        self.grid = np.zeros((size, size))
        self.snakeposX = 0
        self.snakeposY = 0
        self.appleposX = 2
        self.appleposY = 2
        self.snakeDir = Direction.RIGHT
