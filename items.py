import pygame
from random import randint
from config import itemConfig, SCREEN_X, SCREEN_Y

FuelBarrel = r"resources\Fuel.png"
AmmoBox = r"resources\AmmoBox.png"
BULLET = r"resources\bullet.png"

# Author Adrian L Moen
class Item(pygame.sprite.Sprite):
    
    # Author Adrian L Moen
    def __init__(self, terrain, items):
        super().__init__()
        self.width = itemConfig["width"]
        self.height = itemConfig["height"]
        self.activated = 0
        self.recepient = None
        self.terrain = terrain
        self.items = items
        self.alreadyShot = 0
           
    def determineSpawn(self, itemType):

        if itemType == 1:
            self.image = pygame.image.load(FuelBarrel).convert_alpha()
        if itemType == 2:
            self.image = pygame.image.load(BULLET).convert_alpha()
        if itemType == 3:
            self.image = pygame.image.load(AmmoBox).convert_alpha()

        self.rect = self.image.get_rect(topleft=(randint(0, SCREEN_X-self.width), randint(0, SCREEN_Y-self.height)))
        self.image_mask = pygame.mask.from_surface(self.image)

        item_terrain_offset = (int(self.terrain.rect.left - self.rect.left), int(self.terrain.rect.top - self.rect.top))
        item_terrain_overlap = self.image_mask.overlap(self.terrain.image_mask, item_terrain_offset)

        while item_terrain_overlap:

            self.rect = self.image.get_rect(topleft=(randint(0, SCREEN_X-self.width), randint(0, SCREEN_Y-self.height)))

            item_terrain_offset = (int(self.terrain.rect.left - self.rect.left), int(self.terrain.rect.top - self.rect.top))
            item_terrain_overlap = self.image_mask.overlap(self.terrain.image_mask, item_terrain_offset)

            if item_terrain_overlap:
                continue

            for i in self.items:

                item_item_offset = (int(i.rect.left-self.rect.left), int(i.rect.top-self.rect.top))
                item_item_overlap = self.image_mask.overlap(i.image_mask, item_item_offset)
                
                if item_item_overlap:
                    print("")
                    print(int(i.rect.left-self.rect.left), int(i.rect.top-self.rect.top))
                    self.rect = self.image.get_rect(topleft=(randint(0, SCREEN_X-self.width), randint(0, SCREEN_Y-self.height)))
                    continue
            
                item_terrain_offset = (int(self.terrain.rect.left - self.rect.left), int(self.terrain.rect.top - self.rect.top))
                item_terrain_overlap = self.image_mask.overlap(self.terrain.image_mask, item_terrain_offset)
                
                if item_terrain_overlap:
                    self.rect = self.image.get_rect(topleft=(randint(0, SCREEN_X-self.width), randint(0, SCREEN_Y-self.height)))
                    continue
                else:
                    # print("spawned item at", self.rect.x, self.rect.y, "after correction")
                    break

            # print("spawned item at", self.rect.x, self.rect.y)
                    



class Fuel(Item):
    
    def __init__(self, terrain, items):
        super().__init__(terrain, items)
        super().determineSpawn(1)

    def update(self):
        if self.activated:
            self.recipient.fuel = self.recipient.max_fuel
            self.kill()



class Health(Item):

    def __init__(self, terrain, items):
        super().__init__(terrain, items)
        super().determineSpawn(2)

    def update(self):
        if self.activated:
            self.recipient.health += 40 
            self.kill()



class Ammo(Item):

    def __init__(self, terrain, items):
        super().__init__(terrain, items)
        super().determineSpawn(3)
    
    def update(self):
        if self.activated:
            self.recipient.bullets += 20 
            self.kill()