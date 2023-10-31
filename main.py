#Tessa Thompson
#10.18.23
#King Curtis Game

import pygame
from player import Player
from enemy import Enemy
from enemy import goodEnemy

pygame.init()

#set up screen
width, height = 800, 600
screen_size = (width, height)
FPS = 60

screen = pygame.display.set_mode(screen_size)
#add title to game
pygame.display.set_caption("King Curtis Game")

#make sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
goodEnemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

#add multiple enemies
for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)
for i in range(5):
    goodenemy = goodEnemy()
    all_sprites.add(goodenemy)
    goodEnemies.add(goodenemy)

#start a score system
score = 0

#make background a png image
background = pygame.image.load("Background.png").convert()

#keep running until x button is pushed
running = True
while running:
    for event in pygame.event.get():
        #if person presses x
        if event.type == pygame.QUIT:
            running = False
    #make background appear
    screen.blit(background, (0,0))
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, enemies, True)
    #gain and lose points with enemies
    for enemy in hits:
        score -= 1
        new_enemy = Enemy()
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)
    hits2 = pygame.sprite.spritecollide(player, goodEnemies, True)
    for goodenemy in hits2:
        score += 1
        new_goodEnemy = goodEnemy()
        all_sprites.add(new_goodEnemy)
        enemies.add(new_goodEnemy)
    #make sprites show up on screen
    all_sprites.draw(screen)
    #show points scored
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: {}".format(score),True,(255, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
