import pygame
from config import ship_config, bullet_config, world, SCREEN_X, SCREEN_Y

SHIP1_OFF = r"resources\Player1.png"
SHIP2_OFF = r"resources\Player2.png"
SHIP1_ON = r"resources\Player1Moving.png"
SHIP2_ON = r"resources\Player2Moving.png"

EXPLOSION = r"resources\explosion.png"


class Ship(pygame.sprite.Sprite):
    def __init__(self, player_number):
        super().__init__()

        self.pos = pygame.Vector2([500, 200])
        self.direction = pygame.Vector2([0, -1])
        self.acceleration = pygame.Vector2([0, 0])
        self.velocity = pygame.Vector2([0, 0])
        self.gravity = pygame.Vector2([0, 1]) * world["gravity"]

        # Angle -> Used to rotate the image, engine_on -> if the engine is on (to know which image to load)
        self.angle = 0
        self.engine_on = 0

        self.player_number = player_number

        self.max_fuel = ship_config["max_fuel"]
        self.max_bullets = ship_config["max_bullets"]
        self.max_health = ship_config["max_health"]

        # Loading image for engine_on and engine_off
        if self.player_number == 1:
            self.ship_on = pygame.image.load(SHIP1_ON)
            self.ship_off = pygame.image.load(SHIP1_OFF)
        if self.player_number == 2:
            self.ship_on = pygame.image.load(SHIP2_ON)
            self.ship_off = pygame.image.load(SHIP2_OFF)

        self.image = self.ship_off
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))
        self.image_mask = pygame.mask.from_surface(self.image)

        self.reload = 0
        self.flameReload = 0
        self.score = 0
        self.fuel = self.max_fuel
        self.bullets = self.max_bullets
        self.health = self.max_health

        self.alive = True
        self.alive_ctr = 0

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


    def collision(self, bullets, terrain, items):

        # If ship gets hits by bullet or bullet hits terrain
        for i in bullets:

            bullet_terrain_offset = (int(i.rect.left - terrain.rect.left), int(i.rect.top - terrain.rect.top))
            bullet_terrain_collision = terrain.image_mask.overlap(i.image_mask, bullet_terrain_offset)

            if bullet_terrain_collision:
                i.kill()

            if i.since_birth > bullet_config["priming_time"]:  # Bullet "priming time"
                bullet_ship_offset = (int(i.rect.left - self.rect.left), int(i.rect.top - self.rect.top))
                collision = self.image_mask.overlap(i.image_mask, bullet_ship_offset)

                if collision:
                    self.health -= 2
                    i.kill()

        # If ship crashes into terrain
        ship_terrain_offset = (int(terrain.rect.left - self.rect.left), int(terrain.rect.top - self.rect.top))
        ship_terrain_collision = self.image_mask.overlap(terrain.image_mask, ship_terrain_offset)
        
        if ship_terrain_collision and self.alive_ctr > 20:
            self.health -= 1

        if self.health == 0:
            self.alive = 0
        
        for i in items:
            item_ship_offset = (int(i.rect.left-self.rect.left), int(i.rect.top-self.rect.top))
            item_collision = self.image_mask.overlap(i.image_mask, item_ship_offset)
            if item_collision:
                i.recepient = self
                i.activated = 1

    def update(self):

        if self.alive:
            self.edges()

            self.alive_ctr += 1

            # Calculating the forces acting on the ship, and adding them to the velocity of it
            forces = self.acceleration + self.gravity
            self.velocity += forces
            self.velocity *= (1 - world["drag"])

            # Calculating the forces acting on the ship, and adding them to the velocity of it.
            # I've removed gravity as of now for testing purposes.
            forces = self.acceleration
            self.velocity += forces
            self.velocity *= (1 - world["drag"])
            # Updating position of the ship
            self.pos = self.pos + self.velocity

            # "Reloads" the gun
            if self.reload > 0:
                self.reload -= 1

            if self.flameReload > 0:
                self.flameReload -= 1

            # Different engine states
            if self.engine_on:
                rotated_image = pygame.transform.rotate(self.ship_on, self.angle)
                self.image = rotated_image
                self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))

            else:
                rotated_image = pygame.transform.rotate(self.ship_off, self.angle)
                self.image = rotated_image
                self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))

        if not self.alive:
            self.image = pygame.image.load(EXPLOSION)
            self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))
