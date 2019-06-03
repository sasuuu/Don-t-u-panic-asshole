import time

ACTIVE_TIME_IN_SECONDS = 10


class Client:

    def __init__(self, address, auth_key):
        self.__address = address
        self.__auth_key = auth_key
        self.__last_received_time = time.time()

    def get_address(self):
        return self.__address

    def get_auth_key(self):
        return self.__auth_key

    def update_last_received_time(self, received_time):
        self.__last_recived_time = received_time

    def is_user_active(self):
        current_time = time.time()
        if current_time - self.__last_received_time > ACTIVE_TIME_IN_SECONDS:
            return False
        else:
            return True
