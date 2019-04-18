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
    def __init__(self, connection, address, request_handlers_chain, server=None):
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

    def send_data(self, data: dict):
        bytes_to_send = self.__json_to_byte(data)
        self.__connection.send(bytes_to_send)

    def __handle_data(self, data) -> bytes:
        try:
            json_data = self.__byte_to_json(data)
            respond_to_parse = self.__request_handlers_chain.handle(json_data)
            respond_bytes = self.__json_to_byte(respond_to_parse)
        except (JSONDecodeError, UnicodeDecodeError):
            respond_to_parse = req.respond_error('decode error')
            respond_bytes = self.__json_to_byte(respond_to_parse)
        return respond_bytes

    @staticmethod
    def __byte_to_json(data: bytes) -> dict:
        request_string = data.decode('utf-8')
        # print('DEBUG: request string: ', request_string)  # debug info
        json_data = json.loads(request_string)
        # print('DEBUG: json data: ', json_data)  # debug info
        return json_data

    @staticmethod
    def __json_to_byte(respond_to_parse: dict) -> bytes:
        # print('DEBUG: respond_to_parse: ', respond_to_parse)  # debug info
        respond_str = json.dumps(respond_to_parse)
        respond_bytes = str.encode(respond_str, 'utf-8')
        return respond_bytes


if __name__ == "__main__":
    __testChain = req.EchoRequestHandler(req.PingRequestHandler(req.ServerListRequestHandler()))
    __server = Server(__testChain)
