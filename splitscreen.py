import pygame
from config import SCREEN_X, SCREEN_Y

# THIS IS A MESS - No need to read, just playing around with it
# Code isn't supposed to be pretty ;D

TESTMAP = r"resources\SPLITSCREEN_TEST.png"

SHIP_OFF = r"resources\rocketship.png"
SHIP_ON = r"resources\rocketship_thrust.png"

ship_on = pygame.image.load(SHIP_ON)
ship_off = pygame.image.load(SHIP_OFF)

img = pygame.image.load(TESTMAP)


class Splitscreen():
    def __init__(self, player1, player2, screen):

        self.player1 = player1
        self.player2 = player2
        self.screen = screen

    def player1_screen(self):
        self.screen.blit(img, (0, 0), (self.player1.pos.x - SCREEN_X / 4, self.player1.pos.y - SCREEN_Y / 2, SCREEN_X / 2, SCREEN_Y))

        if self.player1.engine_on == True:
            player1 = pygame.transform.rotate(ship_on, self.player1.angle)
            rect = player1.get_rect()
            self.screen.blit(player1, (SCREEN_X // 4 - rect.width/2, SCREEN_Y / 2 - rect.height/2))
        else:
            rotated_image = pygame.transform.rotate(ship_off, self.player1.angle)
            rect = rotated_image.get_rect()
            self.screen.blit(rotated_image, (SCREEN_X // 4 - rect.width/2, SCREEN_Y / 2 - rect.height/2))

        if - SCREEN_X / 4 < self.player1.pos.x - self.player2.pos.x < SCREEN_Y/4 and - SCREEN_Y/2 < self.player1.pos.y - self.player2.pos.y < SCREEN_Y / 2:
            player2 = pygame.transform.rotate(ship_off, self.player2.angle)
            rect = player2.get_rect()
            self.screen.blit(player2, (SCREEN_X // 4 + (self.player2.pos.x - self.player1.pos.x), SCREEN_Y / 2 + (self.player2.pos.y - self.player1.pos.x)))



    def player2_screen(self):
        self.screen.blit(img, (SCREEN_X/2, 0), (self.player2.pos.x - SCREEN_X / 4, self.player2.pos.y - SCREEN_Y / 2, SCREEN_X / 2, SCREEN_Y))

        if self.player2.engine_on == True:
            rotated_image = pygame.transform.rotate(ship_on, self.player2.angle)
            rect = rotated_image.get_rect()
            self.screen.blit(rotated_image, (3 * SCREEN_X // 4 - rect.width/2, SCREEN_Y / 2 - rect.height/2))
        else:
            rotated_image = pygame.transform.rotate(ship_off, self.player2.angle)
            rect = rotated_image.get_rect()
            self.screen.blit(rotated_image, (3 * SCREEN_X // 4 - rect.width/2, SCREEN_Y / 2 - rect.height/2))

    def update(self):
        self.player1_screen()
        self.player2_screen()
