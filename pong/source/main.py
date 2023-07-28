
import pygame
from sys import exit
import config

def main():
    pygame.init()
    screen = pygame.display.set_mode( config.SCREEN_SIZE )
    pygame.display.set_caption("pong")
    clock = pygame.time.Clock()

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            
            
            print(clock.get_fps())
            pygame.display.update()
            clock.tick(config.FPS)

if __name__ == "__main__":
    main()