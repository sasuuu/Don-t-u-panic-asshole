from lib import request_types as request
from lib.chunk_provider import ChunkProvider


class RequestHandler:

    def __init__(self):
        self.__dictionary = self.__get_dictionary()
        self.__chunk_provider = ChunkProvider()

    def __get_dictionary(self):
        return {
            request.GET_CHUNKS: (lambda data, connection: self.__handle_chunks(data)),
            request.UPDATE_POSITION: (lambda data, connection: self.__handle_position_update(data))
        }

    def handle_request(self, request_type, data):
        self.__dictionary[request_type].__call__(data)

    def __handle_chunks(self, data):
        return self.__chunk_provider.get_specified_chunk(data['positions'])

    def __handle_position_update(self, data, connection):
        pass


