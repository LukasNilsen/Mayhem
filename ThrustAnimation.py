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

    def __init__(self, playerPos, playerDirection, player):
        super().__init__()

        self.direction = playerDirection
        self.playerPos = playerPos
        self.playerDirection = playerDirection.normalize()
        self.pos = pygame.Vector2()

        self.angle = player.angle

        self.Frame1 = pygame.image.load(FRAME1)
        self.Frame2 = pygame.image.load(FRAME2)
        self.Frame3 = pygame.image.load(FRAME3)
        self.Frame4 = pygame.image.load(FRAME4)
        self.Frame5 = pygame.image.load(FRAME5)
        self.Frame6 = pygame.image.load(FRAME6)
        self.Frame7 = pygame.image.load(FRAME7)

        self.image = pygame.transform.rotate(self.Frame1, self.angle).convert_alpha()
        self.rect =self.image.get_rect(center=(round(self.playerPos.x-self.playerDirection.x*32), round(self.playerPos.y-self.playerDirection.y*32)))

        self.timer = 0

    def update(self):

        # might be wrong, but goes around 160 frames per second it seems
        self.timer += 1
        
        # Animates the flame
        if self.timer > 10 and self.timer < 15:
            self.image = pygame.transform.rotate(self.Frame2, self.angle).convert_alpha()

        elif self.timer > 20 and self.timer < 23:
            self.image = pygame.transform.rotate(self.Frame3, self.angle).convert_alpha()

        elif self.timer > 26 and self.timer < 29:
            self.image = pygame.transform.rotate(self.Frame4, self.angle).convert_alpha()

        elif self.timer > 29 and self.timer < 32:
            self.image = pygame.transform.rotate(self.Frame5, self.angle).convert_alpha()

        elif self.timer > 32 and self.timer < 35:
            self.image = pygame.transform.rotate(self.Frame6, self.angle).convert_alpha()
            
        elif self.timer > 35 and self.timer < 38:
            self.image = pygame.transform.rotate(self.Frame7, self.angle).convert_alpha()


        if self.timer > 38:
            self.kill()
