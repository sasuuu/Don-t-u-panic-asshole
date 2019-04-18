from lib import request_types


def return_login(data, connection):
    return {"respond": 'True'}


def return_servers(data, connection):
    names = ["Server Krzemień", "Server Kulig", "Server Merta", "Server Kwilosz", "Server Krzystanek",
             "Server Łyś", "Server Król"]
    return {"serverList": names}


def get_request_dictionary():
    return {
        request_types.LOGIN: (lambda data, connection: return_login(data, connection)),
        request_types.GET_SERVERS: (lambda data, connection: return_servers(data, connection)),
    }