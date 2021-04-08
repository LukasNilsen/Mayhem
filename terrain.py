import pygame
from config import BrickConfig

from config import SCREEN_X, SCREEN_Y

EXAMPLE_MAP_1 = r"resources\example_map.png"
TEST = r"resources\test_test.png"


class Terrain(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, type):
        super().__init__()

        self.pos = pygame.Vector2([0, 0])

        self.image = pygame.image.load(EXAMPLE_MAP_1).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
        self.image_mask = pygame.mask.from_surface(self.image)


