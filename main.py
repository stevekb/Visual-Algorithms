from VisualGUI import VisualGUI
from VisualNN import VisualNN
from neuralnet import NeuralNet
from SnakeGame import SnakeGame
from VisualSnakeGame import VisualSnakeGame
from SnakeGame import Direction
import pygame
import pygame.gfxdraw
#this class is just a wrapper
#where I can run different things

# for our sample data set just use random numbers
#and then sin

#trainingX = np.array()

z = (4,2,2,3)
shapes = list(zip(z[1:], z[:-1]))
w_shapes = [(a, b) for a, b in zip(z[1:], z[:-1])]
print(shapes)
print(w_shapes)

vg = VisualGUI()
pygame.init()
screen = pygame.display.set_mode((1200, 800))
time = 0.0


myNN = NeuralNet((70, 5, 5, 5, 4))
# print(myNN.getweights())
print(myNN.predict([0]*70))

mySG = SnakeGame(8)
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
bestscore = 0
entry = 0
while running:
    screen.fill((0, 0, 0))
    VNN.draw()
    myVSG.draw()
    state = myVSG.snakegame.getstate()
    #myNN.predict(state.T)


    time += 0.1
    entry+=1
    pygame.display.update()

    if bestscore < 10:
        myVSG.snakegame.reset()
        VNN.nn.randomize()
        score = myVSG.snakegame.getscore(VNN.nn)
        if score > bestscore:
            bestscore = score
            print("entry: " + str(entry) + " new best score: " + str(bestscore))
        if entry%100 == 0:
            print("entry: " + str(entry) + " score: " + str(score) + " bestscore: " + str(bestscore))

    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0]:
            VNN.clicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            myVSG.snakegame.reset()
            VNN.nn.randomize()
            score = myVSG.snakegame.getscore(VNN.nn)
            if score > bestscore:
                bestscore = score
            print("score: " + str(score) + " bestscore: " + str(bestscore))

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
            pygame.quit()

