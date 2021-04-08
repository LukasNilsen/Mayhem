import pygame
from fire import Fire
from config import ship_config, world, SCREEN_X, SCREEN_Y

SHIP1_OFF = r"resources\Player1.png"
SHIP2_OFF = r"resources\Player2.png"
SHIP1_ON = r"resources\Player1Moving.png"
SHIP2_ON = r"resources\Player2Moving.png"

class Ship(pygame.sprite.Sprite):
    def __init__(self, playerNr):
        super().__init__()

        self.pos = pygame.Vector2([500, 200])
        self.direction = pygame.Vector2([0, -1])
        self.acceleration = pygame.Vector2([0, 0])
        self.velocity = pygame.Vector2([0, 0])
        self.gravity = pygame.Vector2([0, 1]) * world["gravity"]

        # Angle -> Used to rotate the image, engine_on -> if the engine is on (to know which image to load)
        self.angle = 0
        self.engine_on = 0

        self.playerNr = playerNr

        self.max_fuel = ship_config["max_fuel"]

        # Loads the ship image
        if self.playerNr == 1:
            self.image = pygame.image.load(SHIP1_OFF).convert_alpha()
            self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))
        
        if self.playerNr == 2:
            self.image = pygame.image.load(SHIP2_OFF).convert_alpha()
            self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))

        self.reload = 0
        self.flameReload = 0
        self.score = 0

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


    def edges(self):

        if self.pos.x > SCREEN_X:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SCREEN_X
        if self.pos.y > SCREEN_Y:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = SCREEN_Y

    def update(self):

        #self.edges()

        # Calculating the forces acting on the ship, and adding them to the velocity of it.
        # I've removed gravity as of now for testing purposes.
        forces = self.acceleration
        self.velocity += forces
        self.velocity *= (1 - world["drag"])

        # Updating position of the ship
        self.pos = self.pos + self.velocity

        # Loading image for engine_on and engine_off
        if self.playerNr == 1:
            ship_on = pygame.image.load(SHIP1_ON)
            ship_off = pygame.image.load(SHIP1_OFF)
        if self.playerNr == 2:
            ship_on = pygame.image.load(SHIP2_ON)
            ship_off = pygame.image.load(SHIP2_OFF)

        # "Reloads" the gun
        if self.reload > 0:
            self.reload -= 1
        
        if self.flameReload > 0:
            self.flameReload -= 1

        # Different engine states
        if self.engine_on == True:
            rotated_image = pygame.transform.rotate(ship_on, self.angle)
            self.image = rotated_image
            self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))
        else:
            rotated_image = pygame.transform.rotate(ship_off, self.angle)
            self.image = rotated_image
            self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))