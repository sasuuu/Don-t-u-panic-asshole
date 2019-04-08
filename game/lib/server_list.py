import pygame as py
import gamestates


class ServerList:

    def __init__(self, game, connector):
        self.__menu_title = "Servers"
        self.__connector = connector
        self.__game = game
        self.__server_list = None
        self.__active_server = 0

    def loop(self):
        if self.__server_list is None:
            self.__server_list = self.__connector.get_servers()

        for event in py.event.get():
            if event.type == py.QUIT:
                return gamestates.QUIT
            elif event.type ==  py.KEYUP:
                self.__handle_active_server_up()
            elif event.type == py.KEYDOWN:
                self.__handle_active_server_down()
            elif event.type == py.K_ESCAPE:
                return gamestates.MAIN_MENU
            elif event.type == py.K_RETURN:
                pass
            else:
                self.__generate_view()
                return gamestates.SERVER_LIST

    def __handle_active_server_up(self):
        if self.__active_server > 0 :
            self.__active_server -= 1
        else:
            self.__active_server = len(self.__server_list)

    def __handle_active_server_down(self):
        if self.__active_server < len(self.__server_list):
            self.__active_server += 1
        else:
            self.__active_server = 0

    def __generate_view(self):
        pass
      #  for server in self.__server_list:


