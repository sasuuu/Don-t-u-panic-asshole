from lib import request_types as request


class Chunk:

    def __init__(self, position):
        self.type = request.CHUNK
        self.position = position
        self.object_list = None
