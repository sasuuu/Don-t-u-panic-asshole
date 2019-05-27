import pygame

class WorldObject:

    __real_x = None
    __real_y = None
    _x_coordinate = None
    _y_coordinate = None
    _heigth = None
    _width = None
    _sprite_path = None

    def get_x(self):
        return self._x_coordinate

    def get_y(self):
        return self._y_coordinate

    def get_sprite(self):
        return self._sprite_path

    def set_x(self, value):
        self._x_coordinate = value

    def set_y(self, value):
        self._y_coordinate = value

    def change_position_on_screen(self):
        actual_time = pygame.time.get_ticks()

