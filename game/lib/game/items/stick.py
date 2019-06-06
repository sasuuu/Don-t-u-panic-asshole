from lib.game.items.item import Item
import pygame


class Stick(Item):

    def __init__(self):
        self._id = 1
        self._name = 'Stick'
        self._sprite = pygame.transform.scale(pygame.image.load('config/assets/items/stick.png'), (64, 64))


