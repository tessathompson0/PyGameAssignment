#Tessa Thompson
#10.18.23
#King Curtis Game

import pygame
from player import Player
from enemy import Enemy

pygame.init()

width, height = 800, 600
screen_size = (width, height)
FPS = 60

white = (255, 255, 255)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("King Curtis Game")

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0

background = pygame.image.load("Background.png").convert()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, enemies, True)
    for enemy in hits:
        score += 1
        new_enemy = Enemy()
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)

    all_sprites.draw(screen)
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: {}".format(score),True,(255, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
