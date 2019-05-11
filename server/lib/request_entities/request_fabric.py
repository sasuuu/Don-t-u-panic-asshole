from abc import ABC, abstractmethod

from lib import request_types

from lib.db.db_connection import DataBase


def get_request_dictionary():
    sql = DataBase()
    return {
        request_types.LOGIN: LoginRequestHandler(sql),
        request_types.GET_SERVERS: ServerList(sql),
    }


class RequestHandler(ABC):

    def __init__(self, db):
        self._DB = db

    @abstractmethod
    def handle(self, data, connection):
        pass


class LoginRequestHandler(RequestHandler):

    def handle(self, data, connection):
        user = data['username']
        password = data['password']
        (resoult,) = self._DB.make_query(f"SELECT count(*) FROM player where password = '{password}' and nick='{user}'")[0]
        print(resoult)
        if resoult == 1:
            print('user ' + user + '  log in')
            return {"request_type": request_types.LOGIN_RESULT, "response": 'True'}
        elif resoult == 0:
            print('user ' + user + '  fail log in')
            return {"request_type": request_types.LOGIN_RESULT, "response": 'False'}
        else:
            raise ImportError('data base return inconsistency result')


class ServerList(RequestHandler):

    def handle(self, data, connection):
        names = ["Server Krzemień", "Server Kulig", "Server Merta", "Server Kwilosz", "Server Krzystanek",
                 "Server Łyś", "Server Król"]
        return {"request_type": request_types.SERVER_LISTS, "response": names}
