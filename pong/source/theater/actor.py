import pygame

# Theme:
# Use "Actor" for rects

class Actor(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__(self)
        
        self.surface = pygame.Surface( (width, height) )
        self.rect = self.surface.get_rect()