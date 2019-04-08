import pygame as py
from lib import gamestates

class ServerList:
    def __init__(selfs, game, connector):
        self.__menu_title = "Servers"
        self.__server_list is None
        self.__active_server = 0
        self.

    def loop(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                return gamestates.QUIT
            elif event.type ==  py.KEYUP:
                handle_active_server_up()
            elif event.type == py.KEYDOWN:
                handle_active_server_down()
            elif event.type == py.K_ESCAPE:
                return gamestates.



        if self.__server_list is None:
            self.__server_list = connector.get_server_list()


    def handle_active_server_up(self):
        if self.__active_server > 0 :
            self.__active_server -= 1
        else:
            self.__active_server = len(self.__server_list)

    def handle_active_server_down(self):
        if self.__active_server < len(self.__server_list):
            self.__active_server += 1
        else:
            self.__active_server = 0

