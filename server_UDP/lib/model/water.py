from game_object import GameObject


class Water(GameObject):

    def __init__(self, position, object_type):
        super(Water, self).__init__(position, object_type)
