import pygame
from lib import gamestates
from lib import input

class Login(object):
    def __init__(self,game):
        self.__game = game
        self.__input_login = input.Input(100, 100, 0.8, 0.2, 'Login')
        self.__input_password = input.Input(100, 300, 0.8, 0.2, 'Password', is_password=True)
        print("Login initialized")

    def loop(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return gamestates.QUIT
        self.__input_login.draw(events)
        self.__input_password.draw(events)
        return gamestates.LOGIN
