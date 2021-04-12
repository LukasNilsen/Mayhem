"""
Author: Lukas Nilsen & Adrian L Moen

TEXT TEXT TEXT TEXT TEXT TEXT
"""

import pygame

from config import SCREEN_X, SCREEN_Y, bullet_config, flameConfig, itemList, itemPos
from fire import Fire
from player import Player
from thrustanimation import ThrustAnimation
from terrain import Terrain
from gui import GUI
from items import Item

class Game:
    """

    """
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Mayhem")

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

        self.generateTerrain()
        self.generateItems()

        self.all_group.add(self.player1, self.player2, self.terrain)

        self.hz = 144
        self.clock = pygame.time.Clock()
        
        self.player1.pos = pygame.Vector2([200, 300])
        self.player2.pos = pygame.Vector2([SCREEN_X-200, 300])


    # Author Lukas Nilsen & Adrian L Moen
    def main(self):
        
        while True:
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # Fill background
            self.screen.fill((160, 160, 160))

            time_passed = self.clock.tick(self.hz) / 1000.0

            # Log key inputs
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                exit()

            for i in self.player_group:
                i.input(keys)

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
            
            # Handles the thruster flames animation the same way you handled the bullets
            if keys[self.player1.thrust_key] and self.player1.flameReload == 0:
                flame = ThrustAnimation(self.player1.pos, self.player1.direction, self.player1)
                self.all_group.add(flame)
                self.player1.flameReload = flameConfig["delay"]

            if keys[self.player2.thrust_key] and self.player2.flameReload == 0:
                flame = ThrustAnimation(self.player2.pos, self.player2.direction, self.player2)
                self.all_group.add(flame)
                self.player2.flameReload = flameConfig["delay"]

            for player in self.player_group:
                player.collision(self.bullet_group, self.terrain, self.item_group)

            self.all_group.update()
            self.all_group.draw(self.screen)
            self.gui.update()
            pygame.display.update()
    
    def generateTerrain(self):
        self.terrain = Terrain()
    
    # Author Adrian L Moen
    def generateItems(self):
        
        for i in itemPos:

            fuel = Item (itemPos[i][0], itemPos[i][1], itemPos[i][2])

            self.item_group.add(fuel)

            self.all_group.add(fuel)




if __name__ == "__main__":
    game = Game()
    game.main()
