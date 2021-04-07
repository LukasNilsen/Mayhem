import pygame
from config import ship_config, bullet_config, world, SCREEN_X, SCREEN_Y

SHIP_OFF = r"resources\rocketship.png"
SHIP_ON = r"resources\rocketship_thrust.png"
EXPLOSION = r"resources\explosion.png"


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
        self.max_bullets = ship_config["max_bullets"]

        # Loads the ship image
        self.image = pygame.image.load(SHIP_OFF).convert_alpha()
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))
        self.image_mask = pygame.mask.from_surface(self.image)

        self.reload = 0
        self.score = 0
        self.fuel = self.max_fuel
        self.bullets = self.max_bullets

        self.alive = True

    def action(self, keys):

        if "left" in keys:
            self.direction = self.direction.rotate(-1)
            self.angle += 1

        if "right" in keys:
            self.direction = self.direction.rotate(1)
            self.angle -= 1

        if "thrust" in keys and self.fuel > 0:
            self.acceleration = self.direction * 0.05
            self.engine_on = True
            self.fuel -= 1

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

    def hit(self, bullets):

        for i in bullets:
            if i.since_birth > bullet_config["priming_time"]:      # Bullet "priming time"
                offset = (int(i.rect.left - self.rect.left), int(i.rect.top - self.rect.top))
                collision = self.image_mask.overlap(i.image_mask, offset)

                if collision:
                    self.alive = False

    def update(self):

        if self.alive:
            self.edges()

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

            # Different engine states
            if self.engine_on == True:
                rotated_image = pygame.transform.rotate(ship_on, self.angle)
                self.image = rotated_image
                self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))
            else:
                rotated_image = pygame.transform.rotate(ship_off, self.angle)
                self.image = rotated_image
                self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))

        else:
            self.image = pygame.image.load(EXPLOSION)
            self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))