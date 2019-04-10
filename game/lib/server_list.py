import pygame as py
import gamestates
import interactive_menu
import colors
from connections import connector


class ServerList(object):
    def __init__(self, game):
        self.__menu_title = "Servers"
        self.__connector = connector
        self.__game = game
        self.__server_list = None
        self.__active_server = 0
        self.__title = py.font.SysFont("Segoe UI", 50)
        self.__interactive_menu = interactive_menu.InteractiveMenu(0.25, 0.2, 0.5, 0.6)

    def loop(self):
        # if self.__server_list is None:
        #      self.__server_list = self.__connector.get_servers()
        #      self.__scroll= interactive_menu.InteractiveMenu(0.25, 0.2, 0.5, 0.6,self.__server_list)
        events = py.event.get()
        for event in events:
            if event.type == py.QUIT:
                print('quit')
                self.__game.set_state(gamestates.QUIT)
                return
            elif event.type == py.K_ESCAPE:
                return gamestates.MAIN_MENU
            elif event.type == py.K_RETURN:
                pass
                # return gamestates.SERVER_LIST
            elif event.type == py.KEYDOWN and event.key == py.K_RETURN:
                if self.__server_list is not None:
                    self.__active_server = self.__interactive_menu.get_marked_line_index
                    self.__game.set_state(gamestates.GAME)
                    print(self.__active_server)

        self.__generate_view(events)

    def __generate_view(self, events):
        display_surface = py.display.get_surface()
        title = self.__title.render("Select game server", True, colors.BLACK)
        title_rect = title.get_rect()
        title_rect.center = (display_surface.get_width() / 2, display_surface.get_height() * 0.1)
        display_surface.blit(title, title_rect)
        self.__interactive_menu.draw(events)
