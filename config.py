import pygame

# Maybe we shouldn't use dictionaries and instead just use variables? or a mix? We'll see.

SCREEN_X = 1600
SCREEN_Y = 900

world = {
    "gravity": 0.00,
    "drag": 0.01
}

ship_config = {
    "max_fuel": 1000,
    "engine_strength": 1.02,
    "max_bullets": 30
}

bullet_config = {
    "speed": 5,
    "reload_time": 20,
    "priming_time": 20
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
