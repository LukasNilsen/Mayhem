import pygame
from config import *                # change this

pygame.init()
pygame.display.set_caption("Mayhem")

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)


def main():

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()



if __name__ == "__main__":
    main()