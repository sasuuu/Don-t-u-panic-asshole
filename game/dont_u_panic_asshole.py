import pygame
import json
import os

from lib import gamestates
from lib import intro
from lib import login
from lib import colors
from lib import main_menu
from lib import server_list
from lib.connections import connector


class Game:
    def __init__(self):
        self.__game_title = 'Dont\'t u panic asshole'
        self.__settings = None
        self.__settings_file = "./settings.json"
        self.__state = None
        self.__clock = None
        self.__screen = None
        self.__events = None

    def get_screen(self):
        return self.__screen

    def get_events(self):
        return self.__events

    def update_events(self):
        self.__events = pygame.event.get()

    def get_settings(self):
        file_exists = os.path.isfile(self.__settings_file)
        if not file_exists:
            self.crash("Settings file does not exists")
        with open(self.__settings_file) as json_file:
            data = json.load(json_file)
        self.__settings = data
        return data

    def init(self):
        if self.__settings is None:
            self.get_settings()
        width = self.__settings['width']
        height = self.__settings['height']
        if self.__settings['fullscreen']:
            display_mode = pygame.FULLSCREEN
        else:
            display_mode = 0
        self.__clock = pygame.time.Clock()
        pygame.init()
        self.__screen = pygame.display.set_mode((width, height), display_mode)
        pygame.display.set_caption(self.__game_title)
        if self.__settings['intro_enable']:
            self.__state = gamestates.INTRO
        else:
            self.__state = gamestates.LOGIN
        print("Game initialized")

    def get_state(self):
        return self.__state

    def handle_quit_event(self):
        for event in self.__events:
            if event.type == pygame.QUIT:
                self.set_state(gamestates.QUIT)

    def set_state(self, state):
        self.__state = state

    def tick(self):
        pygame.display.update()
        self.__clock.tick(self.__settings['fps_max'])
        self.__screen.fill(colors.WHITE)

    @staticmethod
    def crash(msg):
        print(msg)
        pygame.quit()
        exit(-1)

    @staticmethod
    def quit():
        print("Bye bye :(")
        pygame.quit()
        exit(0)


if __name__ == "__main__":
    main = Game()
    main.init()
    conn = connector.Connector()
    intro_obj = intro.Intro(main)
    login_obj = login.Login(main)
    main_menu_obj = main_menu.MainMenu(main)
    server_list_obj = server_list.ServerList(main, conn)
    settings_obj = None
    settings_video_obj = None
    settings_controls_obj = None
    settings_audio_obj = None
    creators_obj = None
    game_obj = None
    while True:
        main.update_events()
        main.handle_quit_event()
        if main.get_state() == gamestates.QUIT:
            main.quit()
        elif main.get_state() == gamestates.INTRO:
            intro_obj.loop()
        elif main.get_state() == gamestates.LOGIN:
            login_obj.loop()
        elif main.get_state() == gamestates.MAIN_MENU:
            main_menu_obj.loop()
        elif main.get_state() == gamestates.SERVER_LIST:
            server_list_obj.loop()
        elif main.get_state() == gamestates.SETTINGS:
            pass
        elif main.get_state() == gamestates.SETTINGS_VIDEO:
            pass
        elif main.get_state() == gamestates.SETTINGS_CONTROLS:
            pass
        elif main.get_state() == gamestates.SETTINGS_AUDIO:
            pass
        elif main.get_state() == gamestates.CREATORS:
            pass
        elif main.get_state() == gamestates.GAME:
            pass
        else:
            main.crash("Unknown game state")
        main.tick()
