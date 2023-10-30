import pygame
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)
        self.speed = 5
    def update(self):
        keys = pygame.key.get_pressed()
        #go up
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        #go down
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        #go left
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        #go right
        if keys[pygame.K_d]:
            self.rect.x +=self.speed
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(600 - self.rect.height, self.rect.y))
