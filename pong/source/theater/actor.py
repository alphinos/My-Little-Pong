import pygame
from pygame.locals import *
from random import randint

# Theme:
# Use "Actor" for rects

class Actor(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        
        self.image = pygame.Surface( (width, height) )
        self.rect = self.image.get_rect()
        
        self.direction = pygame.math.Vector2(0, 0)
        self.spd = 12
    
    def correctDir(self):
        if self.direction.length_squared() == 0 or self.direction.is_normalized():
            return
        self.direction.normalize_ip()
    
    def move(self):
        self.rect.centerx += self.direction.x * self.spd
        self.rect.centery += self.direction.y * self.spd
        
    def update(self):
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

class AutoActor(Actor):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.target = None
    
    def followTarget(self):
        if self.rect.top > self.target.rect.bottom + self.rect.height // 2:
            self.direction.y = -1
        if self.rect.bottom < self.target.rect.top - self.rect.height // 2:
            self.direction.y = 1
    
    def update(self):
        self.followTarget()
        self.correctDir()
        self.move()

class RandomActor(Actor):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.spd = randint(8, 12)
        self.changeX = self.changeDir(1)
        self.changeY = self.changeDir(-1)
        
        self.direction.x = randint(-100, 101)
        self.direction.y = randint(-30, 30)
    
    def changeDir(self, dir):
        def Xaxis():
            self.direction.x *= -1
        def Yaxis():
            self.direction.y *= -1
        
        if dir == 1:
            return Xaxis
        if dir == -1:
            return Yaxis