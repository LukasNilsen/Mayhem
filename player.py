import pygame
from ship import Ship
from config import *


class Player(Ship):
    def __init__(self, left, right, thrust, fire):
        super().__init__()

        self.left_key = keyboard[left]
        self.right_key = keyboard[right]
        self.thrust_key = keyboard[thrust]
        self.fire_key = keyboard[fire]

        self.fuel = self.max_fuel

    def input(self, keys):
        if keys[self.left_key]:
            self.action("left")
        if keys[self.right_key]:
            self.action("right")
        if keys[self.thrust_key]:
            self.action("thrust")

        else:
            self.action(None)
        if keys[self.fire_key]:
            self.action("fire")






