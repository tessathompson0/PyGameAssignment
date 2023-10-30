import pygame
import random
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(600 - self.rect.height)
        self.speed = 2
    def update(self):
        self.rect.x += random.choice([-1, 0, 1]) * self.speed
        self.rect.y += random.choice([-1, 0, 1]) * self.speed
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))
