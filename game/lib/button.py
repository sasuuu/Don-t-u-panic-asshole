import pygame
from game.lib import colors

DEFAULT_WIDTH = 100
DEFAULT_HEIGHT = 50
DEFAULT_POS_X = 0
DEFAULT_POS_Y = 0
DEFAULT_TEXT_SIZE = 34
FONT_STYLE = "Segoe UI"
DEFAULT_BUTTON_BORDER = 0
DEFAULT_BORDER_COLOR = colors.BLACK
DEFAULT_HOVER_COLOR = colors.DEFAULT_BUTTON_HOVER_COLOR
DEFAULT_NOHOVER_COLOR = colors.DEFAULT_BUTTON_NOHOVER_COLOR
DEFAULT_TEXT_COLOR = colors.BLACK


class Button(object):
    def __init__(self, pos_x=DEFAULT_POS_X, pos_y=DEFAULT_POS_Y, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, text='',
                 text_size=DEFAULT_TEXT_SIZE, text_color=DEFAULT_TEXT_COLOR,
                 button_border=DEFAULT_BUTTON_BORDER, hover_color=DEFAULT_HOVER_COLOR,
                 nohover_color=DEFAULT_NOHOVER_COLOR, border_color=DEFAULT_BORDER_COLOR, function=None):
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
                self.__height = DEFAULT_HEIGHT
        else:
            self.__height = height
        self.__function = function
        self.__text = text
        self.__text_size = text_size
        self.__text_color = text_color
        self.__hover = False
        self.__font_text = pygame.font.SysFont(FONT_STYLE, self.__text_size)
        self.__button_border = button_border
        self.__border_color = border_color
        self.__hover_color = hover_color
        self.__nohover_color = nohover_color

    def check_mouse(self, button_rect, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and button_rect.collidepoint(pygame.mouse.get_pos()):
                if self.__function is not None:
                    self.__function()
            elif button_rect.collidepoint(pygame.mouse.get_pos()):
                self.__hover = True
            else:
                self.__hover = False

    def run_function(self):
        self.__function()

    def set_text(self, text):
        self.__text = text

    def set_hover_color(self, color):
        self.__hover_color = color

    def set_nohover_color(self, color):
        self.__nohover_color = color

    def set_color(self, color):
        self.__hover_color = color
        self.__nohover_color = color

    def get_text(self):
        button_text = self.__font_text.render(self.__text, True, self.__text_color)
        button_text_rect = button_text.get_rect()
        button_text_rect.center = (self.__pos_x + self.__width / 2, self.__pos_y + self.__height / 2)
        return button_text, button_text_rect

    def draw(self, events):
        button_surface = pygame.Surface((self.__width, self.__height))
        button_rect = pygame.Rect(self.__pos_x, self.__pos_y, self.__width, self.__height)
        self.check_mouse(button_rect, events)
        if self.__hover:
            button_surface.fill(self.__hover_color[0:3])
            if len(self.__hover_color) == 4:
                button_surface.set_alpha(self.__hover_color[3])
        else:
            button_surface.fill(self.__nohover_color[0:3])
            if len(self.__nohover_color) == 4:
                button_surface.set_alpha(self.__nohover_color[3])
        if self.__button_border > 0:
            pygame.draw.rect(button_surface, self.__border_color, (0, 0, button_surface.get_width(),
                             button_surface.get_height()), self.__button_border)
        display_surface = pygame.display.get_surface()
        button_text, button_text_rect = self.get_text()
        display_surface.blit(button_surface,button_rect)
        display_surface.blit(button_text, button_text_rect)
