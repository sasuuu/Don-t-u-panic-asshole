import pygame
from pygame.locals import *
from colors import Color
font_size = 20
padding = 10

class CreatorsMenu(object):

    def __init__(self, main, screen):
        self.main_menu = main
        self.screen = screen
        self.__color = Color
        self.screen.fill(self.__color.black)
        self.buffer = []
        self.read_text()
        self.text = []
        self.__start_y = 720
        self.__start_x = 50

    def show_creators(self):
        pygame.display.set_caption('Creators of game')
        font = pygame.font.Font('freesansbold.ttf', font_size)
        for element in self.buffer:
            self.text.append(font.render(element, True, self.__color.green, self.__color.black))

        while True:
            for index in range(self.__start_y + len(self.buffer) * (font_size + padding)):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            return

                self.write_text(index * -1 + self.__start_y)
                pygame.time.delay(20)
                self.screen.fill(self.__color.black)
            return

    def read_text(self):
        with open(r"final_credits.txt", encoding="utf8") as file:
            for line in file:
                self.buffer.append(line.strip())
        file.close()

    def write_text(self, y):
        for element in self.text:
            self.screen.blit(element, (self.__start_x, y))
            y += font_size + padding

        pygame.display.flip()
