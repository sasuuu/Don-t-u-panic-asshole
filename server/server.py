import socket
import os
import sys
import json
import pickle
from threading import Thread

from lib.request_entities import request_fabric as request_fabric
from lib import errors_provider as error
from lib import request_types as request

class Server(object):

    def __init__(self):
        self.__IP_ADDRESS = None
        self.__PORT_NUMBER = None
        self.__MAX_HOSTS = None
        self.__MAX_PACKAGE = None
        self.__socket = None
        self.__login_request_handler = None
        self.__server_list_request_handler = None
        self.__connected_clients = []
        self.__config_file = 'config/server_config.json'
        self.__read_config()
        self.__requests_dictionary = request_fabric.get_request_dictionary()
        self.__bind_socket()
        self.__listen_for_connections()

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
            client = Client(connection, address, self.__requests_dictionary, self.__MAX_PACKAGE, self)
            client.start()
            self.__connected_clients.append(client)

    def notify_end_connection(self, client):
        self.__connected_clients.remove(client)


class Client(Thread):

    def __init__(self, connection, address, requests_dictionary, mas_package, server=None):
        Thread.__init__(self)
        self.__connection = connection
        self.__address = address
        self.__requests_dictionary = requests_dictionary
        self.__MAX_PACKAGE = mas_package
        self.__server = server

    def run(self):
        print(f'open connection {self.__connection}')
        data = True
        while data:
            try:
                data = self.__connection.recv(self.__MAX_PACKAGE)
                if data == b'':
                    break
                deserialized_data = self.__deserialize_object(data)
                request_type = self.__get_request_type(deserialized_data)
                handler = self.__requests_dictionary[request_type]
                respond = handler(deserialized_data, self.__connection)
                # print('DEBUG',type(respond), ' ', respond)
                self.__connection.send(self.__serialize_object(respond))
            except Exception as e:
                print(f'Error deserializing data {e}')
        print(f'close connection {self.__connection}')
        self.__connection.close()
        self.__server.notify_end_connection(self)

    @staticmethod
    def __get_request_type(data):
        try:
            print(f'Data i Received {data}')
            # mapped_to_json = json.loads(data)
            return data['requestType']
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
