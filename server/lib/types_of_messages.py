from enum import Enum


class RequestType(Enum):
    ECHO_TEST = 1
    MESSAGE = 2
    PING = 3
    SERVER_LIST = 4
    ERROR = 5
