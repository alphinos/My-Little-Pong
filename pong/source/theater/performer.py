import pygame

# Theme:
# Use "Performer" for masks

class Actor(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__(self)
        
        self.surface = pygame.Surface( (width, height) )
        self.mask = pygame.mask.from_surface( self.surface )