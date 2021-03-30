import pygame
from config import bullet_config

BULLET = r"resources\bullet.png"


class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()

        self.direction = direction
        self.pos = pygame.Vector2([x,y])
        self.speed = bullet_config["speed"]

        # Frames since it was birth
        self.since_birth = 0

        self.image = pygame.image.load(BULLET).convert_alpha()
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))

    def update(self):
        self.pos += self.direction.normalize() * self.speed
        self.rect.center = round(self.pos.x), round(self.pos.y)

        # Kills the bullet if it is out of the screen
        if self.pos.x > 1600 or self.pos.x < 0 or self.pos.y > 900 or self.pos.y < 0:
            self.kill()
