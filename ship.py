import pygame
from fire import Fire
from config import ship_config, world

SHIP_OFF = r"resources\rocketship.png"
SHIP_ON = r"resources\rocketship_thrust.png"


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.pos = pygame.Vector2([500, 200])
        self.direction = pygame.Vector2([0, -1])
        self.acceleration = pygame.Vector2([0, 0])
        self.velocity = pygame.Vector2([0, 0])
        self.gravity = pygame.Vector2([0, 1]) * world["gravity"]

        # Angle -> Used to rotate the image, engine_on -> if the engine is on (to know which image to load)
        self.angle = 0
        self.engine_on = 0

        self.max_fuel = ship_config["max_fuel"]

        # Loads the ship image
        self.image = pygame.image.load(SHIP_OFF).convert_alpha()
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))

        self.reload = 0

    def action(self, keys):
        if "left" in keys:
            self.direction = self.direction.rotate(-1)
            self.angle += 1

        if "right" in keys:
            self.direction = self.direction.rotate(1)
            self.angle -= 1

        if "thrust" in keys:
            self.acceleration = self.direction * 0.05
            self.engine_on = True

        else:
            self.acceleration = [0, 0]
            self.engine_on = False


    def update(self):

        # Calculating the forces acting on the ship, and adding them to the velocity of it
        forces = self.acceleration + self.gravity
        self.velocity += forces
        self.velocity *= (1 - world["drag"])

        # Updating position of the ship
        self.pos = self.pos + self.velocity

        # Loading image for engine_on and engine_off
        ship_on = pygame.image.load(SHIP_ON)
        ship_off = pygame.image.load(SHIP_OFF)

        # "Reloads" the gun
        if self.reload > 0:
            self.reload -= 1



        # Loads different engine
        if self.engine_on == True:
            rotated_image = pygame.transform.rotate(ship_on, self.angle)
            self.image = rotated_image
            self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))
        else:
            rotated_image = pygame.transform.rotate(ship_off, self.angle)
            self.image = rotated_image
            self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))