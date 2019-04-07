import pygame
from game.lib import colors

DEFAULT_WIDTH = 100
DEFAULT_HEIGHT = 50
DEFAULT_POS_X = 0
DEFAULT_POS_Y = 0
DEFAULT_TEXT_SIZE = 34
DEFAULT_LABEL_SIZE = 34
FONT_STYLE = "Segoe UI"
DEFAULT_INPUT_BORDER = 1
INPUT_FOCUS_ALPHA = 80
INPUT_NOFOCUS_ALPHA = 20
DEFAULT_LABEL_COLOR = colors.BLACK
DEFAULT_TEXT_COLOR = colors.BLACK
DEFAULT_BORDER_COLOR = colors.BLACK
KEYS = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'z', 'x', 'c', 'v', 'b', 'n', 'm',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


class Input(object):
    def __init__(self, pos_x=DEFAULT_POS_X, pos_y=DEFAULT_POS_Y, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, label='',
                 label_size=DEFAULT_LABEL_SIZE, text_size=DEFAULT_TEXT_SIZE, label_color=DEFAULT_LABEL_COLOR,
                 text_color=DEFAULT_TEXT_COLOR, input_border=DEFAULT_INPUT_BORDER, border_colo=DEFAULT_BORDER_COLOR,
                 is_password=False):
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
        self.__is_password = is_password
        self.__label = label
        self.__value = ''
        self.__text_size = text_size
        self.__label_text_size = label_size
        self.__font_label = pygame.font.SysFont(FONT_STYLE, self.__label_text_size)
        self.__label_color = label_color
        self.__text_color = text_color
        self.__active = False
        self.__font_text = pygame.font.SysFont(FONT_STYLE, self.__text_size)
        self.__text_start = 0
        self.__input_border = input_border
        self.__border_color = DEFAULT_BORDER_COLOR

    def check_mouse(self, input_rect):
        if pygame.mouse.get_pressed()[0] and input_rect.collidepoint(pygame.mouse.get_pos()):
            self.__active = True
        elif pygame.mouse.get_pressed()[0] and not input_rect.collidepoint(pygame.mouse.get_pos()):
            self.__active = False

    def check_user_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and len(self.__value) > 0:
                    self.__value = self.__value[:-1]
                    if self.__text_start > 0:
                        self.__text_start = self.__text_start - 1
                elif event.unicode.lower() in KEYS:
                    self.__value = self.__value + event.unicode

    def get_value(self):
        return self.__value

    def get_text(self):
        if self.__is_password:
            str = ''
            for i in range(self.__text_start, len(self.__value)):
                str = str + '*'
            input_text = self.__font_text.render(str, True, self.__text_color)
        else:
            input_text = self.__font_text.render(self.__value[self.__text_start:], True, self.__text_color)
        input_text_rect = input_text.get_rect()
        input_text_rect.center = (self.__pos_x + self.__width / 2, self.__pos_y + self.__height / 2)
        return input_text, input_text_rect

    def get_label(self):
        input_label = self.__font_label.render(self.__label, True, self.__label_color)
        input_label_rect = input_label.get_rect()
        input_label_rect.center = (self.__pos_x + self.__width / 2, self.__pos_y - input_label_rect.height / 2)
        return input_label, input_label_rect

    def draw(self, events):
        input_surface = pygame.Surface((self.__width, self.__height))
        input_surface.fill(colors.GREEN)
        if self.__input_border > 0:
            pygame.draw.rect(input_surface, self.__border_color, (0, 0, input_surface.get_width(),
                             input_surface.get_height()), self.__input_border)
        input_rect = pygame.Rect(self.__pos_x, self.__pos_y, self.__width, self.__height)
        self.check_mouse(input_rect)
        if self.__active:
            input_surface.set_alpha(INPUT_FOCUS_ALPHA)
            self.check_user_input(events)
        else:
            input_surface.set_alpha(INPUT_NOFOCUS_ALPHA)
        display_surface = pygame.display.get_surface()
        input_text, input_text_rect = self.get_text()
        if input_text_rect.width > input_rect.width:
            self.__text_start = self.__text_start + 1
        display_surface.blit(input_surface, input_rect)
        display_surface.blit(input_text, input_text_rect)
        if self.__label is not None:
            input_label, input_label_rect = self.get_label()
            display_surface.blit(input_label, input_label_rect)
