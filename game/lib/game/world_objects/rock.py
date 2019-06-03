import pygame
from lib.game.world_objects.world_object import WorldObject
from random import randint

rock_sprite = [pygame.image.load('config/assets/objects/Kamien1.png'),
               pygame.image.load('config/assets/objects/Kamien2.png'),
               pygame.image.load('config/assets/objects/Kamien3.png'),
               pygame.image.load('config/assets/objects/Kamien4.png')]


class Rock(WorldObject):

    def __init__(self, x_coordinate=10, y_coordinate=10, width=70, height=70):
        self._x_coordinate = x_coordinate
        self.__real_x = x_coordinate
        self.__real_y = y_coordinate
        self._y_coordinate = y_coordinate
        self._width = width
        self._height = height
        self._mov_x = 0
        self._mov_y = 0
        self.__rand = randint(0, 3)
        self._sprite_path = rock_sprite[self.__rand]

        if self.__rand == 1:
            self._mov_y = 50  # 15  # Y
            self._mov_x = 20  # 20  # X
            self._width = 155  # 160  # X
            self._height = 130  # 165  # Y
        elif self.__rand == 2:
            self._mov_y = 70    # 30   # Y
            self._mov_x = 40    # 20   # X
            self._width = 140   # 160  # X
            self._height = 90   # 140  # Y
        elif self.__rand == 3:
            self._mov_y = 70  # 30      # Y
            self._mov_x = 20  # 20      # X
            self._width = 155  # 155    # X
            self._height = 90  # 140   # Y
        elif self.__rand == 0:
            self._mov_y = 15     # Y
            self._mov_x = 15     # X
            self._width = 70    # X
            self._height = 70   # Y




