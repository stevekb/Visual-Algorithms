from VisualGUI import VisualGUI
from VisualNN import VisualNN
from neuralnet import NeuralNet
import pygame
import pygame.gfxdraw
#this class is just a wrapper
#where I can run different things

# for our sample data set just use random numbers
#and then sin

#trainingX = np.array()

z = (4,2,3)
shapes = list(zip(z[1:], z[:-1]))
w_shapes = [(a, b) for a, b in zip(z[1:], z[:-1])]
print(shapes)
print(w_shapes)

vg = VisualGUI()
pygame.init()
screen = pygame.display.set_mode((800, 800))
time = 0.0

myNN = NeuralNet((2, 10, 10, 4))
# print(myNN.getweights())
print("test")
print(myNN.predict([3, 1]))
# myNN.randomize()
# print(myNN.getoutputw())
# VNN = VisualNN(screen, myNN)

# basic loop
running = True
while running:
    screen.fill((0, 0, 0))
    # VNN.draw()
    #update array info

    # array = vg.get_array()
    #
    # posx = 100.0
    # posy = 100.0
    # width = 600.0
    # height = 600.0
    # length = len(array)
    # for i in range(length):
    #     if array[i] == 0:
    #         continue
    #     pygame.draw.rect(screen,
    #                      [255, 255, 255],
    #                      (int(posx + i * width / length),
    #                       int(posy + height - int(array[i] * height / 32.0)),
    #                       int(width / length),
    #                       int(array[i] * height / 32.0)),
    #                      0)

    #pygame.gfxdraw.aacircle(screen,[255,255,255],[16,int(16+time)],16,0)
    # pygame.gfxdraw.filled_circle(screen, 16, int(16+time), 16, [255, 255, 255])
    # pygame.gfxdraw.aacircle(screen, 16, int(16+time), 16, [255, 255, 255])


    time += 0.1

    pygame.display.update()

    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0]:
            a = 0
            # VNN.nn.randomize()
            # VNN.clicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        if event.type == pygame.QUIT:
            running = False

