import pygame
import random

def randSignal():
    n = random.randint(-1, 1)
    if n == 0:
        return 1
    return n

def timer(last, time, callback):
    current = pygame.time.get_ticks()
    if current - last >= time:
        callback()
        return current