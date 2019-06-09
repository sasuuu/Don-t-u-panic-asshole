import pygame
from lib.game.world_objects.world_object import WorldObject


class Hero(WorldObject):

    def __init__(self, x_coordinate, y_coordinate, hp, nick, items, id, width=40, height=40):
        super().__init__(x_coordinate, y_coordinate, width, height)
        self._sprite_path = pygame.image.load('config/assets/main_hero_run_down_0.png')
        self.__id = id
        self.__hp = 2
        self.__nick = 'elo'
        self.__items = []

    def get_id(self):
        return self.__id
