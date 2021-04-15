"""
Author: Lukas Nilsen & Adrian L Moen
"""

import pygame

EXAMPLE_MAP = r"resources\example_map.png"

class Terrain(pygame.sprite.Sprite):
    """

    """
    def __init__(self):
        super().__init__()

        self.pos = pygame.Vector2([0, 0])

        self.image = pygame.image.load(EXAMPLE_MAP).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
        self.image_mask = pygame.mask.from_surface(self.image)