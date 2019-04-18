import socket
import os
import sys
import json
from json import JSONDecodeError
from threading import Thread

from lib import errors_provider as error

from lib import request_handler as req


class Server(object):

    def __init__(self, request_handlers_chain):
        self.__IP_ADDRESS = None
        self.__PORT_NUMBER = None
        self.__MAX_HOSTS = None
        self.__socket = None
        self.__connected_clients = []
        self.__request_handlers_chain = request_handlers_chain
        self.__config_file = "config/server_config.json"
        self.__read_config()
        self.__handle_binding()
        self.__listen_for_connections()

    def get_client_list(self):
        return self.__connected_clients

    def __read_config(self):
        if os.path.isfile(self.__config_file):
            with open(self.__config_file) as json_file:
                config_file = json.load(json_file)
                self.__IP_ADDRESS = config_file['ipAddress']
                self.__PORT_NUMBER = config_file['portNumber']
                self.__MAX_HOSTS = config_file['maxHosts']
        else:
            self.__handle_config_from_console()

    def __handle_config_from_console(self):
        print("There is no config file for server! Pass me interface, port number and max hosts")
        self.__IP_ADDRESS = input('Enter host IP x.x.x.x: ')
        self.__PORT_NUMBER = int(input('Enter port number: '))
        self.__MAX_HOSTS = int(input('Enter max hosts to connect with: '))

    def __handle_binding(self):
        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.bind((self.__IP_ADDRESS, self.__PORT_NUMBER))
        except socket.error as msg:
            print(f'Failed binding specified interface {self.__IP_ADDRESS} and port {self.__PORT_NUMBER} error {msg}')
            sys.exit(error.WRONG_SOCKET)

    def __listen_for_connections(self):
        self.__socket.listen(self.__MAX_HOSTS)
        print("Server initialized")
        while True:
            connection, address = self.__socket.accept()
            client = Connection(connection, address, self.__request_handlers_chain, self)
            self.__connected_clients.append(client)
            client.start()

    def notify_end_connection(self, client):
        self.__connected_clients.remove(client)


class Connection(Thread):
    def __init__(self, connection, address, server=None):
        Thread.__init__(self)
        self.__connection = connection
        self.__address = address
        self.__request_handlers_chain = request_handlers_chain
        self.__server = server

    def run(self):
        print(f'Users that are connected {self.__connection}')
        data = True
        while data:
            data = self.__connection.recv(1024)
            print(f'Receiving data from {self.__address} = {data}')
            if data is not b'':
                respond = self.__handle_data(data)
                self.__connection.send(respond)
        self.__connection.close()
        print(f'User disconnect {self.__address}')
        self.__server.notify_end_connection(self)

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
