import pygame
from game.lib import colors

DEFAULT_WIDTH = 100
DEFAULT_HEIGHT = 50
DEFAULT_POS_X = 0
DEFAULT_POS_Y = 0
DEFAULT_TEXT_SIZE = 34
FONT_STYLE = "Segoe UI"
BUTTON_BORDER = 1
BUTTON_HOVER_ALPHA = 80
BUTTON_NOHOVER_ALPHA = 20
DEFAULT_TEXT_COLOR = colors.BLACK
DEFAULT_BUTTON_COLOR = colors.GREEN


class Button(object):
    def __init__(self, pos_x=DEFAULT_POS_X, pos_y=DEFAULT_POS_Y, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, text='',
                 text_size=DEFAULT_TEXT_SIZE, text_color=DEFAULT_TEXT_COLOR, button_color=DEFAULT_BUTTON_COLOR,
                 function=None):
        if pos_x < 1:
            suf = pygame.display.get_surface()
            if suf is not None:
                self.__pos_x = pos_x * suf.get_width()
            else:
                self.__pos_x = DEFAULT_POS_X
        else:
            self.__pos_x = pos_x
        if pos_y < 1:
            suf = pygame.display.get_surface()
            if suf is not None:
                self.__pos_y = pos_y * suf.get_height()
            else:
                self.__pos_y = DEFAULT_POS_Y
        else:
            self.__pos_y = pos_y
        if width < 1:
            suf = pygame.display.get_surface()
            if suf is not None:
                self.__width = width * suf.get_width()
            else:
                self.__width = DEFAULT_WIDTH
        else:
            self.__width = width
        if height < 1:
            suf = pygame.display.get_surface()
            if suf is not None:
                self.__height = height * suf.get_height()
            else:
                self.__width = DEFAULT_HEIGHT
        else:
            self.__height = height
        self.__button_color = button_color
        self.__function = function
        self.__text = text
        self.__text_size = text_size
        self.__text_color = text_color
        self.__hover = False
        self.__font_text = pygame.font.SysFont(FONT_STYLE, self.__text_size)

    def check_mouse(self, button_rect, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] \
                    and button_rect.collidepoint(pygame.mouse.get_pos()):
                if self.__function is not None:
                    self.__function()
            elif button_rect.collidepoint(pygame.mouse.get_pos()):
                self.__hover = True
            else:
                self.__hover = False

    def run_function(self):
        self.__function()

    def get_text(self):
        button_text = self.__font_text.render(self.__text, True, self.__text_color)
        button_text_rect = button_text.get_rect()
        button_text_rect.center = (self.__pos_x + self.__width / 2, self.__pos_y + self.__height / 2)
        return button_text, button_text_rect

    def draw(self, events):
        button_surface = pygame.Surface((self.__width, self.__height))
        button_surface.fill(self.__button_color)
        button_rect = pygame.Rect(self.__pos_x, self.__pos_y, self.__width, self.__height)
        self.check_mouse(button_rect, events)
        if self.__hover:
            button_surface.set_alpha(BUTTON_HOVER_ALPHA)
        else:
            button_surface.set_alpha(BUTTON_NOHOVER_ALPHA)
        display_surface = pygame.display.get_surface()
        button_text, button_text_rect = self.get_text()
        display_surface.blit(button_surface, button_rect)
        display_surface.blit(button_text, button_text_rect)
