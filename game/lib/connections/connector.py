import socket
import pickle
import json
from lib import errors_provider
from lib.connections.request.login_data import Login
from lib.connections.request.server_list import ServerList


class Connector:

    def __init__(self):
        self.__SERVER_IP_ADDRESS = None
        self.__SERVER_PORT = None
        self.__MAX_PACKAGE = None
        self.__socket = None
        self.__server_config_file_dir = "config/server_config.json"
        self.__read_config()
        self.__bind_socket()

    def __read_config(self):
        try:
            with open(self.__server_config_file_dir) as json_file:
                config_file = json.load(json_file)
                self.__SERVER_IP_ADDRESS = config_file['ipAddress']
                self.__SERVER_PORT = config_file['portNumber']
                self.__MAX_PACKAGE = config_file['maxPackage']
        except Exception as e:
            print(f'Error reading config file {e}')
            exit(errors_provider.CONFIG_ERROR)

    def __bind_socket(self):
        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.connect((self.__SERVER_IP_ADDRESS, self.__SERVER_PORT))
        except socket.error as exc:
            print(f'Exception while connecting to server {exc}')

    def login_authorize(self, username, password):
        authorized_user = Login(username, password)
        try:
            self.__socket.send(self.__serialize_object(authorized_user))
            server_response = self.__deserialize_object((self.__socket.recv(self.__MAX_PACKAGE)))
            print(f'Server responded with {server_response}')
            return server_response['response']
        except Exception as e:
            print(f'Error sending and receiving data from server (Login) {e}')
        return False

    def get_servers(self):
        servers_list = ServerList()
        try:
            self.__socket.send(self.__serialize_object(servers_list))
            server_response = self.__deserialize_object(self.__socket.recv(self.__MAX_PACKAGE))
            print(f'Server responded with {server_response}')
            return server_response['response']
        except Exception as e:
            print(f'Error sending and receiving data from server (Server list) {e}')
        return []

    @staticmethod
    def __serialize_object(sending_object):
        return pickle.dumps(json.dumps(vars(sending_object)))

    @staticmethod
    def __deserialize_object(sending_object):
        return json.loads(pickle.loads(sending_object))

