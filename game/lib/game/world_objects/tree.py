import json
import os

import pygame
from lib.game.world_objects.world_object import WorldObject
from random import randint
# rock 1 = 69x66px

tree_sprite = [pygame.image.load('config/assets/objects/Drzewo1.png'),
               pygame.image.load('config/assets/objects/Drzewo2.png'),
               pygame.image.load('config/assets/objects/Drzewo3.png'),
               pygame.image.load('config/assets/objects/Drzewo4.png')]


object_config = None
file_exists = os.path.isfile("config/object_config.json")
if file_exists:
    with open("config/object_config.json") as json_file:
        object_config = json.load(json_file)


class Tree(WorldObject):

    def __init__(self, x_coordinate=100, y_coordinate=100, width=70, height=70):
        self._x_coordinate = x_coordinate
        self.__real_x = x_coordinate
        self.__real_y = y_coordinate
        self._y_coordinate = y_coordinate
        self._width_collision = width
        self._height_collision = height
        self._width = width
        self._height = height
        self.__rand_sprite = randint(0, 3)
        self._sprite_path = tree_sprite[self.__rand_sprite]
        self._move_left_corner_x = 125
        self._move_left_corner_y = 125

        if self.__rand_sprite == 0:
            self._move_left_corner_y = object_config['tree1_move_left_corner_y']
            self._move_left_corner_x = object_config['tree1_move_left_corner_x']
            self._width_collision = object_config['tree1_width_collision']
            self._height_collision = object_config['tree1_height_collision']

        elif self.__rand_sprite == 1:
            self._move_left_corner_y = object_config['tree2_move_left_corner_y']
            self._move_left_corner_x = object_config['tree2_move_left_corner_x']
            self._width_collision = object_config['tree2_width_collision']
            self._height_collision = object_config['tree2_height_collision']

        elif self.__rand_sprite == 2:
            self._move_left_corner_y = object_config['tree3_move_left_corner_y']
            self._move_left_corner_x = object_config['tree3_move_left_corner_x']
            self._width_collision = object_config['tree3_width_collision']
            self._height_collision = object_config['tree3_height_collision']

        elif self.__rand_sprite == 3:
            self._move_left_corner_y = object_config['tree4_move_left_corner_y']
            self._move_left_corner_x = object_config['tree4_move_left_corner_x']
            self._width_collision = object_config['tree4_width_collision']
            self._height_collision = object_config['tree4_height_collision']


