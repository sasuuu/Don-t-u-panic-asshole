import pygame
from lib import colors
import pygame.freetype
import json
import os
from lib import gamestates
from math import floor

game_config = None
file_exists = os.path.isfile("config/game_config.json")
if file_exists:
    with open("config/game_config.json") as json_file:
        game_config = json.load(json_file)

FONT_SIZE = game_config['creators_font_size'] if game_config is not None else 20
PADDING = game_config['creators_padding'] if game_config is not None else 10
FONT_STYLE = game_config['creators_font_style'] if game_config is not None else "freesansbold.ttf"


class CreatorsMenu(object):

    def __init__(self, game):
        self.__game = game
        self.__game.get_screen().fill(colors.BLACK)
        self.__screen_size = self.__game.get_screen().get_size()
        self.__buffer = []
        self.__read_text()
        self.__text = []
        self.__start_y = self.__screen_size[1]
        self.__start_x = floor(self.__screen_size[0] / 6)
        self.__font = pygame.font.Font(FONT_STYLE, FONT_SIZE)
        self.__delay = 20
        self.__prepare_text()

    def loop(self):

        events = self.__game.get_events()
        for index in range(self.__start_y + len(self.__buffer) * (FONT_SIZE + PADDING)):
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.__game.set_state(gamestates.MAIN_MENU)
                    return

            self.__write_text(-index + self.__start_y)
            pygame.time.delay(self.__delay)
            self.__game.get_screen().fill(colors.BLACK)
        self.__game.set_state(gamestates.MAIN_MENU)
        return

    def __read_text(self):
        with open(r"lib/resources/final_credits.txt", encoding="utf8") as file:
            for line in file:
                self.__buffer.append(line.strip())
        file.close()

    def __write_text(self, y):
        for element in self.__text:
            self.__game.get_screen().blit(element, (self.__start_x, y))
            y += FONT_SIZE + PADDING

        pygame.display.flip()

    def __prepare_text(self):
        for element in self.__buffer:
            if element != '':
                if element[0] == '-':
                    self.__text.append(self.__font.render(element, True, colors.GREEN, colors.BLACK))
                else:
                    self.__text.append(self.__font.render(element, True, colors.WHITE, colors.BLACK))
            else:
                self.__text.append(self.__font.render(element, True, colors.GREEN, colors.BLACK))
