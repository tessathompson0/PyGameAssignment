#Tessa Thompson
#10.18.23
#King Curtis Game

#import stuff
import pygame
from player import Player
from enemy import Enemy
from enemy import goodEnemy
from enemy import Enemy2
from enemy import Enemy3
from enemy import Enemy4
from enemy import Enemy5
from enemy import goodEnemy2
from enemy import goodEnemy3
from enemy import goodEnemy4

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
enemies2 = pygame.sprite.Group()
enemies3 = pygame.sprite.Group()
enemies4 = pygame.sprite.Group()
enemies5 = pygame.sprite.Group()
goodEnemies = pygame.sprite.Group()
goodEnemies2 = pygame.sprite.Group()
goodEnemies3 = pygame.sprite.Group()
goodEnemies4 = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

#spawn sprites
for i in range(2):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)
for i in range(2):
    goodenemy = goodEnemy()
    all_sprites.add(goodenemy)
    goodEnemies.add(goodenemy)
for i in range(2):
    enemy2 = Enemy2()
    all_sprites.add(enemy2)
    enemies2.add(enemy2)
for i in range(2):
    enemy3 = Enemy3()
    all_sprites.add(enemy3)
    enemies3.add(enemy3)
for i in range(2):
    enemy4 = Enemy4()
    all_sprites.add(enemy4)
    enemies4.add(enemy4)
for i in range(2):
    enemy5 = Enemy5()
    all_sprites.add(enemy5)
    enemies5.add(enemy5)
for i in range(2):
    goodenemy2 = goodEnemy2()
    all_sprites.add(goodenemy2)
    goodEnemies2.add(goodenemy2)
for i in range(2):
    goodenemy3 = goodEnemy3()
    all_sprites.add(goodenemy3)
    goodEnemies2.add(goodenemy3)
for i in range(2):
    goodenemy4 = goodEnemy4()
    all_sprites.add(goodenemy4)
    goodEnemies4.add(goodenemy4)

#start a score system
score = 0

#make background a png image
background = pygame.image.load("Background.png").convert()
#make background if you win
youWin = pygame.image.load("YouWin.png").convert()
#make background if you lose
youLose = pygame.image.load("YouLose.png").convert()
#make welcome message load
welcomeMessage = pygame.image.load("WelcomeMessage.png").convert()

#game start/end variables
game_started = False
game_over = False

#keep running until x button is pushed
running = True
while running:
    for event in pygame.event.get():
        #if person presses x
        if event.type == pygame.QUIT:
            running = False
        #starts game if background is pressed
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_started:
            game_started = True
        #welcome message stays until button is clicked
    if not game_started:
        screen.blit(welcomeMessage, (0,0))
    else:
        #make background appear
        screen.blit(background, (0,0))
        all_sprites.update()
        #collision between player and wife swap mom (-10 points)
        hits = pygame.sprite.spritecollide(player, enemies, True)
        #collision between player and chicken nugget (+10 points)
        hits2 = pygame.sprite.spritecollide(player, goodEnemies, True)
        #collision between player and fruit (-4 points)
        hits3 = pygame.sprite.spritecollide(player, enemies2, True)
        #collision between player and Lettuce (-8 points)
        hits4 = pygame.sprite.spritecollide(player, enemies3, True)
        #collision between player and Tomato (-2 points)
        hits5 = pygame.sprite.spritecollide(player, enemies4, True)
        #collision between player and water (-1 point)
        hits6 = pygame.sprite.spritecollide(player, enemies5, True)
        #collision between player and bacon (+8 points)
        hits7 = pygame.sprite.spritecollide(player, goodEnemies2, True)
        #collision between player and soda (+2 points)
        hits8 = pygame.sprite.spritecollide(player, goodEnemies3, True)
        #collision between player and twinkies (+4 points)
        hits9 = pygame.sprite.spritecollide(player, goodEnemies4, True)
        #collision 1 (with wife swap mom)
        for enemy in hits:
            #change score
            score = score - 10
            #add new enemy to replace old enemy
            new_enemy = Enemy()
            all_sprites.add(new_enemy)
            enemies.add(new_enemy)
        #collision 2 (with chicken nugget)
        for goodenemy in hits2:
            #change
            score = score + 10
            new_goodEnemy = goodEnemy()
            all_sprites.add(new_goodEnemy)
            goodEnemies.add(new_goodEnemy)
        #collision 3 (with fruit)
        for enemy2 in hits3:
            #change score
            score = score - 4
            #add new enemy to replace old enemy
            new_enemy2 = Enemy2()
            all_sprites.add(new_enemy2)
            enemies2.add(new_enemy2)
        #collision 4 (with Lettuce)
        for enemy3 in hits4:
            #change score
            score = score - 8
            #add new enemy to replace old enemy
            new_enemy3 = Enemy3()
            all_sprites.add(new_enemy3)
            enemies3.add(new_enemy3)
        #collision 5 (with Tomato)
        for enemy4 in hits5:
            #change score
            score = score - 2
            #add new enemy to replace old enemy
            new_enemy4 = Enemy4()
            all_sprites.add(new_enemy4)
            enemies4.add(new_enemy4)
        #collision 6 (with Water)
        for enemy5 in hits6:
            #change score
            score = score - 2
            #add new enemy to replace old enemy
            new_enemy5 = Enemy5()
            all_sprites.add(new_enemy5)
            enemies5.add(new_enemy5)
        #collision 7 (with bacon)
        for goodenemy2 in hits7:
            #change score
            score = score + 8
            #add new enemy to replace old enemy
            new_goodEnemy2 = goodEnemy2()
            all_sprites.add(new_goodEnemy2)
            goodEnemies2.add(new_goodEnemy2)
        #collision 8 (with soda)
        for goodenemy3 in hits8:
            #change score
            score = score + 2
            #add new enemy to replace old enemy
            new_goodEnemy3 = goodEnemy3()
            all_sprites.add(new_goodEnemy3)
            goodEnemies3.add(new_goodEnemy3)
        #collision 8 (with Twinkies)
        for goodenemy4 in hits9:
        #change score
            score = score + 4
            #add new enemy to replace old enemy
            new_goodEnemy4 = goodEnemy4()
            all_sprites.add(new_goodEnemy4)
            goodEnemies4.add(new_goodEnemy4)

        #make sprites show up on screen
        all_sprites.draw(screen)
        #end game if you get 100 or more points (you win)
        if score >= 100:
            game_over = True
            screen.blit(youWin, (0,0))
        #end game if you get -50 points or less (you lose)
        if score <= -50:
            game_over = True
            screen.blit(youLose, (0,0))
        #show points scored
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: {}".format(score),True,(255, 0, 0))
        screen.blit(score_text, (10, 10))

    pygame.display.flip()
    #exit when game is over (wait 5 seconds to show message)
    if game_over:
        pygame.time.delay(5000)
        running = False

pygame.quit()
