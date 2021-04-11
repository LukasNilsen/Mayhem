"""
Author: Lukas Nilsen & Adrian L Moen

TEXT TEXT TEXT TEXT TEXT TEXT
"""

import pygame
from ship import Ship
from config import keyboard


class Player(Ship):
    def __init__(self, left, right, thrust, fire, player_number):
        super().__init__(player_number)

        self.left_key = keyboard[left]
        self.right_key = keyboard[right]
        self.thrust_key = keyboard[thrust]
        self.fire_key = keyboard[fire]

        self.player = player_number

        self.score = 0


    def input(self, keys):

        strokes = []
        if keys[self.left_key]:
            strokes.append("left")
        if keys[self.right_key]:
            strokes.append("right")
        if keys[self.thrust_key]:
            strokes.append("thrust")
        if keys[self.fire_key]:
            strokes.append("fire")

        self.action(strokes)






