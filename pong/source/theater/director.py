import pygame
import sys
import theater
import theater.config as config
from random import randint

class Director:
    def __init__(self):
        pygame.init()
        self.stage = pygame.display.set_mode( config.SCREEN_SIZE )
        pygame.display.set_caption("pong")
        self.clock = pygame.time.Clock()
        
        self.player = theater.actor.ControlActor(48, 172)
        self.player.image.fill(theater.color.MAGENTA)
        
        self.ball = theater.actor.RandomActor(24, 24)
        self.ball.image.fill(theater.color.PINK)
        
        self.enemy = theater.actor.AutoActor(48, 172)
        self.enemy.image.fill(theater.color.PURPLE)
        self.enemy.target = self.ball
        
        self.paddles = pygame.sprite.Group()
        self.paddles.add(self.player, self.enemy)
        
        self.SingleBall = pygame.sprite.GroupSingle()
        self.SingleBall.add(self.ball)
        
        self.ball.rect.center = (config.SCREEN_SIZE[0]/2, config.SCREEN_SIZE[1]/2)
        self.player.rect.center = (config.SCREEN_SIZE[0] - 64, config.SCREEN_SIZE[1]/2 - 24)
        self.enemy.rect.center = (64, config.SCREEN_SIZE[1]/2 - 24)
        
        self.plaudit = theater.plaudit.Plaudit()
        self.plaudit.subscribe(self.player)
        #self.plaudit.subscribe(self.enemy)
    
    def collision(self):
        collide = pygame.sprite.spritecollide(self.ball, self.paddles, False)
        
        if collide:
            paddle = collide[0].rect
            if abs(self.ball.rect.right - paddle.left) < 10 and self.ball.direction.x > 0:
                self.ball.direction.x = -1
            if abs(self.ball.rect.left - paddle.right) < 10 and self.ball.direction.x < 0:
                self.ball.direction.x = 1
    
    def wallCollision(self):
        if self.ball.rect.right >= config.SCREEN_SIZE[0]:
            self.reset()
        if self.ball.rect.left <= 0:
            self.reset()
        if self.ball.rect.bottom >= config.SCREEN_SIZE[1]:
            self.ball.rect.bottom = config.SCREEN_SIZE[1]
            self.ball.direction.y *= -1
        if self.ball.rect.top <= 0:
            self.ball.rect.top = 0
            self.ball.direction.y *= -1
        
        for paddle in self.paddles.sprites():
            if paddle.rect.top <= 0 and paddle.direction.y == -1:
                paddle.rect.top = 0
                paddle.direction.y = 0
            if paddle.rect.bottom >= config.SCREEN_SIZE[1] and paddle.direction.y == 1:
                paddle.rect.bottom = config.SCREEN_SIZE[1]
                paddle.direction.y = 0
    
    def reset(self):
        # Reset the ball to the center of the screen and change its direction
        self.ball.rect.centerx = config.SCREEN_SIZE[0] // 2 - self.ball.rect.width // 2
        self.ball.rect.centery = config.SCREEN_SIZE[1] // 2 - self.ball.rect.height // 2
        self.ball.direction.x = randint(-100, 101)
        self.ball.direction.y = randint(-30, 30)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.plaudit.update()
            self.player.update()
            self.ball.update()
            self.enemy.followTarget(self.ball.rect.y)
            self.enemy.update()
            
            self.wallCollision()
            self.collision()
            
            self.stage.fill("black")
            
            self.paddles.draw(self.stage)
            self.SingleBall.draw(self.stage)
            
            print(self.clock.get_fps())
            
            pygame.display.update()
            self.clock.tick(config.FPS)