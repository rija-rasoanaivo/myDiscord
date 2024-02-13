from PrivateChatRoom import *
from Login import *
from Register import *
import socket
import threading

class Message:

    def __init(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_objects = [self.server_socket]
        self.host = '82.165.185.52'
        self.port = 9001