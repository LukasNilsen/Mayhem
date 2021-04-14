"""
Author: Lukas Nilsen & Adrian L Moen
"""

import pygame
from config import ship_config, bullet_config, world, SCREEN_X, SCREEN_Y

class Ship(pygame.sprite.Sprite):
    """
    A class to handle the ships

    Attributes:
    ----------
    pos : vector
        vector from [0,0] to the position of the ship
    direction : vector
        vector that points the same way the ship does
    acceleration : vector
        acceleration vector of forces acting on the ship
    velocity : vector
        vector of where the ship is moving (not pointing)
    gravity : vector
        gravity vector
    health : int
        current health of the ship
    bullets : int
        bullets left in "mag"
    alive : bol
    max_fuel : int
    max_bullets : int
    max_health : int

    Methods
    ----------
    action(keys) : None
        rotates, thrusts and/or shoots depending on input keys
    edges() : None
        if ship goes out of the screen, it goes to the opposite side of the screen
    collision(bullets, item, terrain) : None
        checks if there is a collision between ship and any of the parameters
    reset_ship()
        resets the ship to the __init__ state
    update()
        updates the position of the ship and checks if it's still has health left
    """
    def __init__(self, player_number):
        """
        Constructs the necessary attributes for the object.

        Parameters
        -----------
        player_number : int
            set the player number of the ship
        """
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

        SHIP1_OFF = ship_config["SHIP1_OFF"]
        SHIP2_OFF = ship_config["SHIP2_OFF"]
        SHIP1_ON = ship_config["SHIP1_ON"]
        SHIP2_ON = ship_config["SHIP2_ON"]
        
        self.EXPLOSION = ship_config["EXPLOSION"]

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

        # So the player can't shoot every iteration of main while loop
        self.reload = 0
        self.flameReload = 0

        # Ship starts out with max fuel, bullet and health
        self.fuel = self.max_fuel
        self.bullets = self.max_bullets
        self.health = self.max_health

        self.alive = True
        self.since_birth = 0    # Needed because first iteration of the game always says it has collided with terrain

        self.collisionIterations = 0
        self.currentOverlap = None
        self.newOverlap = None
        self.previousVelocity = self.velocity
        self.posCheck = True


    def action(self, keys):
        """
        Rotates, thrusts and/or shoots depending on key input

        Parameters
        ---------
        keys : list
            list of pygame.K_x ( x : key )
        """

        if "left" in keys:
            self.direction = self.direction.rotate(-1)
            self.angle += 1

        if "right" in keys:
            self.direction = self.direction.rotate(1)
            self.angle -= 1

        if "thrust" in keys and self.fuel > 0:
            self.acceleration = self.direction * 0.05
            self.engine_on = True
            self.fuel -= 0

        else:
            self.acceleration = [0, 0]
            self.engine_on = False

    def edges(self):
        """ If ship goes out of bounds, it appears on opposite side of screen"""
        if self.pos.x > SCREEN_X:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SCREEN_X
        if self.pos.y > SCREEN_Y:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = SCREEN_Y

    def collision(self, bullets, terrain, items):
        """
        Checks if ship crashes with bullets, terrain or items.

        Collision with bullets -> -x health
        Collision with terrain -> -x health and velocity *= -1
        Collision with items -> stuff happens depending on what item it "collides with"

        Parameters
        ----------
        bullets : list
            list of bullet-objects
        items : list
            list of item-objects
        terrain : terrain-object
        """

        # If ship gets hits by bullet or bullet hits terrain
        for i in bullets:

            # If bullet hits terrain
            bullet_terrain_offset = (int(i.rect.left - terrain.rect.left), int(i.rect.top - terrain.rect.top))
            bullet_terrain_collision = terrain.image_mask.overlap(i.image_mask, bullet_terrain_offset)
            if bullet_terrain_collision:
                i.kill()

            # If bullet hits ship
            if i.since_birth > bullet_config["priming_time"]:  # Bullet "priming time"
                bullet_ship_offset = (int(i.rect.left - self.rect.left), int(i.rect.top - self.rect.top))
                collision = self.image_mask.overlap(i.image_mask, bullet_ship_offset)

                # What happens when bullet hits ship
                if collision:
                    self.health -= 1
                    i.kill()


        # Checks if ship collides with terrain
        ship_terrain_offset = (int(terrain.rect.left - self.rect.left), int(terrain.rect.top - self.rect.top))
        ship_terrain_collision = self.image_mask.overlap(terrain.image_mask, ship_terrain_offset)

        # currentOverlap = self.image_mask.overlap_area(terrain.image_mask, ship_terrain_offset)

        # What happens when bullet hits ship
        # Im assuming you mean "What happens when ship hits terrain" with this one
        if ship_terrain_collision and self.since_birth > 20:
            
            #Simpel kollisjonstest, dersom testCollision returnerer 1, er det en høyre eller venstre kollisjon, og velocity.x endres, men funksjonen fungerer ikke enn så lenge, se nederst på siden
            if self.testCollision(terrain, ship_terrain_offset) == 1:
                self.velocity.x *= -1
            elif self.testCollision(terrain, ship_terrain_offset) == 2:
                self.velocity.y *= -1

            self.health -= 1


        # Checks if ship has health left
        if self.health <= 0:
            self.alive = False


        # Checks if ship "collides" with items
        for i in items:
            item_ship_offset = (int(i.rect.left-self.rect.left), int(i.rect.top-self.rect.top))
            item_collision = self.image_mask.overlap(i.image_mask, item_ship_offset)
            if item_collision:
                i.recipient = self
                i.activated = 1



    def update(self):
        """Updates the state of the ship"""
        # Only updates the state of the ship if it's still alive
        if self.alive:
            self.edges()
            self.since_birth += 1

            # Calculating the forces acting on the ship, and adding them to the velocity of it
            forces = self.acceleration + self.gravity
            self.velocity += forces
            self.velocity *= (1 - world["drag"])

            # Updating position of the ship
            if self.posCheck:
                self.pos += self.velocity
            

            # "Reloads" the gun and thrustanimation
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
            self.image = pygame.image.load(self.EXPLOSION)
            self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))

        self.image_mask = pygame.mask.from_surface(self.image)



    def reset_ship(self):
        """Resets the ship to __init__ state"""
        self.pos = pygame.Vector2([500, 200])
        self.direction = pygame.Vector2([0, -1])
        self.acceleration = pygame.Vector2([0, 0])
        self.velocity = pygame.Vector2([0, 0])

        self.angle = 0
        self.engine_on = 0

        self.image = self.ship_off
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))
        self.image_mask = pygame.mask.from_surface(self.image)

        self.reload = 0
        self.flameReload = 0
        self.fuel = self.max_fuel
        self.bullets = self.max_bullets
        self.health = self.max_health

        self.alive = True
        self.since_birth = 0



    # returns 1 if the decision is correct, see the collision handling 
    def testCollision(self, terrain, offset):

        """
        Tester for sidekollisjon, hvis ikke er det en top/bunn kollisjon
        """

        currentOverlap = self.image_mask.overlap(terrain.image_mask, offset)
        if currentOverlap:
            oldPos = self.pos
            self.pos.y -= self.velocity.y
            self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))
            offset = (int(terrain.rect.left - self.rect.left), int(terrain.rect.top - self.rect.top))
            self.posCheck = False
            self.update()
            sideOverlap = self.image_mask.overlap(terrain.image_mask, offset)
            self.posCheck = True

            if sideOverlap:
                self.pos = oldPos - self.velocity
                print("side collision")
                return 1
            
            print("over eller under kollisjon")
            self.pos = oldPos - self.velocity
            return 2