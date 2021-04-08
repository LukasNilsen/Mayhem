import pygame

from config import SCREEN_X, SCREEN_Y, bullet_config, flameConfig
from fire import Fire
from player import Player
from ThrustAnimation import ThrustAnimation
from terrain import Terrain
from gui import GUI


class Game:
    
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Mayhem")

        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

        self.player_group = pygame.sprite.Group()
        self.all_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.terrain_group = pygame.sprite.Group()

        self.player1 = Player("a", "d", "w", "space", 1)
        self.player2 = Player("left", "right", "up", "m", 2)
        self.player_group.add(self.player1, self.player2)
        self.gui = GUI(self.player1, self.player2, self.screen)

        self.terrain = Terrain()

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

            time_passed = self.clock.tick(self.hz) / 1000.0

            # Log key inputs
            keys = pygame.key.get_pressed()

            for i in self.player_group:
                i.input(keys)

            if keys[self.player1.fire_key] and self.player1.reload == 0:
                f = Fire(self.player1.pos.x, self.player1.pos.y, self.player1.direction)
                self.bullet_group.add(f)
                self.all_group.add(f)
                self.player1.reload = bullet_config["reload_time"]

            if keys[self.player2.fire_key] and self.player2.reload == 0:
                f = Fire(self.player2.pos.x, self.player2.pos.y, self.player2.direction)
                self.bullet_group.add(f)
                self.all_group.add(f)
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
                player.hit(self.bullet_group)
                player.collision(self.terrain)

            self.all_group.update()
            self.all_group.draw(self.screen)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.main()
