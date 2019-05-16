import pygame
import pygame.freetype
from .colors import *
import json
import os
from lib import gamestates

game_config = None
file_exists = os.path.isfile("config/game_config.json")
if file_exists:
    with open("config/game_config.json") as json_file:
        game_config = json.load(json_file)

CONTROLS_FONT = game_config['font'] if game_config is not None else "Arial"
CONTROLS_FONT_SIZE = game_config['controls_font_size'] if game_config is not None else 50
CONTROLS_TITLE_SIZE = game_config['controls_title_size'] if game_config is not None else 70

class Controls:
    def __init__(self, game):
        self.__game = game
        self.__size = self.__game.get_screen().get_size()
        self.__menu = pygame.freetype.SysFont(CONTROLS_FONT, CONTROLS_FONT_SIZE)
        self.__title = pygame.freetype.SysFont(CONTROLS_FONT, CONTROLS_TITLE_SIZE)
        self.__text = pygame.freetype.SysFont(CONTROLS_FONT, CONTROLS_FONT_SIZE)

    def loop(self):

        self.__game.get_screen().fill(WHITE)

        title_x = 100
        title_y = self.__size[1] / 8
        self.__title.render_to(self.__game.get_screen(), (title_x, title_y), "Controls", BLACK)

        first_row_text_y = self.__size[1] / 3 + 160
        first_row_icon_y = self.__size[1] / 3 + 80
        second_row_text_y = self.__size[1] * (3 / 4) + 80

        wsad_length_x = 230
        wsad_length_y = 150
        wsad_icon_x = self.__size[0] / 4 - 80
        wsad_icon_y = self.__size[1] / 3
        wsad_text_x = wsad_icon_x + 60

        self.__text.render_to(self.__game.get_screen(), (wsad_text_x, first_row_text_y), "Move", BLACK)
        pygame.draw.rect(self.__game.get_screen(), BLACK, (wsad_icon_x, wsad_icon_y, wsad_length_x, wsad_length_y), 2)

        key_length = 70

        equip_icon_x = self.__size[0] / 2 - 40
        equip_text_x = equip_icon_x - 60

        self.__text.render_to(self.__game.get_screen(), (equip_text_x, first_row_text_y), "Equipment", BLACK)
        pygame.draw.rect(self.__game.get_screen(), BLACK, (equip_icon_x, first_row_icon_y, key_length, key_length), 2)

        use_icon_x = self.__size[0] * (3 / 4) - 170

        self.__text.render_to(self.__game.get_screen(), (use_icon_x, first_row_text_y), "Use", BLACK)
        pygame.draw.rect(self.__game.get_screen(), BLACK, (use_icon_x, first_row_icon_y, key_length, key_length), 2)

        escape_icon_x = self.__size[0] * (3 / 4) + 30
        escape_text_x = escape_icon_x - 15

        self.__text.render_to(self.__game.get_screen(), (escape_text_x, first_row_text_y), "Menu", BLACK)
        pygame.draw.rect(self.__game.get_screen(), BLACK, (escape_icon_x, first_row_icon_y, key_length, key_length), 2)

        access_x_length = 390
        access_y_length = 70
        access_icon_x = self.__size[0] / 4 - 160
        access_icon_y = self.__size[1] * (3 / 4)
        access_text_x = access_icon_x + 70

        self.__text.render_to(self.__game.get_screen(), (access_text_x, second_row_text_y), "Quick access", BLACK)
        pygame.draw.rect(self.__game.get_screen(), BLACK, (access_icon_x, access_icon_y, access_x_length, access_y_length), 2)

        mouse_length = 140
        mouse_icon_y = self.__size[1] * (3 / 4) - 70

        attack_icon_x = self.__size[0] / 2
        attack_text_x = attack_icon_x + 15

        self.__text.render_to(self.__game.get_screen(), (attack_text_x, second_row_text_y), "Attack", BLACK)
        pygame.draw.rect(self.__game.get_screen(), BLACK, (attack_icon_x, mouse_icon_y, mouse_length, mouse_length), 2)

        move_icon_x = self.__size[0] * (3 / 4) - 80
        move_text_x = move_icon_x + 40

        self.__text.render_to(self.__game.get_screen(), (move_text_x, second_row_text_y), "Aim", BLACK)
        pygame.draw.rect(self.__game.get_screen(), BLACK, (move_icon_x, mouse_icon_y, mouse_length, mouse_length), 2)

        exit_x = self.__size[0] * (5 / 6)
        exit_y = self.__size[1] / 8 + 10
        exit_x_length = 100
        exit_y_length = 40


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if exit_x + exit_x_length > mouse[0] > exit_x and exit_y + exit_y_length > mouse[1] > exit_y:
            self.__menu.render_to(self.__game.get_screen(), (exit_x, exit_y), "Back", GREEN)
            pygame.draw.rect(self.__game.get_screen(), GREEN, (exit_x, exit_y, exit_x_length, exit_y_length), 2)
            if click[0]:
                self.__game.set_state(gamestates.MAIN_MENU)
        else:
            self.__menu.render_to(self.__game.get_screen(), (exit_x, exit_y), "Back", BLACK)
            pygame.draw.rect(self.__game.get_screen(), BLACK, (exit_x, exit_y, exit_x_length, exit_y_length), 2)

