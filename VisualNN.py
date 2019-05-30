import numpy as np
from NN import NN
import pygame
import pygame.gfxdraw

# the following will visualize a nn that has been thrown in
# note this will accept a custom NN object which contains data about itself
# this class will draw and position it when asked by the main class


class VisualNN:

    def __init__(self, screen, nn):
        self.screen = screen
        self.nn = nn
        self.posx = 50
        self.posy = 50
        self.height = 700
        self.width = 700
        self.inputHeight = nn.getinputw().shape[0]
        self.hiddenHeight = nn.gethiddenw().shape[0]
        self.hiddenWidth = nn.gethiddenw().shape[2]
        self.outputHeight = nn.getoutputw().shape[1]
        self.hspacing = self.width / (self.hiddenWidth + 2)

        #calculate positions of all the nodes (from 0-1) so we can scale
        #array of x's (they are all the same away from each other
        #array of all the ys in input/hidden/output (separate)
        #see if below can be written better than this
        self.nodePosX = np.arange(self.hiddenWidth + 2) / (self.hiddenWidth + 2) + (1 / (self.hiddenWidth + 2)) / 2
        self.nodeInputPosY = np.arange(self.inputHeight) / self.inputHeight + (1 / self.inputHeight) / 2
        self.nodeHiddenPosY = np.arange(self.hiddenHeight) / self.hiddenHeight + (1 / self.hiddenHeight) / 2
        self.nodeOutputPosY = np.arange(self.outputHeight) / self.outputHeight + (1 / self.outputHeight) / 2
        print("test")
        print(self.nodeHiddenPosY)

    def print(self):
        print(self.nn.getinputw())
        print(self.nn.gethiddenw())
        print(self.nn.getoutputw())

    def draw(self):
        # draw all weights first
        weights = self.nn.getinputw()
        for j in range(self.inputHeight):
            for i in range(self.hiddenHeight): #weights
                pygame.gfxdraw.line(self.screen,
                                    int(self.posx + self.nodePosX[0] * self.width),
                                    int(self.posy + self.nodeInputPosY[j] * self.height),
                                    int(self.posx + self.nodePosX[1] * self.width),
                                    int(self.posy + self.nodeHiddenPosY[i] * self.height),
                                    self.weighttocolor(weights[j][i]))

        weights = self.nn.getoutputw()
        for j in range(self.outputHeight):
            for i in range(self.hiddenHeight):
                pygame.gfxdraw.line(self.screen,
                                    int(self.posx + self.nodePosX[-2] * self.width),
                                    int(self.posy + self.nodeHiddenPosY[i] * self.height),
                                    int(self.posx + self.nodePosX[-1] * self.width),
                                    int(self.posy + self.nodeOutputPosY[j] * self.height),
                                    self.weighttocolor(weights[i][j]))

        weights = self.nn.gethiddenw()
        for i in range(self.hiddenWidth):
            for j in range(self.hiddenHeight):
                #if we're not at the end then do it
                if i != self.hiddenWidth - 1:
                    for z in range(self.hiddenHeight):
                        pygame.gfxdraw.line(self.screen,
                                            int(self.posx + self.nodePosX[i + 1] * self.width),
                                            int(self.posy + self.nodeHiddenPosY[j] * self.height),
                                            int(self.posx + self.nodePosX[i + 2] * self.width),
                                            int(self.posy + self.nodeHiddenPosY[z] * self.height),
                                            self.weighttocolor(weights[j][z][i]))


        # draw all nodes after
        for j in range(self.inputHeight):
            pygame.gfxdraw.filled_circle(self.screen,
                                         int(self.posx + self.nodePosX[0] * self.width),
                                         int(self.posy + self.nodeInputPosY[j] * self.height),
                                         16, [255, 255, 255])
            pygame.gfxdraw.aacircle(self.screen,
                                    int(self.posx + self.nodePosX[0] * self.width),
                                    int(self.posy + self.nodeInputPosY[j] * self.height),
                                    16, [255, 255, 255])

        for j in range(self.outputHeight):
            pygame.gfxdraw.filled_circle(self.screen,
                                         int(self.posx + self.nodePosX[-1] * self.width),
                                         int(self.posy + self.nodeOutputPosY[j] * self.height),
                                         16, [255, 255, 255])
            pygame.gfxdraw.aacircle(self.screen,
                                    int(self.posx + self.nodePosX[-1] * self.width),
                                    int(self.posy + self.nodeOutputPosY[j] * self.height),
                                    16,
                                    [255, 255, 255])

        for i in range(self.hiddenWidth):
            for j in range(self.hiddenHeight):
                pygame.gfxdraw.filled_circle(self.screen,
                                             int(self.posx + self.nodePosX[i + 1] * self.width),
                                             int(self.posy + self.nodeHiddenPosY[j] * self.height),
                                             16, [255, 255, 255])
                pygame.gfxdraw.aacircle(self.screen,
                                        int(self.posx + self.nodePosX[i + 1] * self.width),
                                        int(self.posy + self.nodeHiddenPosY[j] * self.height),
                                        16, [255, 255, 255])


    # this takes in a weight and translate it from -1 to 1 to 0-255
    def weighttocolor(self, value):
        a = int((value + 1.0)/2.0 * 255.0)
        return [255 - a, a, 0]
