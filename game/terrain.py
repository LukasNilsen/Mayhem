"""
Author: Lukas Nilsen & Adrian L Moen
"""

import pygame
from game.config import brick_config, SCREEN_X, SCREEN_Y, SCREEN_START

EXAMPLE_MAP = r"resources\example_map.png"

class Terrain(pygame.sprite.Sprite):
    """

    """
    def __init__(self):
        super().__init__()

        self.pos = pygame.Vector2([0, SCREEN_START])

        self.image = pygame.image.load(EXAMPLE_MAP).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
        self.mask = pygame.mask.from_surface(self.image)