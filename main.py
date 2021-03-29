import pygame
from player import Player
from config import *  # change this

pygame.init()
pygame.display.set_caption("Mayhem")

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

# TEST CODE:
all_group = pygame.sprite.Group()
a = Player("a", "d", "w", "space")
b = Player("left", "right", "up", "m")
all_group.add(a, b)

hz = 144
clock = pygame.time.Clock()


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

        for i in all_group:
            i.input(keys)

        all_group.update()
        all_group.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
