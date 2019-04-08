import pygame
from pygame.locals import *
from colors import Color


class CreatorsMenu(object):

    def __init__(self, screen):
        self.screen = screen
        self.__color = Color
        self.screen.fill(self.__color.black)
        self.__buffer = []
        self.__read_text()
        self.__text = []
        self.__start_y = 720
        self.__start_x = 200
        self.__font_size = 20
        self.__font = pygame.font.Font('freesansbold.ttf', self.__font_size)
        self.__padding = 10
        self.__delay = 20

    def show_creators(self):
        pygame.display.set_caption('Creators of game')
        self.__prepare_text()

        while True:
            for index in range(self.__start_y + len(self.__buffer) * (self.__font_size + self.__padding)):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            return

                self.__write_text(index * -1 + self.__start_y)
                pygame.time.delay(self.__delay)
                self.screen.fill(self.__color.black)
            return

    def __read_text(self):
        with open(r"final_credits.txt", encoding="utf8") as file:
            for line in file:
                self.__buffer.append(line.strip())
        file.close()

    def __write_text(self, y):
        for element in self.__text:
            self.screen.blit(element, (self.__start_x, y))
            y += self.__font_size + self.__padding

        pygame.display.flip()

    def __prepare_text(self):
        for element in self.__buffer:
            if element != '':
                if element[0] == '-':
                    self.__text.append(self.__font.render(element, True, self.__color.green, self.__color.black))
                else:
                    self.__text.append(self.__font.render(element, True, self.__color.white, self.__color.black))
            else:
                self.__text.append(self.__font.render(element, True, self.__color.green, self.__color.black))