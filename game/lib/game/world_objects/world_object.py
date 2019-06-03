import pygame


class WorldObject:

    __real_x = None
    __real_y = None
    _x_coordinate = None
    _y_coordinate = None
    _height = None
    _width = None
    _sprite_path = None
    _move_left_corner_x = None
    _move_left_corner_y = None
    _width_collision = None
    _height_collision = None

    def get_x(self):
        return self._x_coordinate

    def get_y(self):
        return self._y_coordinate

    def get_mv_x(self):
        return self._move_left_corner_x

    def get_mv_y(self):
        return self._move_left_corner_y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_width_collision(self):
        return self._width_collision

    def get_height_collision(self):
        return self._height_collision

    def get_sprite(self):
        return self._sprite_path

    def set_x(self, value):
        self._x_coordinate = value

    def set_y(self, value):
        self._y_coordinate = value

    def change_position_on_screen(self):
        actual_time = pygame.time.get_ticks()

    def check_collision(self, screen, hero_pos_x, hero_pos_y, hero_width, hero_height, center_x, center_y):
        x_obj, y_obj = self._x_coordinate - hero_pos_x, self._y_coordinate - hero_pos_y
        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
        hero_x, hero_y = width / 2 + center_x, height / 2 + center_y
        if x_obj + self._move_left_corner_x < hero_x < (x_obj + self._move_left_corner_x + self._width_collision) or x_obj + self._move_left_corner_x < \
                (hero_x + hero_width) < (x_obj + self._width_collision + self._move_left_corner_x):
            if y_obj + self._move_left_corner_y < hero_y < y_obj + self._move_left_corner_y + self._height_collision:
                return True
            elif y_obj + self._move_left_corner_y < (hero_y + hero_height) < (y_obj + self._move_left_corner_y + self._height_collision):
                return True
            else:
                return False
        else:
            return False

    def draw_collision_rect(self, screen, hero_pos_x, hero_pos_y, hero_width, hero_height, center_x, center_y):
        x_obj, y_obj = self._x_coordinate - hero_pos_x, self._y_coordinate - hero_pos_y
        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
        hero_x, hero_y = width / 2 + center_x, height / 2 + center_y
        pygame.draw.rect(screen, (255, 0, 255), [x_obj + self._move_left_corner_x, y_obj + self._move_left_corner_y, self._width_collision, self._height_collision], 1)
        pygame.draw.rect(screen, (255, 0, 0), [hero_x, hero_y, hero_width, hero_height], 1)
