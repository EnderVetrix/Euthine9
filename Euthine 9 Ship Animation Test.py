# test1_pyganim.py - A very very very basic pyganim test program.
#
# This program just runs a single animation. It shows you what you need to do to use Pyganim. Basically:
#   1) Import the pyganim module
#   2) Create a pyganim.PygAnimation object, passing the constructor a list of image filenames and durations.
#   3) Call the play() method.
#   4) Call the blit() method.
#
# The animation images come from POW Studios, and are available under an Attribution-only license.
# Check them out, they're really nice.
# http://powstudios.com/

import pygame
from pygame.locals import *
import sys
import time
import pyganim

pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((320, 240), 0, 32)
pygame.display.set_caption('Pyganim Test 1')

# create the animation objects   ('filename of image',    duration_in_seconds)
shipx = pyganim.PygAnimation([('Sprite/Euthine 9.png', 0.1),
                                 ('Sprite/Euthine 9 1.png', 0.1),
                                 ('Sprite/Euthine 9 2.png', 0.1),
                                 ('Sprite/Euthine 9 3.png', 0.1),
                                 ('Sprite/Euthine 9 4.png', 0.1),
                                 ('Sprite/Euthine 9 5.png', 0.1),
                                 ('Sprite/Euthine 9 6.png', 0.1),
                                 ('Sprite/Euthine 9 7.png', 0.1),
                                 ('Sprite/Euthine 9 8.png', 0.1),
                                 ('Sprite/Euthine 9 9.png', 0.1),
                                 ('Sprite/Euthine 9 10.png', 0.1)])
shipx.play() # there is also a pause() and stop() method

mainClock = pygame.time.Clock()
BGCOLOR = (100, 50, 50)
while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_l:
            # press "L" key to stop looping
            shipx.loop = False

    shipx.blit(windowSurface, (100, 50))

    pygame.display.update()
    mainClock.tick(30) # Feel free to experiment with any FPS setting.
