"""
Author: Lukas Nilsen & Adrian L Moen
"""
import pygame
from config import itemConfig

FUEL = r"resources\Fuel.png"

class Item(pygame.sprite.Sprite):
    """

    """
    def __init__(self, x, y, item):
        super().__init__()

        self.pos = pygame.Vector2([x,y])

        self.width = itemConfig["width"]
        self.height = itemConfig["height"]
        self.activated = 0
        self.recipient = None
        self.type = item
        self.itemTypeCheck()


    def itemTypeCheck(self):
        if self.type == 1:
            print("fuel spawned", self.pos.x, self.pos.y, self.width, self.height)
            self.image = pygame.image.load(FUEL).convert_alpha()
            self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
            self.image_mask = pygame.mask.from_surface(self.image)


    def fuel(self):
        self.recipient.fuel = self.recipient.max_fuel

    def bomb(self):
        pass


    def ammo(self):
        pass

    def update(self):
        self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
        if self.activated:
            if self.type == 1:
                self.fuel()
            self.kill()

        