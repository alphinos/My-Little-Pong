import pygame
import theater


class GlitterThrower():
    def __init__(self):
        self.glitter_ls = []
        self.last = pygame.time.get_ticks()

    def createGlitter(self, x= 50, y= 50, target = None):
        pos_x = x
        pos_y = y
        radius = 10
        direction = pygame.math.Vector2(0, -1)
        spd = 1
        if target is not None:
            pos_x = target.rect.centerx
            pos_y = target.rect.centery
            direction = target.direction * -1
        glitter_circle = [ [pos_x, pos_y], radius, direction, spd ]
        self.glitter_ls.append(glitter_circle)
        

    def destroyGlitter(self, glitter):
        pass

    def throwGlitter(self, surface):
        if self.glitter_ls:
            for glitter in self.glitter_ls:

                if not glitter[1] > 0:
                    self.glitter_ls.remove(glitter)
                    del glitter
                    continue

                glitter[0][0] += glitter[2][0] * glitter[3]
                glitter[0][1] += glitter[2][1] * glitter[3]

                glitter[3] *= 1.001
                glitter[3] = int(glitter[3])

                glitter[1] -= 0.2

                pygame.draw.circle(surface, pygame.Color("White"), glitter[0], int(glitter[1]) )
    
    def managing(self, time=50, target=None):
        current = pygame.time.get_ticks()
        if current - self.last >= time:
            self.createGlitter(target=target)
            self.last = current
