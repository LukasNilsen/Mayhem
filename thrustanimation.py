"""
Author: Lukas Nilsen & Adrian L Moen
"""

import pygame
from ship import Ship

FRAME1 = r"resources\Burst1.png"
FRAME2 = r"resources\Burst2.png"
FRAME3 = r"resources\Burst3.png"
FRAME4 = r"resources\Burst4.png"
FRAME5 = r"resources\Burst5.png"
FRAME6 = r"resources\Burst6.png"
FRAME7 = r"resources\Burst7.png"

class ThrustAnimation(pygame.sprite.Sprite):
    """

    """
    def __init__(self, player_position, player_direction, player):
        """

        """
        super().__init__()

        self.direction = player_direction
        self.player_pos = player_position
        self.player_direction = player_direction.normalize()
        self.pos = pygame.Vector2()

        self.angle = player.angle

        self.Frame1 = pygame.image.load(FRAME1).convert_alpha()
        self.Frame2 = pygame.image.load(FRAME2).convert_alpha()
        self.Frame3 = pygame.image.load(FRAME3).convert_alpha()
        self.Frame4 = pygame.image.load(FRAME4).convert_alpha()
        self.Frame5 = pygame.image.load(FRAME5).convert_alpha()
        self.Frame6 = pygame.image.load(FRAME6).convert_alpha()
        self.Frame7 = pygame.image.load(FRAME7).convert_alpha()

        self.image = pygame.transform.rotate(self.Frame1, self.angle).convert_alpha()
        self.rect =self.image.get_rect(center=(round(self.player_pos.x - self.player_direction.x * 32), round(self.player_pos.y - self.player_direction.y * 32)))

        self.timer = 0

    def update(self):

        self.timer += 1
        
        # Animates the flame
        if self.timer > 10 and self.timer < 15:
            self.image = pygame.transform.rotate(self.Frame2, self.angle)

        elif self.timer > 20 and self.timer < 23:
            self.image = pygame.transform.rotate(self.Frame3, self.angle)

        elif self.timer > 26 and self.timer < 29:
            self.image = pygame.transform.rotate(self.Frame4, self.angle)

        elif self.timer > 29 and self.timer < 32:
            self.image = pygame.transform.rotate(self.Frame5, self.angle)

        elif self.timer > 32 and self.timer < 35:
            self.image = pygame.transform.rotate(self.Frame6, self.angle)
            
        elif self.timer > 35 and self.timer < 38:
            self.image = pygame.transform.rotate(self.Frame7, self.angle)

        # self.player_pos -= self.player_direction
        # self.rect = self.image.get_rect(center=(round(self.player_pos.x - self.player_direction.x * 32), round(self.player_pos.y - self.player_direction.y * 32)))

        if self.timer > 38:
            self.kill()
