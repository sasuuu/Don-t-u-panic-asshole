import socket
import os
import sys
import json
import pickle
import _thread as thread
from lib import errors_provider as error
from lib import request_types as request
from lib.request_entities.login_response import LoginResponse
from lib.request_entities.server_list_response import ServerList


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
                request.LOGIN: (lambda data, connection: self.__return_login(data, connection)),
                request.GET_SERVERS: (lambda data, connection: self.__return_servers(data, connection)),
                request.NOT_FOUND: (lambda data, connection: print('Request not found'))
        }

    # Method for testing purpose, will be deleted after adding proper request handlers
    def __return_login(self, data, connection):
        print(f'Received {data}')
        server_authorization = LoginResponse('True')
        connection.send(self.__serialize_object(server_authorization))

    def __return_servers(self, data, connection):
        print(f'Received {data}')
        names = ["Server Krzemień", "Server Kulig", "Server Merta", "Server Kwilosz", "Server Krzystanek",
                       "Server Łyś", "Server Król"]
        server_list = ServerList(names)
        connection.send(self.__serialize_object(server_list))

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
            try:
                data = connection.recv(self.__MAX_PACKAGE)
                deserialized_data = pickle.loads(data)
                request_type = self.__get_request_type(deserialized_data)
                self.__requests_dictionary[request_type].__call__(deserialized_data, connection)
            except Exception as e:
                print(f'Error deserializing data {e}')
        self.__connected_users.remove([connection, address])
        connection.close()

    @staticmethod
    def __get_request_type(data):
        try:
            print(f'Data i Received {data}')
            mapped_to_json = json.loads(data)
            return mapped_to_json['requestType']
        except ValueError as e:
            print(f'Exception in parsing json file {e}')
        return request.NOT_FOUND

    @staticmethod
    def __serialize_object(sending_object):
        return pickle.dumps(json.dumps(vars(sending_object)))

    @staticmethod
    def __deserialize_object(sending_object):
        return json.loads(pickle.loads(sending_object))


if __name__ == '__main__':
    __server = Server()
