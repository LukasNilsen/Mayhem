"""
Author: Lukas Nilsen & Adrian L Moen
"""

import pygame
from game.config import SCREEN_X, SCREEN_START

pygame.font.init()
myfont = pygame.font.SysFont("calibri", 20)


class GUI():
    """
    A class to handle GUI

    Attributes:
    -----------
    screen : pygame.display
    player1 : player-object
    player2 : player-object

    Methods:
    -----------
    update() : None
        Re-render GUI and blit it to screen
    """

    def __init__(self, player1, player2, screen):
        """
        Constructs the necessary attributes for the object.

        Parameters
        -----------
        player1 : player-object
            direction and position taken from player1-object
        player2 : player-object
            direction and position taken from player2-object
        screen : pygame.display
            where GUI should be blit to
        """
        self.screen = screen
    
        self.player1 = player1
        self.player2 = player2

    def update(self):
        """ Re-renders the GUI-text with new values """

        pygame.draw.rect(self.screen, (0, 0, 0), (0,0, SCREEN_X, SCREEN_START))

        pygame.draw.rect(self.screen, (255*self.player1.health/self.player1.max_health, 0, 0), (SCREEN_X / 8 - 10,68, self.player1.health*2, 20))

        pygame.draw.rect(self.screen, (255*self.player2.health/self.player2.max_health, 0, 0), (SCREEN_X - SCREEN_X / 5 - 10,68, self.player2.health*2, 20))

        player1_score = myfont.render(f"Score: {self.player1.score}", False, (255,255,255))
        player2_score = myfont.render(f"Score: {self.player2.score}", False, (255,255,255))

        self.screen.blit(player1_score, (SCREEN_X / 100, 20))
        self.screen.blit(player2_score, (SCREEN_X - SCREEN_X / 100 - player2_score.get_width(), 20))
        
        if self.player1.fuel > self.player1.max_fuel / 4:
            player1_fuel = myfont.render(f"Fuel: {self.player1.fuel}", False, (255,255,255))
        else:
            player1_fuel = myfont.render(f"Fuel: {self.player1.fuel}", False, (255,0,0))
        if self.player2.fuel > self.player1.max_fuel / 4:
            player2_fuel = myfont.render(f"Fuel: {self.player2.fuel}", False, (255,255,255))
        else: 
            player2_fuel = myfont.render(f"Fuel: {self.player2.fuel}", False, (255,0,0))

        self.screen.blit(player1_fuel, (SCREEN_X / 10, 20))
        self.screen.blit(player2_fuel, (SCREEN_X - SCREEN_X / 10 - player2_fuel.get_width(), 20))

        player1_bullets = myfont.render(f"Bullets: {self.player1.bullets}", False, (255,255,255))
        player2_bullets = myfont.render(f"Bullets: {self.player2.bullets}", False, (255,255,255))
        self.screen.blit(player1_bullets, (SCREEN_X / 5, 20))
        self.screen.blit(player2_bullets, (SCREEN_X - SCREEN_X / 5 - player2_bullets.get_width(), 20))

        player1_health = myfont.render(f"HP: {self.player1.health}", False, (255,255,255))
        player2_health = myfont.render(f"HP: {self.player2.health}", False, (255,255,255))
        self.screen.blit(player1_health, (SCREEN_X / 8, 70))
        self.screen.blit(player2_health, (SCREEN_X - SCREEN_X / 5, 70))
        # pygame.draw.rect(self.screen, (255,0,0), pygame.Rect())




