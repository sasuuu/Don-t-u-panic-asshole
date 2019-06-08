
class ChunkProvider:

    def __init__(self):
        #self.__all_chunks = self.__udp_repository.get_all_chunks()
        pass

    def get_specified_chunk(self, chunk_list):
        returned_chunks = []
        for chunk in chunk_list:
            x_chunk = chunk[0]
            y_chunk = chunk[1]
            returned_chunks.append(self.__all_chunks[x_chunk][y_chunk])
        return returned_chunks

