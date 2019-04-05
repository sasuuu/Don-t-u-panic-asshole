import pygame
from game.lib import gamestates
from game.lib import input


class Login(object):
    def __init__(self, game):
        self.__game = game
        self.__input_login = input.Input(0.25, 0.3, 0.5, 0.1, 'Login')
        self.__input_password = input.Input(0.25, 0.5, 0.5, 0.1, 'Password', is_password=True)
        print("Login initialized")

    def loop(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.__game.set_state(gamestates.QUIT)
        self.__input_login.draw(events)
        self.__input_password.draw(events)
