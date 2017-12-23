import socket


class TCPRemoteClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP over IP
        self.is_alive = False

    def connect(self):
        if not self.is_alive:
            self.connection.connect((self.host, self.port))
            self.is_alive = True

    def transfer(self, data, flags=None):
        if not self.is_alive:
            raise ConnectionError
        self.connection.send(data, flags=flags)

    def receive(self, buffer_size, flags=None):
        if not self.is_alive:
            raise ConnectionError
        return self.connection.recv(buffer_size, flags=flags)

    def hang_up(self):
        if self.is_alive:
            self.connection.close()
            self.is_alive = False
