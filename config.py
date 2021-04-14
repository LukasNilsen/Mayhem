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
    "max_bullets": 40,
    "max_health": 3,

    "SHIP1_OFF": r"resources\Player1.png",
    "SHIP2_OFF": r"resources\Player2.png",
    "SHIP1_ON": r"resources\Player1Moving.png",
    "SHIP2_ON": r"resources\Player2Moving.png",

    "EXPLOSION": r"resources\aaa.png"
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

itemPos = {
    "fuel1": [50, 100, 1, 32, 32],
    "fuel2": [50, 500, 1, 32, 32],
    "fuel3": [200, 400, 1, 32, 32],
    "fuel4": [600, 500, 1, 32, 32],
    "fuel5": [1000, 700, 1, 32, 32],
    "fuel6": [1270, 250, 1, 32, 32],
    "fuel7": [1500, 700, 1, 32, 32],
    "fuel8": [600, 500, 1, 32, 32],
    "fuel9": [1000, 700, 1, 32, 32],
    "fuel10": [1570, 250, 1, 32, 32],
    "fuel11": [1500, 400, 1, 32, 32],
    "fuel12": [1500, 600, 1, 32, 32],
    "fuel13": [1600, 600, 1, 32, 32],
    "fuel14": [1500, 700, 1, 32, 32],
    "fuel15": [1570, 800, 1, 32, 32],
    "fuel16": [1500, 890, 1, 32, 32],

    

    "ammo1": [50, 300, 3, 32, 32],
    "ammo2": [400, 700, 3, 32, 32],
    "ammo3": [1200, 700, 3, 32, 32]
}
