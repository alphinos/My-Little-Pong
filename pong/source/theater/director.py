import pygame
import sys
import theater.config as config

class Director:
    def __init__(self):
        pygame.init()
        self.stage = pygame.display.set_mode( config.SCREEN_SIZE )
        pygame.display.set_caption("pong")
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.stage.fill("black")
            pygame.display.update()
            self.clock.tick(config.FPS)