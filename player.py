import pygame
from ship import Ship
from config import keyboard


class Player(Ship):
    def __init__(self, left, right, thrust, fire):
        super().__init__()

        self.left_key = keyboard[left]
        self.right_key = keyboard[right]
        self.thrust_key = keyboard[thrust]
        self.fire_key = keyboard[fire]

        self.fuel = self.max_fuel

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






