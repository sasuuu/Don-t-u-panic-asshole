import pygame

class WorldObject:

    __real_x = None
    __real_y = None
    _x_coordinate = None
    _y_coordinate = None
    _height = None
    _width = None
    _sprite_path = None
    _x_plus_width = None
    _y_plus_height = None
    _mov_x = None
    _mov_y = None

    def get_x(self):
        return self._x_coordinate

    def get_y(self):
        return self._y_coordinate

    def get_mv_x(self):
        return self._mov_x

    def get_mv_y(self):
        return self._mov_y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_sprite(self):
        return self._sprite_path

    def set_x(self, value):
        self._x_coordinate = value
        self._x_plus_width = value + self._width

    def set_y(self, value):
        self._y_coordinate = value
        self._y_plus_height = value + self._height

    def change_position_on_screen(self):
        actual_time = pygame.time.get_ticks()

    def check_collision(self, screen, x_obj, y_obj, hero_width, hero_height, center_x, center_y):
        x_obj, y_obj = self._x_coordinate - x_obj, self._y_coordinate - y_obj
        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
        hero_x, hero_y = width / 2 + center_x, height / 2 + center_y
        pygame.draw.rect(screen, (255, 0, 255),[x_obj + self._mov_x, y_obj + self._mov_y, self._width, self._height], 1)
        pygame.draw.rect(screen, (255, 0, 0), [hero_x, hero_y, hero_width, hero_height], 1)
        if x_obj + self._mov_x < hero_x < (x_obj + self._mov_x + self._width) or x_obj + self._mov_x < \
                (hero_x + hero_width) < (x_obj + self._width + self._mov_x):
            if y_obj + self._mov_y < hero_y < y_obj + self._mov_y + self._height:
                return True
            elif y_obj + self._mov_y < (hero_y + hero_height) < (y_obj + self._mov_y + self._height):
                return True
            else:
                return False
        else:
            return False

