import pygame


class Hero:

    def __init__(self, position):
        self.__sprite = pygame.image.load('config/assets/main_hero_run_right_0.png')
        self.__x = position[0]
        self.__y = position[1]
        self.__hp = 2
        self.__nick = 'elo'
        self.__items = []

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_position(self, position):
        self.__x = position[0]
        self.__y = position[1]

    def get_sprite(self):
        return self.__sprite
