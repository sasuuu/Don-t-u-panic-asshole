from lib.game.items.item import Item
import pygame


class FishingRod(Item):

    def __init__(self):
        self._id = 3
        self._name = 'fishing_rod'
        self._sprite = pygame.transform.scale(pygame.image.load('config/assets/items/fishing_rod.png'), (64, 64))


