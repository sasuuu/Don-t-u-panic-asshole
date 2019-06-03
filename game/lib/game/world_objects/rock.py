import json
import os
import pygame
from lib.game.world_objects.world_object import WorldObject
from random import randint

rock_sprite = [pygame.image.load('config/assets/objects/Kamien1.png'),
               pygame.image.load('config/assets/objects/Kamien2.png'),
               pygame.image.load('config/assets/objects/Kamien3.png'),
               pygame.image.load('config/assets/objects/Kamien4.png')]

object_config = None
file_exists = os.path.isfile("config/object_config.json")
if file_exists:
    with open("config/object_config.json") as json_file:
        object_config = json.load(json_file)


class Rock(WorldObject):

    def __init__(self, x_coordinate=10, y_coordinate=10, width=70, height=70):
        self._x_coordinate = x_coordinate
        self.__real_x = x_coordinate
        self.__real_y = y_coordinate
        self._y_coordinate = y_coordinate
        self._width = width
        self._height = height
        self._width_collision = width
        self._height_collision = height
        self._move_left_corner_x = 0
        self._move_left_corner_y = 0
        self.__rand_sprite = randint(0, 3)
        self._sprite_path = rock_sprite[self.__rand_sprite]

        if self.__rand_sprite == 0:
            self._move_left_corner_y = object_config['rock1_move_left_corner_y']
            self._move_left_corner_x = object_config['rock1_move_left_corner_x']
            self._width_collision = object_config['rock1_width_collision']
            self._height_collision = object_config['rock1_height_collision']

        elif self.__rand_sprite == 1:
            self._move_left_corner_y = object_config['rock2_move_left_corner_y']
            self._move_left_corner_x = object_config['rock2_move_left_corner_x']
            self._width_collision = object_config['rock2_width_collision']
            self._height_collision = object_config['rock2_height_collision']

        elif self.__rand_sprite == 2:
            self._move_left_corner_y = object_config['rock3_move_left_corner_y']
            self._move_left_corner_x = object_config['rock3_move_left_corner_x']
            self._width_collision = object_config['rock3_width_collision']
            self._height_collision = object_config['rock3_height_collision']

        elif self.__rand_sprite == 3:
            self._move_left_corner_y = object_config['rock4_move_left_corner_y']
            self._move_left_corner_x = object_config['rock4_move_left_corner_x']
            self._width_collision = object_config['rock4_width_collision']
            self._height_collision = object_config['rock4_height_collision']







