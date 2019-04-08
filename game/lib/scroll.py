import pygame
from game.lib import colors

DEFAULT_WIDTH = 100
DEFAULT_HEIGHT = 200
DEFAULT_POS_X = 0
DEFAULT_POS_Y = 0
DEFAULT_TEXT_SIZE = 25
FONT_STYLE = "Segoe UI"
DEFAULT_TEXT_COLOR = colors.BLACK
DEFAULT_MARKED_COLOR = colors.YELLOW
DEFAULT_BACKGROUND_COLOR = colors.GRAY
DEFAULT_CONTENT = ['This is default content. ', 'If you are seeing this, ', 'it means ', 'something went wrong ',
                   'and server list,', "couldn't be downloaded."]


class Scroll(object):
    def __init__(self, pos_x=DEFAULT_POS_X, pos_y=DEFAULT_POS_Y, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT,
                 content=DEFAULT_CONTENT, text_size=DEFAULT_TEXT_SIZE, text_color=DEFAULT_TEXT_COLOR,
                 marked_text_color=DEFAULT_MARKED_COLOR, background_color=DEFAULT_BACKGROUND_COLOR):
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
        self.__text_size = text_size
        self.__text_color = text_color
        self.__marked_line_color = marked_text_color
        self.__background_color = background_color
        self.__content = content
        self.__text_size = text_size
        self.__marked_line_index = 0   # index to currently marked line
        self.__font_text = pygame.font.SysFont(FONT_STYLE, self.__text_size)
        self.__top_margin = 10
        self.__amount_to_print = int((self.__height-self.__top_margin)/self.__text_size)

    def check(self, scroll_surface, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if self.__marked_line_index != 0:
                    self.__marked_line_index = self.__marked_line_index - 1
                    self.fill_surface(scroll_surface)
                    pygame.display.flip()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if self.__marked_line_index != (len(self.__content)-1):
                    self.__marked_line_index = self.__marked_line_index + 1
                    self.fill_surface(scroll_surface)
                    pygame.display.flip()

    def draw(self, events):
        scroll_surface = pygame.Surface((self.__width, self.__height))
        scroll_surface.fill(self.__background_color)
        scroll_rectangle = pygame.Rect(self.__pos_x, self.__pos_y, self.__width, self.__height)
        display_surface = pygame.display.get_surface()
        self.check(scroll_surface, events)
        self.fill_surface(scroll_surface)
        display_surface.blit(scroll_surface, scroll_rectangle)

    def fill_surface(self, scroll_surface):
        temp = int(self.__marked_line_index/self.__amount_to_print)  # which elements should be printed
        last_to_print = temp*self.__amount_to_print+self.__amount_to_print \
            if temp*self.__amount_to_print+self.__amount_to_print <= len(self.__content)\
            else len(self.__content)  # last element to print
        list_to_print = [self.__content[i] for i in range(temp*self.__amount_to_print, last_to_print)]  # elements to print
        top_margin = self.__top_margin
        left_margin = 5
        antialias = True
        for index, server in enumerate(list_to_print, temp*self.__amount_to_print):
            if index == self.__marked_line_index:
                scroll_surface.blit(self.__font_text.render(server, antialias, self.__marked_line_color),
                                    (left_margin, top_margin))
            else:
                scroll_surface.blit(self.__font_text.render(server, antialias, self.__text_color),
                                    (left_margin, top_margin))
            top_margin += self.__text_size
            if (top_margin + self.__text_size) >= scroll_surface.get_height():  # if next line wont fit into window - stop writing
                break

    @property
    def get_marked_line_index(self):
        return self.__marked_line_index
