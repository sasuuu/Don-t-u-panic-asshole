from lib import request_types as request


class Chunk:

    def __init__(self):
        self.type = request.CHUNK
        self.position = None
        self.object_list = None
