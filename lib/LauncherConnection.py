class Server(object):
    """
    listening TCP socket for server which available clients connect to server
    dont start listening after create
    """

    def __init__(self):
        pass

    def open_socket(self):
        """
        open socket and allow clients connect to server
        """
        pass

    def close_socket(self):
        """
        close socket, after this clients wont be able connect to server
        """
        pass

    def close_socket_and_all_connections(self):
        """
        close listening socket and connections to all clients
        """
        pass

    def accept_new_client(self):
        """
        return Socket which available communication with new client
        important! blocking the program until connect to the client
        :rtype: Connection
        """
        pass


class Connection(object):
    """
    TCP socket used to communicate between client and server, dont connected after create
    """

    def __init__(self):
        pass

    def close_connection(self):
        """
        close listening socket and end this connection
        """
        pass

    def send_data(self, data):
        """
        send object to second site
        :type data: object
        :param data: object which will be send to second site
        """
        pass

    def receive_data(self):
        """
        receive data from second site and return received object
        important! blocking the program until the message is received
        :rtype object
        """
        pass


# module test
if __name__ == "__main__":
    pass
