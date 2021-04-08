import pygame

from config import SCREEN_X, SCREEN_Y, bullet_config, flameConfig
from fire import Fire
from player import Player
from splitscreen import Splitscreen
from ThrustAnimation import ThrustAnimation
from terrain import Terrain



# I've moved everything that was outside the loop, inside the __init__ might have to add self.[variableName] to most of this stuff

class Game():
    
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Mayhem")

        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

        # TEST CODE:
        self.player_group = pygame.sprite.Group()
        self.all_group = pygame.sprite.Group()
        self.terrain_group = pygame.sprite.Group()

        self.player1 = Player("a", "d", "w" , "space", 1)
        self.player2 = Player("left", "right", "up", "m", 2)
        self.player_group.add(self.player1, self.player2)

        self.all_group.add(self.player1, self.player2)

        self.hz = 144
        self.clock = pygame.time.Clock()

        splitscreen = Splitscreen(self.player1, self.player2, self.screen)

        self.generateTerrain()

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
                # trur ikke dissa trænges, bullet_group brukes ikke en så længe virke det som
                # bullet_group.add(f)
                self.all_group.add(f)
                self.player1.reload = bullet_config["reload_time"]

            if keys[self.player2.fire_key] and self.player2.reload == 0:
                f = Fire(self.player2.pos.x, self.player2.pos.y, self.player2.direction)
                # trur ikke dissa trænges, bullet_group brukes ikke en så længe virke det som
                # bullet_group.add(f)
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

            # COMMENT OUT TO REMOVE SPLITSCREEN
            # splitscreen.update()

            self.all_group.update()
            self.all_group.draw(self.screen) # UNCOMMENT IF SPLITSCREEN ISN'T USED
            pygame.display.update()

    def generateTerrain(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.main()
