from lib import object_types


class Character:

    def __init__(self, nick, health, position, items):
        self.type = object_types.CHARACTER
        self.nick = nick
        self.health = health
        self.position = position
        self.items = items
