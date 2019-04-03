import pygame
from lib import gamestates

class Login(object):
    def __init__(self,game):
        self.game = game
        print("Login initialized")

    def loop(self):
        return gamestates.QUIT
