from lib.game.items.item import Item
import pygame


class Hook(Item):

    def __init__(self):
        self._id = 2
        self._name = 'hook'
        self._sprite = pygame.transform.scale(pygame.image.load('config/assets/items/hook.png'), (64, 64))


