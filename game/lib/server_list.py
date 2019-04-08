import pygame as py
import gamestates
import scroll
from connections import connector


class ServerList(object):
    def __init__(self, game):
        self.__menu_title = "Servers"
        self.__connector = connector
        self.__game = game
        self.__server_list = None
        self.__active_server = 0
        self.__scroll = scroll.Scroll(0.25, 0.2, 0.5, 0.6)

    def loop(self):
        # if self.__server_list is None:
        #      self.__server_list = self.__connector.get_servers()
        #      self.__scroll=
        events = py.event.get()
        for event in events:
            if event.type == py.QUIT:
                print('quit')
                self.__game.set_state(gamestates.QUIT)
                return
            # elif event.type == py.KEYUP or event.type == py.KEYDOWN:
            #     self.__active_server=self.__scroll.get_index()
            elif event.type == py.K_ESCAPE:
                return gamestates.MAIN_MENU
            elif event.type == py.K_RETURN:
                pass
                # return gamestates.SERVER_LIST

        self.__generate_view(events)

    def __handle_active_server_up(self):
        if self.__active_server > 0:
            self.__active_server -= 1
        else:
            self.__active_server = len(self.__server_list)

    def __handle_active_server_down(self):
        if self.__active_server < len(self.__server_list):
            self.__active_server += 1
        else:
            self.__active_server = 0

    def __generate_view(self, events):
        display_surface = py.display.get_surface()
        self.__scroll.draw(events)
      #  for server in self.__server_list:


