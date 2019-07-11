from VisualGUI import VisualGUI
from VisualNN import VisualNN
from neuralnet import NeuralNet
from SnakeGame import SnakeGame
from VisualSnakeGame import VisualSnakeGame
from SnakeGame import Direction
from EvolutionTrainer import EvolutionTrainer
import pygame
import numpy as np
import pygame.gfxdraw
#this class is just a wrapper
#where I can run different things

# for our sample data set just use random numbers
#and then sin
#trainingX = np.array()

# shape = [2,5,6]
# bias = [np.zeros((s, 1)) for s in shape[1:]]
# print(bias)
# bias = [np.array([np.random.standard_normal(s)/s**.5]).T for s in shape[1:]]
# print(bias)


gamesize = 4


vg = VisualGUI()
pygame.init()
screen = pygame.display.set_mode((1200, 800))
time = 0.0

searching = True
bestnnbias = []
bestnnweights = []
myNN = NeuralNet((gamesize*gamesize+6, 10, 10, 10, 4))
# print(myNN.getweights())
# print(myNN.predict([0]*70))

mySG = SnakeGame(gamesize)
myVSG = VisualSnakeGame(screen, mySG)
myVSG.setheight(500)
myVSG.setposition(650, 150)
myVSG.setwidth(500)

# myNN.randomize()
# print(myNN.getoutputw())
VNN = VisualNN(screen, myNN)
VNN.setheight(700)
VNN.setposition(50, 50)
VNN.setwidth(500)
# basic loop
running = True
bestscore = 20
entry = 0

#evolution trainer
et = EvolutionTrainer(myNN, mySG)


while running:
    screen.fill((0, 0, 0))
    VNN.draw()
    myVSG.draw()
    state = myVSG.snakegame.getstate()
    #myNN.predict(state.T)


    if et.currgen < 500:
        et.evalGeneration()


    time += 0.1
    #entry+=1
    pygame.display.update()

    if bestscore < 10 and searching:
        for i in range(10000):
            entry += 1
            myVSG.snakegame.reset()
            VNN.nn.randomize()
            score = myVSG.snakegame.getscore(VNN.nn)
            if score > bestscore:
                bestscore = score
                bestnnweights = VNN.nn.getweights()
                bestnnbias = VNN.nn.getbias()
                print("entry: " + str(entry) + " new best score: " + str(bestscore))
        if entry%100 == 0:
            print("entry: " + str(entry) + " score: " + str(score) + " bestscore: " + str(bestscore))

    if searching == False:
        myVSG.snakegame.update(myVSG.snakegame.predict(VNN.nn.predict(myVSG.snakegame.getstate().T)))
        if myVSG.snakegame.finished:
            searching = True

    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0]:
            k = 0
            # VNN.clicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            # et.evalGeneration()

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            searching = False
            myVSG.snakegame.reset()
            VNN.nn.weights = bestnnweights
            VNN.nn.bias = bestnnbias

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            print("Human: LEFT, AI: " + str(myVSG.snakegame.predict(myNN.predict(state.T))))
            myVSG.snakegame.update(Direction.LEFT)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            print("Human: RIGHT, AI: " + str(myVSG.snakegame.predict(myNN.predict(state.T))))
            myVSG.snakegame.update(Direction.RIGHT)
        if pygame.key.get_pressed()[pygame.K_UP]:
            print("Human: UP, AI: " + str(myVSG.snakegame.predict(myNN.predict(state.T))))
            myVSG.snakegame.update(Direction.UP)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            print("Human: DOWN, AI: " + str(myVSG.snakegame.predict(myNN.predict(state.T))))
            myVSG.snakegame.update(Direction.DOWN)

        if event.type == pygame.QUIT:
            running = False

