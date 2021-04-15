"""
Author: Lukas Nilsen & Adrian L Moen
"""

import pygame
import time

from game.config import SCREEN_X, SCREEN_Y, SCREEN_START, bullet_config, flame_config, item_list
from game.fire import Fire
from game.player import Player
from game.thrustanimation import ThrustAnimation
from game.terrain import Terrain
from game.gui import GUI
from game.items import *

pygame.init()
pygame.display.set_caption("Mayhem")
pygame.font.init()
myfont = pygame.font.SysFont("calibri", 60)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

        self.player_group = pygame.sprite.Group()
        self.all_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.terrain_group = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()

        self.player1 = Player("a", "d", "w", "space", 1)
        self.player2 = Player("left", "right", "up", "m", 2)
        self.player_group.add(self.player1, self.player2)
        self.gui = GUI(self.player1, self.player2, self.screen)

        self.generate_terrain()
        self.generate_items()

        self.all_group.add(self.player1, self.player2, self.terrain)

        self.hz = 144
        self.clock = pygame.time.Clock()

        self.player1.pos = pygame.Vector2([200, 400])
        self.player2.pos = pygame.Vector2([SCREEN_X - 200, 300])

    def main(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # Fill background
            self.screen.fill((160, 160, 160))

            self.check_alive()

            time_passed = self.clock.tick(self.hz) / 1000.0

            # Log key inputs
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                exit()

            for i in self.player_group:
                thrust, bullet = i.input(keys)
                if bullet:
                    self.bullet_group.add(bullet)
                    self.all_group.add(bullet)
                if thrust:
                    self.all_group.add(thrust)

                i.collision(self.bullet_group, self.terrain, self.item_group)



            self.all_group.update()
            self.all_group.draw(self.screen)
            self.gui.update()
            pygame.display.update()

    def generate_terrain(self):
        self.terrain = Terrain()

    def generate_items(self):
        """
        This method generates a given amount of certain items called once when the game initializes, and every time a player dies
        Items are random, but do not collide with terrain, every time
        """
        for i in range(9):
            fuel = Fuel(self.terrain, self.item_group)
            self.item_group.add(fuel)
            self.all_group.add(fuel)
        
        for i in range(7):
            ammo = Ammo(self.terrain, self.item_group)
            self.item_group.add(ammo)
            self.all_group.add(ammo)

        for i in range(4):
            health = Health(self.terrain, self.item_group)
            self.item_group.add(health)
            self.all_group.add(health)


    def reset_game(self):
        """
        Method that resets the game. Called when one of the players die.
        Does not change scores
        """
        for i in self.bullet_group:
            i.kill()

        for i in self.item_group:
            i.kill()

        self.generate_items()

        self.player1.reset_ship()
        self.player2.reset_ship()

        # Spawn position -> Should be worked into the code when we get a map
        self.player1.pos = pygame.Vector2([200, 400])
        self.player2.pos = pygame.Vector2([SCREEN_X - 200, 300])

    def wait(self):
        """
        Waiting method. Stops the game until Y is pressed. Called when one player dies.
        """
        while True:

            press_y_to_continue = myfont.render("Press 'Y' to Continue", False, (255, 255, 255))

            self.all_group.draw(self.screen)
            self.gui.update()
            self.screen.blit(press_y_to_continue, (SCREEN_X / 2 - press_y_to_continue.get_width() // 2, SCREEN_Y / 2))
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                    return

    def check_alive(self):
        """
        Checks if any of the players are dead.

        If a player is dead, the other player is rewarded with a point and the game.wait and game.reset_game are called
        """
        if self.player1.health <= 0:
            self.player2.score += 1

            self.wait()
            self.reset_game()

        if self.player2.health <= 0:
            self.player1.score += 1

            self.wait()
            self.reset_game()