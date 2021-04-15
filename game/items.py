import pygame
from random import randint
from game.config import item_config, SCREEN_X, SCREEN_Y, SCREEN_START

FuelBarrel = r"resources\Fuel.png"
AmmoBox = r"resources\AmmoBox.png"
HealthBox = r"resources\Health.png"

# Author Adrian L Moen
class Item(pygame.sprite.Sprite):
    
    # Author Adrian L Moen
    def __init__(self, terrain, items, Image):
        super().__init__()
        self.width = item_config["width"]
        self.height = item_config["height"]
        self.activated = 0
        self.recepient = None
        self.terrain = terrain
        self.items = items
        self.alreadyShot = 0
        self.image = pygame.image.load(Image).convert_alpha()
           
    def determine_spawn(self):
    
        self.rect = self.image.get_rect(topleft=(randint(0, SCREEN_X-self.width), randint(SCREEN_START, SCREEN_Y-self.height)))
        self.mask = pygame.mask.from_surface(self.image)

        item_terrain_offset = (int(self.terrain.rect.left - self.rect.left), int(self.terrain.rect.top - self.rect.top))
        item_terrain_overlap = self.mask.overlap(self.terrain.mask, item_terrain_offset)

        while pygame.sprite.spritecollideany(self, self.items) or item_terrain_overlap:
            self.rect = self.image.get_rect(topleft=(randint(0, SCREEN_X-self.width), randint(SCREEN_START, SCREEN_Y-self.height)))
            item_terrain_offset = (int(self.terrain.rect.left - self.rect.left), int(self.terrain.rect.top - self.rect.top))
            item_terrain_overlap = self.mask.overlap(self.terrain.mask, item_terrain_offset)


class Fuel(Item):
    
    def __init__(self, terrain, items):
        super().__init__(terrain, items, FuelBarrel)
        super().determine_spawn()

    def update(self):
        if self.activated:
            self.recipient.fuel = self.recipient.max_fuel
            self.kill()


class Health(Item):

    def __init__(self, terrain, items):
        super().__init__(terrain, items, HealthBox)
        super().determine_spawn()

    def update(self):
        if self.activated:
            self.recipient.health += 40 
            if self.recipient.health > 100:
                self.recipient.health = 100
            self.kill()


class Ammo(Item):

    def __init__(self, terrain, items):
        super().__init__(terrain, items, AmmoBox)
        super().determine_spawn()
    
    def update(self):
        if self.activated:
            self.recipient.bullets += 20 
            self.kill()