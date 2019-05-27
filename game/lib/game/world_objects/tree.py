import pygame
from lib.game.world_objects.world_object import WorldObject
from random import randint
# rock 1 = 69x66px

tree_sprite = [pygame.image.load('config/assets/objects/Drzewo1.png'),
               pygame.image.load('config/assets/objects/Drzewo2.png'),
               pygame.image.load('config/assets/objects/Drzewo3.png'),
               pygame.image.load('config/assets/objects/Drzewo4.png')]


class Tree(WorldObject):

    def __init__(self, x_coordinate=100, y_coordinate=100, width=70, heigth=70):
        self._x_coordinate = x_coordinate
        self.__real_x = x_coordinate
        self.__real_y = y_coordinate
        self._y_coordinate = y_coordinate
        self._width = width
        self._heigth = heigth
        self._sprite_path = tree_sprite[randint(0, 3)]
