"""
Author: Lukas Nilsen & Adrian L Moen

TEXT TEXT TEXT TEXT TEXT TEXT
"""

import pygame
import time

from config import SCREEN_X, SCREEN_Y, bullet_config, flameConfig, itemList
from fire import Fire
from player import Player
from thrustanimation import ThrustAnimation
from terrain import Terrain
from gui import GUI
from items import Item




pygame.init()
pygame.display.set_caption("Mayhem")
pygame.font.init()
myfont = pygame.font.SysFont("calibri", 60)


class Game:
    """

    """
    def __init__(self):
        """

        """
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), pygame.FULLSCREEN)

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
        
        self.player1.pos = pygame.Vector2([200, 300])
        self.player2.pos = pygame.Vector2([SCREEN_X-200, 300])

    def main(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # Fill background
            self.screen.fill((160, 160, 160))

            self.check_alive()

            time_passed = self.clock.tick(self.hz) / 1000.0

            print(1/time_passed)

            # Log key inputs
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                exit()

            for i in self.player_group:
                i.input(keys)


            # Checks if "fire_key" is pressed, if the player has a shot ready, and if the player has bullets left
            if keys[self.player1.fire_key] and self.player1.reload == 0 and self.player1.bullets > 0:
                f = Fire(self.player1)
                self.bullet_group.add(f)
                self.all_group.add(f)
                self.player1.bullets -= 1
                self.player1.reload = bullet_config["reload_time"]

            if keys[self.player2.fire_key] and self.player2.reload == 0 and self.player2.bullets > 0:
                f = Fire(self.player2)
                self.bullet_group.add(f)
                self.all_group.add(f)
                self.player2.bullets -= 1
                self.player2.reload = bullet_config["reload_time"]

            if keys[self.player1.thrust_key] and self.player1.flameReload == 0 and self.player1.alive:
                flame = ThrustAnimation(self.player1.pos, self.player1.direction, self.player1)
                self.all_group.add(flame)
                self.player1.flameReload = flameConfig["delay"]

            if keys[self.player2.thrust_key] and self.player2.flameReload == 0 and self.player2.alive:
                flame = ThrustAnimation(self.player2.pos, self.player2.direction, self.player2)
                self.all_group.add(flame)
                self.player2.flameReload = flameConfig["delay"]

            for player in self.player_group:
                player.collision(self.bullet_group, self.terrain, self.item_group)

            self.all_group.update()
            self.all_group.draw(self.screen)
            self.gui.update()
            pygame.display.update()

    def generate_terrain(self):
        """

        """
        self.terrain = Terrain()

    def generate_items(self):
        """

        """
        fuel = Item(200, 200, itemList["fuel"])
        self.item_group.add(fuel)
        self.all_group.add(fuel)

    def reset_game(self):
        """
        Method that resets the game. Called when one of the players die.
        Does not change scores
        """

        for i in self.bullet_group:
            i.kill()

        self.player1.reset_ship()
        self.player2.reset_ship()

        # Spawn position -> Should be worked into the code when we get a map
        self.player1.pos = pygame.Vector2([200, 300])
        self.player2.pos = pygame.Vector2([SCREEN_X-200, 300])

    def wait(self):
        while True:


            press_y_to_continue = myfont.render("Press 'Y' to Continue", False, (0, 0, 0))
            self.screen.blit(press_y_to_continue, (SCREEN_X / 2 - press_y_to_continue.get_width()//2, SCREEN_Y / 2))

            self.all_group.draw(self.screen)
            self.gui.update()
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                    return

    def check_alive(self):
        if self.player1.health <= 0:
            self.player2.score += 1

            self.wait()
            self.reset_game()

        if self.player2.health <= 0:
            self.player1.score += 1

            self.wait()
            self.reset_game()


if __name__ == "__main__":
    game = Game()
    time.sleep(0.5) # To let objects initialize
    game.main()
