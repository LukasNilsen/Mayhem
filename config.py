import pygame

SCREEN_X = 1920
SCREEN_Y = 1080

world = {
    "gravity": 0.00,        # ~0.02 for "semi-realistic" gravity
    "drag": 0.01
}

ship_config = {
    "max_fuel": 1000,
    "engine_strength": 1.02,
    "max_bullets": 30,
    "max_health": 3
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
    "s": pygame.K_s,
    "space": pygame.K_SPACE,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "up": pygame.K_UP,
    "m": pygame.K_m
}

flameConfig = {
    "delay": 2,
    "animationTime": 700
}

brickConfig = {
    "Blue": (0, 0, 255),
    "Red": (255, 0, 0),
    "Green": (0, 255, 0)
}

itemConfig = {
    "width": 32,
    "height": 32
}

itemList = {
    "fuel": 1,
    "bomb": 2,
    "ammo": 3
}
