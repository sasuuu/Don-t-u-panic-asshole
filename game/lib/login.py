import pygame
from game.lib import gamestates
from game.lib import input
from game.lib import button
from game.lib import colors

FONT_STYLE = "Segoe UI"
TEXT_SIZE = 50


class Login(object):
    def __init__(self, game):
        self.__game = game
        self.__title = pygame.font.SysFont(FONT_STYLE, TEXT_SIZE)
        self.__input_login = input.Input(0.25, 0.3, 0.5, 0.1, 'Username')
        self.__input_password = input.Input(0.25, 0.5, 0.5, 0.1, 'Password', is_password=True)
        self.__login_button = button.Button(0.25, 0.65, 0.5, 0.1, text='LOGIN', function=self.login)
        print("Login initialized")

    def login(self):
        login = self.__input_login.get_value()
        password = self.__input_password.get_value()
        # Test login without connection to server
        print("Try to login with username="+login+" and password="+password)
        if login == 'test' and password == 'test':
            print("Login success")
            self.__game.set_state(gamestates.MAIN_MENU)
        else:
            print("Login failure")

    def loop(self):
        events = pygame.event.get()
        display_surface = pygame.display.get_surface()
        for event in events:
            if event.type == pygame.QUIT:
                self.__game.set_state(gamestates.QUIT)
        title = self.__title.render("Don\'t u panic a**hole", True, colors.BLACK)
        title_rect = title.get_rect()
        title_rect.center = (display_surface.get_width() / 2, display_surface.get_height() * 0.1)
        display_surface.blit(title, title_rect)
        self.__input_login.draw(events)
        self.__input_password.draw(events)
        self.__login_button.draw(events)
