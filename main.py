from VisualGUI import VisualGUI
from VisualNN import VisualNN
from NN import NN
import pygame
import pygame.gfxdraw
#this class is just a wrapper
#where I can run different things

# for our sample data set just use random numbers
#and then sin

#trainingX = np.array()


vg = VisualGUI()
pygame.init()
screen = pygame.display.set_mode((800, 800))
time = 0.0

myNN = NN(1, (3, 3), 1)
# print(myNN.getinputw())
myNN.randomize()
print(myNN.getoutputw())
VNN = VisualNN(screen, myNN)

# basic loop
running = True
while running:
    screen.fill((0, 0, 0))
    VNN.draw()
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

            VNN.nn.randomize()
            
        if event.type == pygame.QUIT:
            running = False

