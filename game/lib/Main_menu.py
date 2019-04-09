import pygame
import pygame.freetype
import json
import os
from game.lib import colors
from game.lib import gamestates
from game.lib import button

game_config = None
file_exists = os.path.isfile("lib/config/game_config.json")
if file_exists:
    with open("lib/config/game_config.json") as json_file:
        game_config = json.load(json_file)

FONT_STYLE = game_config['font'] if game_config is not None else "Segoe UI"
FONT_SIZE_TITLE = game_config['menu_title_font_size'] if game_config is not None else 70
FONT_SIZE_MENU = game_config['menu_font_size'] if game_config is not None else 50


class MainMenu(object):
    def __init__(self, game):

        pygame.init()
        self.__game = game
        self.__screen_size = self.__game.get_screen().get_size()
        self.__text_menu_height = FONT_SIZE_MENU
        self.__text_title_height = FONT_SIZE_TITLE
        self.__text_menu_font = pygame.freetype.SysFont(FONT_STYLE, self.__text_menu_height)
        self.__font_game_title = pygame.freetype.SysFont(FONT_STYLE, self.__text_title_height)
        self.__empty_rect = 2
        self.title_pos_y = self.__screen_size[1] / 9
        self.title_pos_x = self.__screen_size[0] / 16
        self.new_line_title = self.__text_title_height + self.__text_title_height / 3
        self.new_line = self.__text_menu_height + self.__text_menu_height / 2
        self.button_pos_x = self.__screen_size[0] / 16
        self.button_pos_y = self.__screen_size[1] / 9 + self.title_pos_y + self.new_line_title
        self.__button_start = button.Button(self.button_pos_x, self.button_pos_y, 0.2, 0.1, text='Start',
                                            function=self.choice, arguments="Start")
        self.__button_setting = button.Button(self.button_pos_x, self.button_pos_y + self.new_line,0.2, 0.1,
                                              text='Setting', function=self.choice, arguments="Setting")
        self.__button_creators = button.Button(self.button_pos_x, self.button_pos_y + 2*self.new_line,0.2, 0.1,
                                               text='Creators', function=self.choice, arguments="Creators")
        self.__button_exit = button.Button(self.button_pos_x, self.button_pos_y + 3 * self.new_line,0.2, 0.1,
                                           text='Exit', function=self.choice, arguments="Exit")
        print("Menu initialized")

    def choice(self, text):
        if text == 'Start':
            self.__game.set_state(gamestates.SERVER_LIST)
        elif text == 'Setting':
            self.__game.set_state(gamestates.SETTINGS)
        elif text == 'Creators':
            self.__game.set_state(gamestates.CREATORS)
        elif text == 'Exit':
            self.__game.set_state(gamestates.QUIT)

    def loop(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.__game.set_state(gamestates.QUIT)

        self.__font_game_title.render_to(self.__game.get_screen(), (self.title_pos_x, self.title_pos_y), "Dont U",
                                         colors.BLACK)
        self.__font_game_title.render_to(self.__game.get_screen(), (self.title_pos_x,
                                                                    self.title_pos_y + self.new_line_title),
                                         "Panic Asshole", colors.BLACK)
        self.__button_start.draw(events)
        self.__button_setting.draw(events)
        self.__button_creators.draw(events)
        self.__button_exit.draw(events)
        # rect for img only for test
        rect_pos_x = self.__screen_size[0] - self.__screen_size[0] / 3
        rect_pos_y = self.__screen_size[1] - self.__screen_size[1] / 4 * 3
        rect_width = self.__screen_size[0] / 4
        rect_height = self.__screen_size[0] / 3
        rectangle = (rect_pos_x, rect_pos_y, rect_width, rect_height)
        pygame.draw.rect(self.__game.get_screen(), colors.BLACK, rectangle, self.__empty_rect)
