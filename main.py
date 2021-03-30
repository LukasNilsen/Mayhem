import pygame
from player import Player
from fire import Fire
from splitscreen import Splitscreen
from config import SCREEN_X, SCREEN_Y, bullet_config

pygame.init()
pygame.display.set_caption("Mayhem")

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

# TEST CODE:
player_group = pygame.sprite.Group()
all_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

player1 = Player("a", "d", "w", "space")
player2 = Player("left", "right", "up", "m")
player_group.add(player1, player2)

all_group.add(player1, player2)

hz = 144
clock = pygame.time.Clock()

splitscreen = Splitscreen(player1, player2, screen)

def main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Fill background
        screen.fill((160, 160, 160))

        time_passed = clock.tick(hz) / 1000.0

        # Log key inputs
        keys = pygame.key.get_pressed()

        for i in player_group:
            i.input(keys)

        if keys[player1.fire_key] and player1.reload == 0:
            f = Fire(player1.pos.x, player1.pos.y, player1.direction)
            bullet_group.add(f)
            all_group.add(f)
            player1.reload = bullet_config["reload_time"]

        if keys[player2.fire_key] and player2.reload == 0:
            f = Fire(player1.pos.x, player2.pos.y, player2.direction)
            bullet_group.add(f)
            all_group.add(f)
            player2.reload = bullet_config["reload_time"]

        # COMMENT OUT TO REMOVE SPLITSCREEN
        # splitscreen.update()

        all_group.update()
        all_group.draw(screen) # UNCOMMENT IF SPLITSCREEN ISN'T USED
        pygame.display.update()


if __name__ == "__main__":
    main()
