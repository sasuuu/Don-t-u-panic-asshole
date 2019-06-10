import random

from lib.object_types import *
from lib.model.game_object import GameObject

MIN_WATER_PLACE_COUNT = 5
MAX_WATER_PLACE_COUNT = 100

MIN_ITEMS_COUNT = 10
MAX_ITEMS_COUNT = 11

MAP_HEIGHT = 50000
MAP_WIDTH = 50000


class MapGenerator(object):
    @staticmethod
    def generate_objects_list():
        list = []
        for i in range(random.randrange(MIN_ITEMS_COUNT, MAX_ITEMS_COUNT)):
            list.append(GameObject(GameObject.get_next_id(),
                                   (random.randrange(-MAP_WIDTH, MAP_WIDTH), random.randrange(-MAP_HEIGHT, MAP_HEIGHT)),
                                   random.randrange(1, OBJECT_TYPES_COUNT)))

        return list
