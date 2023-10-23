import pygame
from pygame.locals import *
pygame.init()
import random
(width,height) = (800,600)
window = pygame.display.set_mode((width,height))
main_background = pygame.image.load('Background.png')
player = pygame.image.load('Player.png')

class MainGame:
    def loadBackground(self):
        running = True
        while running:
            window.blit(main_background,(0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            pygame.display.update()
        pygame.quit()
  
    

        
