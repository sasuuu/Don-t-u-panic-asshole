import pygame
import sys
import pygame.freetype
from colors import Color


class MainMenu(object):
    def __init__(self, game):
        pygame.init()
        self.__game = game
        self.__color = Color
        self.__screen_size = self.__game.screen.get_size()
        self.__text_menu_height = 50
        self.__text_title_height = 70
        self.__text_menu_font = pygame.freetype.SysFont('Arial', self.__text_menu_height)
        self.__font_game_title = pygame.freetype.SysFont('Arial', self.__text_title_height)
        self.__empty_rect = 2

    def draw(self):

        # Title
        title_pos_x = 100
        title_pos_y = self.__screen_size[1] / 8
        new_line_title = self.__text_title_height + 20
        self.__font_game_title.render_to(self.__game.screen, (title_pos_x, title_pos_y), "Dont U", self.__color.black)
        self.__font_game_title.render_to(self.__game.screen, (title_pos_x, title_pos_y + new_line_title), "Panic Asshole", self.__color.black)

        # menu buttons
        button_pos_x = 100
        button_pos_y = self.__screen_size[1] / 4 + 100    # pos_x and pos_y mean top left corner position
        new_line_menu = self.__text_menu_height + 20
        self.__button(button_pos_x, button_pos_y, "Start", 90)
        self.__button(button_pos_x, button_pos_y + new_line_menu, "Setting", 130)
        self.__button(button_pos_x, button_pos_y + 2 * new_line_menu, "Authors", 150)
        self.__button(button_pos_x, button_pos_y + 3 * new_line_menu, "Exit", 70)

        # rect for img
        rect_pos_x = self.__screen_size[0] - self.__screen_size[0] / 3
        rect_pos_y = self.__screen_size[1] - self.__screen_size[1] / 4 * 3
        rect_width = 300
        rect_height = 400
        rectangle = (rect_pos_x, rect_pos_y, rect_width, rect_height)
        pygame.draw.rect(self.__game.screen, self.__color.black, rectangle, self.__empty_rect)

    def __button(self, pos_x, pos_y, txt, text_size):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # if mouse is on button
        if pos_x+text_size > mouse[0] > pos_x and pos_y + self.__text_menu_height > mouse[1] > pos_y:
            self.__text_menu_font.render_to(self.__game.screen, (pos_x, pos_y), txt, self.__color.green)
            pygame.draw.rect(self.__game.screen, self.__color.green, (pos_x, pos_y, text_size, self.__text_menu_height), self.__empty_rect)
            if click[0]:
                if txt == "Start":
                    pass
                elif txt == "Setting":
                    pass
                elif txt == "Authors":
                    pass
                elif txt == "Exit":
                    pygame.quit()
                    sys.exit()
        else:
            self.__text_menu_font.render_to(self.__game.screen, (pos_x, pos_y), txt, self.__color.black)
            pygame.draw.rect(self.__game.screen, self.__color.black, (pos_x, pos_y, text_size, self.__text_menu_height), self.__empty_rect)
