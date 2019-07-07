import numpy as np
import pygame
import pygame.gfxdraw



class VisualSnakeGame:

    def __init__(self, screen, snakegame):
        self.screen = screen
        self.snakegame = snakegame
        self.posx = 00
        self.posy = 00
        self.height = 800
        self.width = 800
        self.gridsize = snakegame.grid.shape[0]


    def draw(self):

        for i in range(self.gridsize + 1):
            # vertical lines
            pygame.draw.aaline(self.screen, [255, 255, 255],
                               [int(self.posx + i * self.width / self.gridsize),
                                int(self.posy)],
                               [int(self.posx + i * self.width / self.gridsize),
                                int(self.posy + self.height)])
            #horizontal lines
            pygame.draw.aaline(self.screen, [255, 255, 255],
                           [int(self.posx),
                            int(self.posy + i * self.height / self.gridsize)],
                           [int(self.posx + self.width),
                            int(self.posy + i * self.height / self.gridsize)])
            #apple
            if self.snakegame.appleposX >= 0:  # if it's not complete
                applex = self.snakegame.appleposX
                appley = self.snakegame.appleposY
                pygame.gfxdraw.filled_circle(self.screen,
                     int(self.posx + applex * self.width / self.gridsize + self.width / self.gridsize / 2),
                     int(self.posy + appley * self.height / self.gridsize + self.height / self.gridsize / 2),
                     int(self.width/self.gridsize/2), [255, 200, 40])
                pygame.gfxdraw.aacircle(self.screen,
                    int(self.posx + applex * self.width / self.gridsize + self.width / self.gridsize / 2),
                    int(self.posy + appley * self.height / self.gridsize + self.height / self.gridsize / 2),
                    int(self.width/self.gridsize/2), [255, 200, 40])
        grid = self.snakegame.grid
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i][j] > 0:
                    pygame.gfxdraw.box(self.screen,
                                         [int(self.posx + i * self.width / self.gridsize),
                                          int(self.posy + j * self.height / self.gridsize),
                                          int(self.width / self.gridsize) + 1,
                                          int(self.width / self.gridsize) + 1],
                                         [255, 255, 255])


    def setposition(self, x, y):
        self.posx = x
        self.posy = y

    def setwidth(self, w):
        self.width = w

    def setheight(self, h):
        self.height = h
