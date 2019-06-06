from lib.game.items.item import Item
import pygame


class Equipment:

    __item_list = [None, None, None, None, None]
    __background = pygame.transform.scale(pygame.image.load('config/assets/item_background.png'), (64, 64))
    __marked_background = pygame.transform.scale(pygame.image.load('config/assets/marked_item_background.png'), (64, 64))
    __marked_index = 0

    def pick_up_item(self, new_item: Item):
        try:
            index = self.__item_list.index(None)
            self.__item_list.insert(index, new_item)
            print("Item placed in eq on slot number:" + str(index))
        except ValueError:
            print("Inventory is full")

    def get_background(self):
        return self.__background

    def get_marked_background(self):
        return self.__marked_background

    def get_item_by_index(self, index):
        return self.__item_list[index]

    def drop_item(self, index):
        self.__item_list.insert(index, None)

    def get_items(self):
        return self.__item_list

    def mark_item(self, index):
        self.__marked_index = index

    def get_marked_index(self):
        return self.__marked_index

