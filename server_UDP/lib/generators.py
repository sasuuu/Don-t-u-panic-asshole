import random

from lib.model.water import Water

MIN_WATER_PLACE = 5
MAX_WATER_PLACE = 100

class MapGenerator(object):
    @staticmethod
    def generate_objects_list():
        list = []
        for i in range(random.randrange(MIN_WATER_PLACE,MAX_WATER_PLACE)):
            list.append(Water())

        return list
