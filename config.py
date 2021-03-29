import pygame

# TODO: Write config file

# Maybe we shouldn't use dictionaries and instead just use variables? or a mix? We'll see.

SCREEN_X = 1280
SCREEN_Y = 720

world = {
    "gravity": 0.02,
    "drag": 0.01
}

ship_config = {
    "max_fuel": 100,
    "engine_strength": 1.02
}

keyboard = {
    "a": pygame.K_a,
    "d": pygame.K_d,
    "w": pygame.K_w,
    "space": pygame.K_SPACE,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "up": pygame.K_UP,
    "m": pygame.K_m
}
