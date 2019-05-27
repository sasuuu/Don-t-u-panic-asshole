import pygame
from lib.game.world_objects.world_object import WorldObject
from random import randint

rock_sprite = [pygame.image.load('config/assets/objects/Kamien1.png'),
               pygame.image.load('config/assets/objects/Kamien2.png'),
               pygame.image.load('config/assets/objects/Kamien3.png'),
               pygame.image.load('config/assets/objects/Kamien4.png')]


class Rock(WorldObject):

    def __init__(self, x_coordinate=10, y_coordinate=10, width=70, heigth=70):
        self._x_coordinate = x_coordinate
        self.__real_x = x_coordinate
        self.__real_y = y_coordinate
        self._y_coordinate = y_coordinate
        self._width = width
        self._heigth = heigth
        self._sprite_path = rock_sprite[randint(0, 3)]
