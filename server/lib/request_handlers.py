from abc import abstractmethod, ABC
from enum import Enum


class RequestType(Enum):
    ECHO_TEST = 1
    MESSAGE = 2
    PING = 3


class RequestHandler(ABC):

    def __init__(self, next_handler=None):
        self.__next_handler = next_handler
        self._request_type = None

    def add_next(self, next_handler):
        self.__next_handler = next_handler

    def _check_can_you_handle(self, request) -> bool:
        if request['type'] == self._request_type:
            return True
        else:
            return False

    @abstractmethod
    def _handle_request(self, request):
        pass

    def try_handle(self, request) -> dict:
        if self._check_can_you_handle(request):
            return self._handle_request(request)
        else:
            if self.__next_handler is None:
                return None
            else:
                return self.__next_handler.try_handle(request)


# todo implement this handler
# class ServerListRequestHandler(RequestHandler):
#     def _handle_request(self, request):
#         pass
#
#     def _check_can_you_handle(self, request) -> bool:
#         pass


class EchoRequestHandler(RequestHandler):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self._request_type = RequestType.ECHO_TEST

    def _handle_request(self, request):
        return {'type': RequestType.MESSAGE, 'message': request['message']}


class PingRequestHandler(RequestHandler):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self._request_type = RequestType.PING

    def _handle_request(self, request):
        return {'type': RequestType.MESSAGE, 'message': 'pong'}


if __name__ == "__main__":
    testChain = EchoRequestHandler(PingRequestHandler())
    print(testChain.try_handle({'type': RequestType.PING, 'message': "xd"}))
