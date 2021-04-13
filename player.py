"""
Author: Lukas Nilsen & Adrian L Moen

TEXT TEXT TEXT TEXT TEXT TEXT
"""

import pygame
from ship import Ship
from config import keyboard


class Player(Ship):
    """
    A class to handle the Player

    Class inherits from Ship-class : check methods and attributes of that class

    Attributes:
    -----------
    left_key : pygame.KEYDOWN
        key to rotate player counterclockwise
    right_key : pygame.KEYDOWN
        key to rorate player clockwise
    thrust_key : pygame.KEYDOWN
        key to start the engine
    fire_key : pygame.KEYDOWN
        key to shoot
    player_number : int
        differentiates between players
    score : int
        how many points the player has

    Methods:
    -----------
    input(keys)
        makes a list of the key-input and calls action method from Ship
    """
    def __init__(self, left, right, thrust, fire, player_number):
        """
        Constructs the necessary attributes for the object.

        Parameters
        ----------
        left_key : pygame.KEYDOWN
            key to rotate player counterclockwise
        right_key : pygame.KEYDOWN
            key to rorate player clockwise
        thrust_key : pygame.KEYDOWN
            key to start the engine
        fire_key : pygame.KEYDOWN
            key to shoot
        player_number : int
            differentiates between players
        """
        super().__init__(player_number)

        self.left_key = keyboard[left]
        self.right_key = keyboard[right]
        self.thrust_key = keyboard[thrust]
        self.fire_key = keyboard[fire]

        self.player = player_number
        self.score = 0

    def input(self, keys):
        """
        Makes a list of keystrokes and calls Ship-method "action"

        Parameters
        -----------
        keys : pygame.key.get_pressed()
            keys pressed
        """
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






