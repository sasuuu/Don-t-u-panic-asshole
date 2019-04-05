import socket
import os
import sys
import json
import _thread as thread
from json import JSONDecodeError

from lib import errors_provider as error

from lib import request_handlers as req


class Server:
    def __init__(self, request_handlers_chain):
        self.__IP_ADDRESS = None
        self.__PORT_NUMBER = None
        self.__MAX_HOSTS = None
        self.__socket = None
        self.__connected_users = []
        self.__request_handlers_chain = request_handlers_chain
        self.__config_file = "config/server_config.json"
        self.__read_config()
        self.__handle_binding()
        self.__listen_for_connections()

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
            thread.start_new_thread(self.__handle_connection, (connection, address))

    def __handle_connection(self, connection, address):
        self.__connected_users.append([connection, address])
        print(f'Users that are connected {self.__connected_users}')
        data = True
        while data:
            data = connection.recv(1024)
            print(f'Receiving data from {address} = {data}')
            respond = self.__handle_data(data)
            connection.send(respond)
        self.__connected_users.remove([connection, address])
        connection.close()
        print(f'User disconnect {address}')

    def __handle_data(self, data) -> bytes:
        try:
            request_string = data.decode('utf-8')
            print('request string: ', request_string)  # debug info
            json_data = json.loads(request_string)
            print('json data: ', json_data)  # debug info
            respond_to_parse = self.__request_handlers_chain.handle(json_data)
            print('respond_to_parse: ', json_data)  # debug info
            respond_str = json.dumps(respond_to_parse)
            respond_bytes = str.encode(respond_str)
        except (JSONDecodeError, UnicodeDecodeError):
            # todo return json respond
            respond_bytes = b"decode error\n"
        return respond_bytes


if __name__ == "__main__":
    __testChain = req.EchoRequestHandler(req.PingRequestHandler(req.ServerListRequestHandler()))
    __server = Server(__testChain)
