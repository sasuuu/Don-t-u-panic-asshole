import pygame
from lib.game.heroes.main_hero import MainHero
from lib.game.heroes.hero import Hero
from lib.game.map import Map
from lib.game.object_generator import ObjectGenerator
from lib.connections.request import request_types


IDLE_SPEED = 0


class GameRunner:

    def __init__(self, game_object):
        self.__game = game_object
        self.__main_hero_pos = tuple(map(lambda x: x / 2, self.__game.get_screen().get_size()))
        self.__screen = self.__game.get_screen()
        self.__screen_size = self.__screen.get_size()
        self.__map = Map(self.__game)
        self.__udp_connector = self.__game.get_udp_connector()
        self.__objects = ObjectGenerator.generate_objects()
        self.__objects.sort(key=lambda y: y.get_y())
        self.__main_hero = None
        self.__main_hero_horizontal_speed = IDLE_SPEED
        self.__main_hero_vertical_speed = IDLE_SPEED
        self.__eq_slot_sprite = None
        self.__eq_slot_width = 64
        self.__marked_slot_sprite = None
        self.__1_key_value = 49
        self.__lower_margin = 84
        self.__shift_from_middle = 160
        self.__x_index = 0
        self.__y_index = 1
        self.__wait_for_data = True
        self.__hero_data = None
        self.__enemy = None

    def __create_hero(self, hero_data):
        if self.__main_hero is None:
            hp = hero_data['health']
            items = hero_data['items']
            nickname = hero_data['nick']
            position = hero_data['position']['py/tuple']
            self.__main_hero = MainHero(self, self.__game, position, nickname, hp, items)
            self.__game.pass_hero(self.__main_hero)
            self.__eq_slot_sprite = self.__main_hero.get_equipment().get_background()
            self.__marked_slot_sprite = self.__main_hero.get_equipment().get_marked_background()

    def loop(self):
        self.__game.create_udp_connection_thread()
        if self.__wait_for_data:
            self.__hero_data = self.__check_server_response()
            if self.__hero_data is not None and self.__hero_data[1] == request_types.UDP_LOGIN:
                self.__create_hero(self.__hero_data[0]['data'][0])
            elif self.__hero_data is not None and self.__hero_data[1] == 4:
                if self.__enemy is None:
                    self.__hero_data = self.__hero_data[0]['data'][0]
                    self.__enemy = Hero(self.__hero_data['position']['py/tuple'])
                    self.__objects.append(self.__enemy)
                else:
                    self.__hero_data = self.__hero_data[0]['data'][0]
                    self.__enemy.set_position(self.__hero_data['position']['py/tuple'])
        if self.__main_hero is not None:
            self.__handle_events()
            self.__transform()
            self.__draw()

    def __handle_events(self):
        for event in self.__game.get_events():
            self.__handle_keydown_events(event)
            self.__handle_keyup_events(event)
            self.__handle_number_key_event(event)

    def __handle_keydown_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            self.__main_hero_vertical_speed = -self.__hero_move_converter(self.__main_hero)
            self.__main_hero.set_movement_up()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            self.__main_hero_vertical_speed = self.__hero_move_converter(self.__main_hero)
            self.__main_hero.set_movement_down()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self.__main_hero_horizontal_speed = -self.__hero_move_converter(self.__main_hero)
            self.__main_hero.set_movement_left()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self.__main_hero_horizontal_speed = self.__hero_move_converter(self.__main_hero)
            self.__main_hero.set_movement_right()

    def __handle_keyup_events(self, event):
        if event.type == pygame.KEYUP and (event.key == pygame.K_w or event.key == pygame.K_s):
            self.__main_hero_vertical_speed = IDLE_SPEED
            self.__main_hero.reset_direction(event.key)
        elif event.type == pygame.KEYUP and (event.key == pygame.K_a or event.key == pygame.K_d):
            self.__main_hero_horizontal_speed = IDLE_SPEED
            self.__main_hero.reset_direction(event.key)

    def __hero_move_converter(self, hero):
        return hero.get_move_speed() * self.__game.get_delta_time()

    def __handle_number_key_event(self, event):
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_1 or event.key == pygame.K_2 or
                                             event.key == pygame.K_3 or event.key == pygame.K_4 or
                                             event.key == pygame.K_5):
            value = event.key - self.__1_key_value
            self.__main_hero.get_equipment().mark_item(value)

    def __transform(self):
        if not self.__main_hero.get_col_flag():
            self.__map.change_bias_x(self.__main_hero_horizontal_speed)
            self.__map.change_bias_y(self.__main_hero_vertical_speed)
        self.__main_hero.update_position(self.__main_hero_horizontal_speed, self.__main_hero_vertical_speed)

    def __draw(self):
        self.__map.fill_screen_with_grass()
        self.__screen.blit(self.__main_hero.get_sprite(), self.__main_hero_pos)
        for world_object in self.__objects:
            self.__screen.blit(world_object.get_sprite(),
                               (
                               world_object.get_x() - self.__main_hero.get_x() + self.__screen_size[self.__x_index] / 2,
                               world_object.get_y() - self.__main_hero.get_y()
                               + self.__screen_size[self.__y_index] / 2))
        marked_index = self.__main_hero.get_equipment().get_marked_index()
        for y in range(0, 5):
            if y == marked_index:
                self.__screen.blit(self.__marked_slot_sprite,
                                   ((self.__screen_size[self.__x_index] / 2) + y * self.__eq_slot_width
                                    - self.__shift_from_middle,
                                    self.__screen_size[self.__y_index] - self.__lower_margin))

            else:
                self.__screen.blit(self.__eq_slot_sprite,
                                   ((self.__screen_size[self.__x_index] / 2) + y * self.__eq_slot_width
                                    - self.__shift_from_middle,
                                    self.__screen_size[self.__y_index] - self.__lower_margin))
            if self.__main_hero.get_equipment().get_item_by_index(y) is not None:
                item_sprite = self.__main_hero.get_equipment()
                item_sprite = item_sprite.get_item_by_index(y)
                item_sprite = item_sprite.get_sprite()
                self.__screen.blit(item_sprite,
                                   ((self.__screen_size[self.__x_index] / 2) + y * self.__eq_slot_width
                                    - self.__shift_from_middle,
                                    self.__screen_size[self.__y_index] - self.__lower_margin))

    def get_objects(self):
        return self.__objects

    def __check_server_response(self):
        server_responses = self.__game.get_udp_server_responses()
        for response in server_responses:
            if response['type'] == request_types.UDP_LOGIN:
                print('hero data got')
                return [response, request_types.UDP_LOGIN]
            if response['type'] == 4:
                print('enemy data got')
                return [response, 4]
            else:
                print("Character creation failure")
                return None
