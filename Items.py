import pygame
from config import itemConfig

Fuel = r"resources\Fuel.png"

# Author Adrian L Moen
class Item(pygame.sprite.Sprite):
    
    # Author Adrian L Moen
    def __init__(self, x, y, item):
        super().__init__()
        self.x = x
        self.y = y
        self.width = itemConfig["width"]
        self.height = itemConfig["height"]
        self.activated = 0
        self.recepient = None
        self.type = item
        self.itemTypeCheck()

    # Author Adrian L Moen
    def itemTypeCheck(self):
        if self.type == 1:
            print("fuel spawned", self.x, self.y, self.width, self.height)
            self.image = pygame.image.load(Fuel).convert_alpha()
            self.rect = self.image.get_rect(topleft=(self.x, self.y))
            self.image_mask = pygame.mask.from_surface(self.image)

    # Author Adrian L Moen
    def fuel(self):
        self.recepient.fuel = self.recepient.max_fuel

    # Author Adrian L Moen
    def Bomb(self):
        pass

    # Author Adrian L Moen
    def ammo(self):
        pass
    
    # Author Adrian L Moen
    def update(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        if self.activated:
            if self.type == 1:
                self.fuel()
            self.kill()

        