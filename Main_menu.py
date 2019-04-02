import pygame
import sys
import pygame.freetype

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)


class MainMenu(object):
    def __init__(self, game):
        self.game = game
        self.size = self.game.screen.get_size()
        self.menu = pygame.freetype.SysFont('Arial', 50)
        self.title = pygame.freetype.SysFont('Arial', 70)

    def tick(self):
        # input
        pass

    def draw(self):

        # Title

        self.title.render_to(self.game.screen, (100, self.size[1] / 8), "Dont U", black)
        self.title.render_to(self.game.screen, (100, self.size[1] / 8+90), "Panic Asshole", black)

        # menu buttons
        self.button(100, self.size[1] / 4 + 100, "Start", 100)
        self.button(100, self.size[1] / 4 + 150, "Ustawienia", 200)
        self.button(100, self.size[1] / 4 + 200, "Tworcy", 150)
        self.button(100, self.size[1] / 4 + 250, "Wyjdź", 120)

        # rect for img
        pygame.draw.rect(self.game.screen, black, (self.size[0] - self.size[0]/3, self.size[1] - self.size[1]/4*3, 300, 400), 2)

    def button(self, pos_x, pos_y, txt, size):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if pos_x+size > mouse[0] > pos_x and pos_y + 40 > mouse[1] > pos_y:
            self.menu.render_to(self.game.screen, (pos_x, pos_y), txt, green)
            pygame.draw.rect(self.game.screen, green, (pos_x, pos_y, size, 40), 2)
            if click[0]:
                if txt == "Start":
                    pass
                elif txt == "Ustawienia":
                    pass
                elif txt == "Tworcy":
                    pass
                elif txt == "Wyjdź":
                    pygame.quit()
                    sys.exit(0)
        else:
            self.menu.render_to(self.game.screen, (pos_x, pos_y), txt, black)
            pygame.draw.rect(self.game.screen, black, (pos_x, pos_y, size, 40), 2)
