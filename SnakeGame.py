import numpy as np
from enum import Enum

Direction = Enum("Direction", ("LEFT", "RIGHT", "UP", "DOWN"))


class SnakeGame:

    #grid initiate and has snake locations
    #initiate snake position var
    #initiate apple position var
    #initiate snake direction var
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size))
        self.snakeposX = 2
        self.snakeposY = 0
        self.snakelength = 3
        self.appleposX = 2
        self.appleposY = 2
        self.snakedir = Direction.RIGHT
        self.score = 0
        self.maxlength = size*size
        self.finished = False
        for i in range(self.snakelength):
            self.grid[i][0] = i+1

    def reset(self):
        self.grid = np.zeros((self.size, self.size))
        self.snakeposX = 2
        self.snakeposY = 0
        self.snakelength = 3
        self.appleposX = 2
        self.appleposY = 2
        self.snakedir = Direction.RIGHT
        self.score = 0
        self.maxlength = self.size * self.size
        self.finished = False
        for i in range(self.snakelength):
            self.grid[i][0] = i + 1

    # takes in snake input and updates the grid
    def update(self, move):
        if self.finished == True:
            print("finished")
            return


        #print("hello")#
        #check if next spot is out of bounds
        if move == Direction.RIGHT:
            if self.snakeposX + 1 != self.grid.shape[0]:  # checks if not going off side
                self.snakedir = Direction.RIGHT
                self.snakeposX += 1
            else:
                self.finished = True
                return
        if move == Direction.LEFT:
            if self.snakeposX != 0:  # checks if not going off side
                self.snakedir = Direction.LEFT
                self.snakeposX -= 1
            else:
                self.finished = True
                return
        if move == Direction.UP:
            if self.snakeposY != 0:  # checks if not going off side
                self.snakedir = Direction.UP
                self.snakeposY -= 1
            else:
                self.finished = True
                return
        if move == Direction.DOWN:
            if self.snakeposY + 1 != self.grid.shape[1]:  # checks if not going off side
                self.snakedir = Direction.DOWN
                self.snakeposY += 1
            else:
                self.finished = True
                return

        #now that we know it's moved to the new spot lets decide what to do baesd on what is here
        #first if it's inside itself terminate the game
        if self.grid[self.snakeposX][self.snakeposY] > 0:
            self.finished = True
            return
        #if we're in the apple instead we wanna grow
        flush = True
        if self.snakeposY == self.appleposY and self.snakeposX == self.appleposX:
            self.snakelength += 1
            flush = False

        if flush is True:
            for i in range(self.grid.shape[0]):
                for j in range(self.grid.shape[1]):
                    if self.grid[i][j] > 0:
                        self.grid[i][j] -= 1
        #after flush we add new snake piece
        self.grid[self.snakeposX][self.snakeposY] = self.snakelength
        #we now put the apple in a new spot
        #first we find all spots that are free and put them into a list
        #then we get a random one and set that position as the new spot
        if flush is False:
            if self.snakelength == self.maxlength:
                self.finished = True
                return
            viable = []
            for i in range(self.grid.shape[0]):
                for j in range(self.grid.shape[1]):
                    if self.grid[i][j] == 0:
                        viable.append((i, j))
            choice = np.random.randint(len(viable))
            self.appleposX = viable[choice][0]
            self.appleposY = viable[choice][1]
            # if self.grid[self.appleposX][self.appleposY] > 0:
            #     print("overlap")
            # print("X: " +str(self.appleposX) + "Y: " + str(self.appleposY))
        #we're done now




    def getstate(self):
        state = self.grid.ravel()
        snakeleft = 1 if self.snakedir == Direction.LEFT else 0
        snakeright = 1 if self.snakedir == Direction.RIGHT else 0
        snakeup = 1 if self.snakedir == Direction.UP else 0
        snakedown = 1 if self.snakedir == Direction.DOWN else 0
        directions = np.array([snakeleft, snakeright, snakeup, snakedown])
        state = np.append(state, directions)
        applepos = np.array([self.appleposX, self.appleposY])
        state = np.append(state, applepos)

        return state

    def predict(self, output):
        largest = 0
        max_direction = Direction.LEFT
        for d in range(len(Direction)):
            if largest < output[d]:
                largest = output[d]
                max_direction = Direction(d + 1)
        return max_direction

    # iterates through the whole game until it's completed and returns length
    def getscore(self, nn):
        n = 0
        while not self.finished and n < 65:
            n += 1
            self.update(self.predict(nn.predict(self.getstate().T)))
        if n == 65:
            raise Exception("getscore ran too long and was stopped")
        return self.snakelength


