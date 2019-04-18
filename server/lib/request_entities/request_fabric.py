from lib import request_types
from lib.request_entities.server_list_response import ServerList
from lib.request_entities.login_response import LoginResponse


def return_login(data, connection):
    print(f'Received {data}')
    server_authorization = LoginResponse('True')
    return server_authorization


def return_servers(data, connection):
    print(f'Received {data}')
    names = ["Server Krzemień", "Server Kulig", "Server Merta", "Server Kwilosz", "Server Krzystanek",
             "Server Łyś", "Server Król"]
    server_list = ServerList(names)
    return server_list


def get_request_dictionary():
    return {
        request_types.LOGIN: (lambda data, connection: return_login(data, connection)),
        request_types.GET_SERVERS: (lambda data, connection: return_servers(data, connection)),
        request_types.NOT_FOUND: (lambda data, connection: print('Request not found'))
    }