import pygame
import random

#mom from wife swap sprite
class Enemy(pygame.sprite.Sprite):
    #load sprite
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        #keep sprite in screen
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(600 - self.rect.height)
        self.speed = 2
    #make sprite move randomly
    def update(self):
        self.rect.x += random.choice([-1, 0, 1]) * self.speed
        self.rect.y += random.choice([-1, 0, 1]) * self.speed
        #keep sprite in screen
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))
#chicken nugget sprite
class goodEnemy(pygame.sprite.Sprite):
    def __init__(self):
        #load sprite
        super().__init__()
        self.image = pygame.image.load("ChickenNugget.png").convert_alpha()
        self.rect = self.image.get_rect()
        #keep sprite in screen
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(600 - self.rect.height)
        self.speed = 2
    #make sprite move randomly
    def update(self):
        self.rect.x += random.choice([-1, 0, 1]) * self.speed
        self.rect.y += random.choice([-1, 0, 1]) * self.speed
        #keep sprite in screen
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))
#Bacon Sprite
class goodEnemy2(pygame.sprite.Sprite):
    def __init__(self):
        #load sprite
        super().__init__()
        self.image = pygame.image.load("Bacon.png").convert_alpha()
        self.rect = self.image.get_rect()
        #keep sprite in screen
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(600 - self.rect.height)
        self.speed = 2
    #make sprite move randomly
    def update(self):
        self.rect.x += random.choice([-1, 0, 1]) * self.speed
        self.rect.y += random.choice([-1, 0, 1]) * self.speed
        #keep sprite in screen
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))
#Soda Sprite
class goodEnemy3(pygame.sprite.Sprite):
    def __init__(self):
        #load sprite
        super().__init__()
        self.image = pygame.image.load("Soda.png").convert_alpha()
        self.rect = self.image.get_rect()
        #keep sprite in screen
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(600 - self.rect.height)
        self.speed = 2
    #make sprite move randomly
    def update(self):
        self.rect.x += random.choice([-1, 0, 1]) * self.speed
        self.rect.y += random.choice([-1, 0, 1]) * self.speed
        #keep sprite in screen
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))
#twinkie sprite
class goodEnemy4(pygame.sprite.Sprite):
    def __init__(self):
        #load sprite
        super().__init__()
        self.image = pygame.image.load("Twinkie.png").convert_alpha()
        self.rect = self.image.get_rect()
        #keep sprite in screen
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(600 - self.rect.height)
        self.speed = 2
    #make sprite move randomly
    def update(self):
        self.rect.x += random.choice([-1, 0, 1]) * self.speed
        self.rect.y += random.choice([-1, 0, 1]) * self.speed
        #keep sprite in screen
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))
#Fruit sprite
class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        #load sprite
        super().__init__()
        self.image = pygame.image.load("Fruit.png").convert_alpha()
        self.rect = self.image.get_rect()
        #keep sprite in screen
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(600 - self.rect.height)
        self.speed = 2
    #make sprite move randomly
    def update(self):
        self.rect.x += random.choice([-1, 0, 1]) * self.speed
        self.rect.y += random.choice([-1, 0, 1]) * self.speed
        #keep sprite in screen
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))
#Lettuce sprite
class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        #load sprite
        super().__init__()
        self.image = pygame.image.load("Lettuce.png").convert_alpha()
        self.rect = self.image.get_rect()
        #keep sprite in screen
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(600 - self.rect.height)
        self.speed = 2
    #make sprite move randomly
    def update(self):
        self.rect.x += random.choice([-1, 0, 1]) * self.speed
        self.rect.y += random.choice([-1, 0, 1]) * self.speed
        #keep sprite in screen
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))
#tomato sprite
class Enemy4(pygame.sprite.Sprite):
    def __init__(self):
        #load sprite
        super().__init__()
        self.image = pygame.image.load("Tomato.png").convert_alpha()
        self.rect = self.image.get_rect()
        #keep sprite in screen
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(600 - self.rect.height)
        self.speed = 2
    #make sprite move randomly
    def update(self):
        self.rect.x += random.choice([-1, 0, 1]) * self.speed
        self.rect.y += random.choice([-1, 0, 1]) * self.speed
        #keep sprite in screen
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))
#water sprite
class Enemy5(pygame.sprite.Sprite):
    def __init__(self):
        #load sprite
        super().__init__()
        self.image = pygame.image.load("Water.png").convert_alpha()
        self.rect = self.image.get_rect()
        #keep sprite in screen
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(600 - self.rect.height)
        self.speed = 2
    #make sprite move randomly
    def update(self):
        self.rect.x += random.choice([-1, 0, 1]) * self.speed
        self.rect.y += random.choice([-1, 0, 1]) * self.speed
        #keep sprite in screen
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))
