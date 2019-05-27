from abc import ABC, abstractmethod


class GameObject(ABC):

    @abstractmethod
    def __init__(self, position, object_type):
        self.position = position
        self.object_type = object_type
