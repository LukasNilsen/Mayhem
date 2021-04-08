import pygame
from config import BrickConfig

class Terrain(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, type):
        super().__init__()
        self.pos = pygame.math.Vector2(x,y)
        self.width = width
        self.height = height
    
    def wall(self):
        