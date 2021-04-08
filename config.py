import pygame

# Maybe we shouldn't use dictionaries and instead just use variables? or a mix? We'll see.

# Perhaps variables, might be more coherent and easier to read with dictionaries?
# Maybe switch out w,a,d out with up left right etc... nvm see that it's needed for split screen, if we get far enough we could try hosting on a server, maybe sit down with a TA for that.
# NOTE: in main.py, everything should be in classes, no stray methods or functions, so we need to figure out a way to do that (this goes for the whole project fyi)

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
