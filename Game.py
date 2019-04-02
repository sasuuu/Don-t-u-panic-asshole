import pygame
import sys
import pygame.freetype
from Main_menu import MainMenu

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)


class Game(object):
    def __init__(self):
        self.max_tps = 300.0
        self.tps_delta = 0.0
        # Init
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock = pygame.time.Clock()
        self.menu = MainMenu(self)
        while True:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            # Tick
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.max_tps:
                self.tick()
                self.tps_delta -= 1 / self.max_tps

            # Draw
            self.screen.fill(white)
            self.draw()
            pygame.display.flip()

    def tick(self):
        pass

    def draw(self):
        self.menu.draw()


if __name__ == "__main__":
    Game()
