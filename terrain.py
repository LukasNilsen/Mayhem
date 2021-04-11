"""
Author: Lukas Nilsen & Adrian L Moen

TEXT TEXT TEXT TEXT TEXT TEXT
"""

import pygame
from config import brickConfig
from config import SCREEN_X, SCREEN_Y

EXAMPLE_MAP = r"resources\example_map2.png"

class Terrain(pygame.sprite.Sprite):
    """

    """
    def __init__(self):
        super().__init__()

        self.pos = pygame.Vector2([0, 0])

        self.image = pygame.image.load(EXAMPLE_MAP).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
        self.image_mask = pygame.mask.from_surface(self.image)


