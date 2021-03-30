import pygame
from config import bullet_config

BULLET = r"resources\bullet.png"


class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()

        self.direction = direction
        self.pos = pygame.Vector2([x,y])
        self.speed = bullet_config["speed"]

        self.image = pygame.image.load(BULLET).convert_alpha()
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))

    def update(self):
        self.pos += self.direction.normalize() * self.speed
        self.rect.center = round(self.pos.x), round(self.pos.y)