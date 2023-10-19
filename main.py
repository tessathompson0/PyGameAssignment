#Tessa Thompson
#10.18.23
#King Curtis Game

import pygame 
import time
pygame.init()
from background import background

#blank canvas
#(width, height) = (800, 600)
#screen = pygame.display.set_mode((width, height))
#add name to top of screen
pygame.display.set_caption('King Curtis Game')
#pygame.display.flip()

start_time = pygame.time.get_ticks()
current_time = pygame.time.get_ticks()
#set main screen
main = background()
main.setFirstBackground()

current_time = pygame.time.get_ticks()
if current_time >= 10000:
  main.setBackgroundMain()
  pygame.display.flip()

#if x (exit) is clicked
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.display.flip()