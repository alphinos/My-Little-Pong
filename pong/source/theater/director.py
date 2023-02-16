import pygame
import sys
import theater
import theater.config as config

class Director:
    def __init__(self):
        pygame.init()
        self.stage = pygame.display.set_mode( config.SCREEN_SIZE )
        pygame.display.set_caption("pong")
        self.clock = pygame.time.Clock()
        
        self.player = theater.actor.ControlActor(48, 172)
        self.player.surface.fill(theater.color.MAGENTA)
        
        self.enemy = theater.actor.ControlActor(48, 172)
        self.enemy.surface.fill(theater.color.PURPLE)
        
        self.player.rect.center = (config.SCREEN_SIZE[0] - 64, config.SCREEN_SIZE[1]/2 - 24)
        self.enemy.rect.center = (64, config.SCREEN_SIZE[1]/2 - 24)
        
        self.plaudit = theater.plaudit.Plaudit()
        self.plaudit.subscribe(self.player)
        self.plaudit.subscribe(self.enemy)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.plaudit.update()
            self.player.update()
            self.enemy.update()
            
            self.stage.fill("black")
            
            self.stage.blit(self.player.surface, (self.player.rect.topleft))
            self.stage.blit(self.enemy.surface, (self.enemy.rect.topleft))
            
            pygame.display.update()
            self.clock.tick(config.FPS)