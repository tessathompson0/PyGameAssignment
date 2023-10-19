import pygame
from pygame.locals import *
pygame.init()
(width,height) = (800,600)
window = pygame.display.set_mode((width,height))

#Beginning of Game
bg_img1 = pygame.image.load('WelcomeMessage.png')
bg_img1 = pygame.transform.scale(bg_img1,(width,height))

#Background if you win
bg_img2 = pygame.image.load('YouWin.png')
bg_img2 = pygame.transform.scale(bg_img2,(width,height))

#Background if you lose
bg_img3 = pygame.image.load('YouLose.png')
bg_img3 = pygame.transform.scale(bg_img3,(width,height))

#Background for main part of game
bg_img4 = pygame.image.load('Background.png')
bg_img4 = pygame.transform.scale(bg_img4,(width,height))

#StartButton
bg_img5 = pygame.image.load('StartGame.png')
bg_img5 = pygame.transform.scale(bg_img5,(50,70))


class background:
    def setFirstBackground(self):
        running = True
        while running:
            window.blit(bg_img1,(0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    runing = False
                    pygame.quit()
            pygame.display.update()
        pygame.quit()
    def setBackgroundMain(self):
        running = True
        while running:
            window.blit(bg_img4,(0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    runing = False
                    pygame.quit()
            pygame.display.update()
        pygame.quit()
    def setYouWinBackground(self):
        running = True
        while running:
            window.blit(bg_img2,(0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    runing = False
                    pygame.quit()
            pygame.display.update()
        pygame.quit()
    def setYouLoseBackground(self):
        running = True
        while running:
            window.blit(bg_img3,(0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    runing = False
                    pygame.quit()
            pygame.display.update()
        pygame.quit()
    def startButton(self):
        running = True
        while running:
            window.blit(bg_img5,(0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    runing = False
                    pygame.quit()
            pygame.display.update()

         