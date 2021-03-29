import pygame
from config import ship_config
from config import world

SHIP_PNG = r"resources\ship_EXAMPLE.png"


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pass

        self.pos = pygame.Vector2([500, 200])
        self.direction = pygame.Vector2([0,-1])
        self.acceleration = pygame.Vector2([0, 0])
        self.velocity = pygame.Vector2([0, 0])

        self.forces = pygame.Vector2([0, 0])
        self.gravity = pygame.Vector2([0, 1]) * world["gravity"]

        # Import variables from the config file
        self.max_fuel = ship_config["max_fuel"]

        # Loads the ship image
        self.image = pygame.image.load(SHIP_PNG).convert_alpha()
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))

    def action(self, key):
        if key == "left":
            self.direction = self.direction.rotate(-1)
            self.velocity = self.velocity.rotate(-1)
        if key == "right":
            self.direction = self.direction.rotate(1)
            self.velocity = self.velocity.rotate(1)
        if key == "thrust":
            self.acceleration = self.direction * 0.05
        else:
            self.acceleration = [0, 0]
        if key == "fire":
            pass

    def update(self):

        self.forces = self.acceleration + self.gravity

        self.velocity += self.forces
        self.velocity *= (1 - world["drag"])

        self.pos = self.pos + self.velocity
        self.rect.center = round(self.pos.x), round(self.pos.y)



