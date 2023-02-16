
import pygame

class Plaudit:
    def __init__(self):
        self.audience = set()
    
    def subscribe(self, watcher):
        self.audience.add(watcher)
    
    def notifyAudience(self, keys):
        for watcher in self.audience:
            watcher.plaudit(keys)
    
    def getInput(self):
        keysPressed = pygame.key.get_pressed()
        return keysPressed
    
    def update(self):
        keys = self.getInput()
        self.notifyAudience(keys)
        