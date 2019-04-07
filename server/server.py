import socket
import os
import sys
import json
import _thread as thread
from lib import errors_provider as error
from lib import request_types as request


class Server:
    def __init__(self):
        self.__IP_ADDRESS = None
        self.__PORT_NUMBER = None
        self.__MAX_HOSTS = None
        self.__MAX_PACKAGE = None
        self.__socket = None
        self.__login_request_handler = None
        self.__server_list_request_handler = None
        self.__connected_users = []
        self.__config_file = 'config/server_config.json'
        self.__read_config()
        self.__requests_dictionary = self.__get_request_dictionary()
        self.__bind_socket()
        self.__listen_for_connections()

    def __get_request_dictionary(self):
        return {
                request.LOGIN: (lambda x: self.__login_request_handler.handle(x)),
                request.GET_SERVERS: (lambda x: self.__server_list_request_handler.handle(x)),
                request.NOT_FOUND: (lambda x: print('Request not found'))
        }

    def __read_config(self):
        if os.path.isfile(self.__config_file):
            with open(self.__config_file) as json_file:
                config_file = json.load(json_file)
                self.__IP_ADDRESS = config_file['ipAddress']
                self.__PORT_NUMBER = config_file['portNumber']
                self.__MAX_HOSTS = config_file['maxHosts']
                self.__MAX_PACKAGE = config_file['maxPackage']
        else:
            self.__handle_config_from_console()

    def __handle_config_from_console(self):
        print('There is no config file for server! Pass me interface, port number and max hosts')
        self.__IP_ADDRESS = input('Enter host IP x.x.x.x: ')
        self.__PORT_NUMBER = int(input('Enter port number: '))
        self.__MAX_HOSTS = int(input('Enter max hosts to connect with: '))

    def __bind_socket(self):
        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.bind((self.__IP_ADDRESS, self.__PORT_NUMBER))
        except socket.error as msg:
            print(f'Failed binding specified interface {self.__IP_ADDRESS} and port {self.__PORT_NUMBER} error {msg}')
            sys.exit(error.WRONG_SOCKET)

    def __listen_for_connections(self):
        self.__socket.listen(self.__MAX_HOSTS)
        print('Server initialized')
        while True:
            connection, address = self.__socket.accept()
            thread.start_new_thread(self.__handle_connection, (connection, address))

    def __handle_connection(self, connection, address):
        self.__connected_users.append([connection, address])
        data = True
        while data:
            data = connection.recv(self.__MAX_PACKAGE)
            request_type = self.__get_request_type(data)
            self.__requests_dictionary[request_type].__call__(data)
        self.__connected_users.remove([connection, address])
        connection.close()

    @staticmethod
    def __get_request_type(data):
        try:
            mapped_to_json = json.loads(data.decode('utf-8'))
            return mapped_to_json['requestType']
        except ValueError as e:
            print(f'Exception in parsing json file {e}')
        return request.NOT_FOUND


if __name__ == '__main__':
    __server = Server()
