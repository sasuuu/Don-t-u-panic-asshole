import pygame
from lib.game.world_objects.world_object import WorldObject
from random import randint
# rock 1 = 69x66px

tree_sprite = [pygame.image.load('config/assets/objects/Drzewo1.png'),
               pygame.image.load('config/assets/objects/Drzewo2.png'),
               pygame.image.load('config/assets/objects/Drzewo3.png'),
               pygame.image.load('config/assets/objects/Drzewo4.png')]


class Tree(WorldObject):

    def __init__(self, x_coordinate=100, y_coordinate=100, width=70, height=70):
        self._x_coordinate = x_coordinate
        self.__real_x = x_coordinate
        self.__real_y = y_coordinate
        self._y_coordinate = y_coordinate
        self._width = width
        self._height = height
        self.__rand = randint(0, 3)
        self._sprite_path = tree_sprite[self.__rand]
        self._mov_x = 125
        self._mov_y = 125

        if self.__rand == 1:
            self._mov_y = 100  # Y
            self._mov_x = 70  # X
            self._width = 100  # X
            self._height = 80  # Y
        elif self.__rand == 2:
            self._mov_y = 140   # Y
            self._mov_x = 140   # X
            self._width = 40  # X
            self._height = 40  # Y
        elif self.__rand == 3:
            self._mov_y = 130      # Y
            self._mov_x = 130      # X
            self._width = 40    # X
            self._height = 40   # Y
        elif self.__rand == 0:
            self._mov_y = 150    # Y
            self._mov_x = 125     # X
            self._width = 40    # X
            self._height = 40   # Y
