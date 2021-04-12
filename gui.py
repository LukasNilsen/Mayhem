"""
Author: Lukas Nilsen & Adrian L Moen

TEXT TEXT TEXT TEXT TEXT TEXT
"""

import pygame
from config import SCREEN_X

pygame.font.init()
myfont = pygame.font.SysFont("calibri", 20)


class GUI():
    def __init__(self, player1, player2, screen):
        """ Initializes the GUI """
        self.screen = screen
        self.player1 = player1
        self.player2 = player2

    def update(self):
        """ Re-renders the GUI-text with new values """
        player1_score = myfont.render(f"Score: {self.player1.score}", False, (0,0,0))
        player2_score = myfont.render(f"Score: {self.player2.score}", False, (0, 0, 0))
        self.screen.blit(player1_score, (SCREEN_X / 4, 20))
        self.screen.blit(player2_score, (3 * SCREEN_X / 4, 20))

        player1_fuel = myfont.render(f"Fuel: {self.player1.fuel}", False, (0,0,0))
        player2_fuel = myfont.render(f"Fuel: {self.player2.fuel}", False, (0,0,0))
        self.screen.blit(player1_fuel, (SCREEN_X / 4, 40))
        self.screen.blit(player2_fuel, (3 * SCREEN_X / 4, 40))

        player1_bullets = myfont.render(f"Bullets: {self.player1.bullets}", False, (0,0,0))
        player2_bullets = myfont.render(f"Bullets: {self.player2.bullets}", False, (0,0,0))
        self.screen.blit(player1_bullets, (SCREEN_X / 4, 60))
        self.screen.blit(player2_bullets, (3 * SCREEN_X / 4, 60))




