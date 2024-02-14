from PrivateChatRoom import *
from Login import *
from Register import *
import socket
import threading

class Message:

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_objects = [self.client_socket]
        self.chatroom = {'id_room_1': [], 'id_room_2': []}
        self.host = '127.0.0.1'
        self.port = 9901
        self.client_socket.connect((self.host, self.port))

    def send_message(self):
        while True:
            message = input("> ")
            self.client_socket.send(message.encode("utf-8"))

    def choose_channel(self):
        channel = input("Please choose a channel: A, B\n")
        self.client_socket.sendall(channel.encode('utf-8'))

    def thread_send(self):
        writing_thread = threading.Thread(target=self.send_message)
        writing_thread.daemon = True
        writing_thread.start()

    def run():
        message = Message()
        message.choose_channel()
        message.thread_send()
        while True:
            server_message = message.client_socket.recv(1024).decode('utf-8')
            print(server_message)
            print("> ", end='', flush=True)

if __name__ == "__main__":
    Message.run()
    

