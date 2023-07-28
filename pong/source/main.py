
import pygame
from sys import exit

import time

class Time:
    def __init__( self ):
        self.delta_time = 0.0
        self.prev_time = time.time()
    def update( self ):
        current_time = time.time()
        self.delta_time = current_time - self.prev_time
        self.prev_time = current_time

# Configurações iniciais
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SCREEN_SIZE = ( SCREEN_WIDTH, SCREEN_HEIGHT )

FPS = 60

# Cores
WHITE = ( 255, 255, 255 )
BLACK = ( 0, 0, 0 )
RED = ( 255, 0, 0 )

def main():
    pygame.init()
    screen = pygame.display.set_mode( SCREEN_SIZE )
    pygame.display.set_caption( "pong" )

    # Tempo
    game_logic_time = Time()
    game_logic_fps = 120

    rendering_time = Time()
    rendering_fps = 60

    # Ball
    ball_size = 50
    ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    ball_spd = 300

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Update the game logic time
            game_logic_time.update()
            delta_time_logic = game_logic_time.delta_time
            
            # Ball movement
            keys = pygame.key.get_pressed()
            if  keys[ pygame.K_LEFT ]:
                ball_x -= ball_spd * delta_time_logic
            if keys[ pygame.K_RIGHT ]:
                ball_x += ball_spd * delta_time_logic
            if keys[ pygame.K_UP ]:
                ball_y -= ball_spd * delta_time_logic
            if keys[ pygame.K_DOWN ]:
                ball_y += ball_spd * delta_time_logic
            
            # Boundary
            ball_x = max( 0, min( SCREEN_WIDTH, ball_x ) )
            ball_y = max( 0, min( SCREEN_HEIGHT, ball_y ) )

            # Clear screen
            screen.fill( BLACK )

            #Draw
            pygame.draw.circle( screen, RED, ( int( ball_x ), int( ball_y ) ), ball_size // 2 )

            if rendering_time.delta_time == 0:
                rendering_time.delta_time  = 1

            # Draw FPS
            fps_font = pygame.font.SysFont( None, 32 )
            fps_text = fps_font.render( f"FPS: { int( 1 / rendering_time.delta_time ) }", True, WHITE )
            screen.blit( fps_text, ( 10, 10 ) )

            # Update display
            pygame.display.flip()

            # Cap the game logic fps
            pygame.time.Clock().tick( game_logic_fps )

            rendering_time.update()

            time_to_sleep = max( 0, 1.0 / rendering_fps - rendering_time.delta_time )
            time.sleep( time_to_sleep )


if __name__ == "__main__":
    main()