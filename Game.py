import pygame
import sys
import pygame.freetype
from Main_menu import MainMenu
from colors import Color


class Game(object):
    def __init__(self):
        self.__color = Color
        self.__tps = 300.0  # Tick per second
        self.__tps_delta = 0.0
        screen_width = 1280
        screen_height = 720
        # Init
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.tps_clock = pygame.time.Clock()
        self.menu = MainMenu(self)
        while True:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
            # Tick
            self.__tps_delta += self.tps_clock.tick() / 1000.0
            while self.__tps_delta > 1 / self.__tps:
                self.tick()
                self.__tps_delta -= 1 / self.__tps

            # Draw
            self.screen.fill(self.__color.white)
            self.draw()
            pygame.display.flip()

    def tick(self):
        pass

    def draw(self):
        self.menu.draw()


if __name__ == "__main__":
    Game()
