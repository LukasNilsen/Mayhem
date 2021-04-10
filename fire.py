import pygame
from config import bullet_config, SCREEN_X, SCREEN_Y

BULLET = r"resources\bullet.png"

class Fire(pygame.sprite.Sprite):
    """

    """
    def __init__(self, player):
        super().__init__()

        self.direction = player.direction
        self.pos = pygame.Vector2([player.pos.x + self.direction.x * 20, player.pos.y + self.direction.y * 20])
        self.speed = bullet_config["speed"]

        self.image = pygame.image.load(BULLET).convert_alpha()
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))
        self.image_mask = pygame.mask.from_surface(self.image)

        self.since_birth = 0

    def update(self):
        self.pos += self.direction.normalize() * self.speed
        self.rect.center = round(self.pos.x), round(self.pos.y)

        self.since_birth += 1

        # Kills the bullet if it is out of the screen
        if self.pos.x > SCREEN_X or self.pos.x < 0 or self.pos.y > SCREEN_Y or self.pos.y < 0:
            self.kill()
