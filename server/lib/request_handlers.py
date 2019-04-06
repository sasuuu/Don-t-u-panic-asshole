from abc import abstractmethod, ABC
from enum import Enum


class RequestType(Enum):
    ECHO_TEST = 1
    MESSAGE = 2
    PING = 3
    SERVER_LIST = 4
    ERROR = 5


def respond_error(message: str):
    return {'type': RequestType.ERROR.value, 'message': message}


class RequestHandler(ABC):

    def __init__(self, next_handler=None):
        self.__next_handler = next_handler
        self._request_type = None

    def add_next(self, next_handler):
        self.__next_handler = next_handler

    @staticmethod
    def _respond_message(message):
        return {'type': RequestType.MESSAGE.value, 'message': message}

    def _check_can_you_handle_request(self, request) -> bool:
        if request['type'] == self._request_type.value:
            return True
        else:
            return False

    @abstractmethod
    def _handle_request(self, request):
        pass

    def handle(self, request) -> dict:
        if self._check_can_you_handle_request(request):
            return self._handle_request(request)
        else:
            if self.__next_handler is None:
                return respond_error("unsupported request")
            else:
                return self.__next_handler.handle(request)


# todo implement this handler
class ServerListRequestHandler(RequestHandler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self._request_type = RequestType.SERVER_LIST

    def _handle_request(self, request):
        return {'type': RequestType.SERVER_LIST.value, 'list': [('127.0.0.1', 'alpha'), ('127.0.0.2', 'beta')]}


class EchoRequestHandler(RequestHandler):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self._request_type = RequestType.ECHO_TEST

    def _handle_request(self, request):
        try:
            return self._respond_message(request['message'])
        except KeyError:
            return respond_error('syntax error')


class PingRequestHandler(RequestHandler):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self._request_type = RequestType.PING

    def _handle_request(self, request):
        return self._respond_message('pong')


if __name__ == "__main__":
    testChain = EchoRequestHandler(PingRequestHandler(ServerListRequestHandler()))
    print(testChain.handle({'type': RequestType.PING.value, 'message': "xd"}))
