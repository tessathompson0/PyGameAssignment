#Tessa Thompson
#10.18.23
#King Curtis Game

import pygame 
import time
pygame.init()

from MainGame import MainGame

#blank canvas
#(width, height) = (800, 600)
#screen = pygame.display.set_mode((width, height))
#add name to top of screen
pygame.display.set_caption('King Curtis Game')
pygame.display.flip()

x = MainGame()
x.loadBackground()


