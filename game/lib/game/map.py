import pygame


class Map:

    def __init__(self, game):
        self.__game = game
        self.__grass_texture = pygame.image.load('config/assets/terrain/grass.png')
        self.__grass_size = self.__grass_texture.get_size()
        self.__screen = self.__game.get_screen()
        self.__bias_x = 0
        self.__bias_y = 0

    def get_grass_texture(self):
        return self.__grass_texture

    def fill_screen_with_grass(self):
        grass_filled_y = -self.__grass_size[1]
        map_end_y = self.__game.get_screen().get_size()[1] + self.__grass_size[1]
        map_end_x = self.__game.get_screen().get_size()[0] + self.__grass_size[0]
        while grass_filled_y < map_end_y:
            self.__fill_row(grass_filled_y, map_end_x)
            grass_filled_y += self.__grass_size[1]

    def __fill_row(self, grass_filled_y, map_end_x):
        grass_filled_x = -self.__grass_size[0]
        while grass_filled_x < map_end_x:
            self.__screen.blit(self.__grass_texture, (grass_filled_x - self.__bias_x, grass_filled_y - self.__bias_y))
            grass_filled_x += self.__grass_size[0]

    def change_bias_x(self, value):
        self.__bias_x = (self.__bias_x + value) % self.__grass_size[0]

    def change_bias_y(self, value):
        self.__bias_y = (self.__bias_y + value) % self.__grass_size[1]


