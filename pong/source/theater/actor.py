import pygame
from pygame.locals import *

# Theme:
# Use "Actor" for rects

class Actor(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        
        self.surface = pygame.Surface( (width, height) )
        self.rect = self.surface.get_rect()
        
        self.direction = pygame.math.Vector2(0, 0)
        self.spd = 8
    
    def correctDir(self):
        if self.direction.length_squared() == 0 or self.direction.is_normalized():
            return
        self.direction.normalize_ip()
    
    def move(self):
        self.rect.centerx += self.direction.x * self.spd
        self.rect.centery += self.direction.y * self.spd
        
        
    def update(self):
        print(self.direction.x, self.direction.y)
        self.correctDir()
        self.move()
        
class ControlActor(Actor):
    
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def plaudit(self, keys):
        self.direction.x = 0
        self.direction.y = 0
        
        if keys[pygame.K_UP]:
            self.direction.y += -1
        if keys[pygame.K_DOWN]:
            self.direction.y += 1
        if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            self.direction.y = 0