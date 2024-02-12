import socket
import select
from MyDb import *

class Server:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 9001
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_objects = [self.server_socket]
        self.channels = {'A': [], 'B': []}

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(10)
            print("Welcome to the J.M.R Server")
            self.run_server()
        except Exception as e:
            print(f"Error starting server: {e}")
            self.server_socket.close()

    def run_server(self):
        while True:
            try:
                readable, _, _ = select.select(self.socket_objects, [], [])
                for sock in readable:
                    if sock == self.server_socket:
                        self.handle_new_connection(sock)
                    else:
                        self.handle_client_message(sock)
            except Exception as e:
                print(f"Error in server loop: {e}")

    def handle_new_connection(self, server_socket):
        user_socket, address = server_socket.accept()
        print(f"New connection from {address}")
        user_socket.sendall(b"Welcome to the J.M.R Server\nPlease choose a channel: A, B\n")
        self.socket_objects.append(user_socket)

    def handle_client_message(self, client_socket):
        try:
            data = client_socket.recv(1024).decode('utf-8').strip()
            if data:
                if client_socket in self.channels['A']:
                    self.send_to_channel('A', data)
                elif client_socket in self.channels['B']:
                    self.send_to_channel('B', data)
                else:
                    self.join_channel(client_socket, data)
            else:
                self.disconnect_client(client_socket)
        except Exception as e:
            print(f"Error handling message: {e}")
            self.disconnect_client(client_socket)

    def join_channel(self, client_socket, channel):
        if channel in ['A', 'B']:
            self.channels[channel].append(client_socket)
            client_socket.sendall(f"Welcome to channel {channel}\n".encode('utf-8'))
        else:
            client_socket.sendall(b"Invalid channel\n")

    def send_to_channel(self, channel, message):
        for sock in self.channels[channel]:
            try:
                sock.sendall(f"Channel {channel}: {message}\n".encode('utf-8'))
            except Exception as e:
                print(f"Error sending message to channel {channel}: {e}")
                self.disconnect_client(sock)

    def disconnect_client(self, client_socket):
        try:
            client_socket.close()
            self.socket_objects.remove(client_socket)
            for channel in self.channels.values():
                if client_socket in channel:
                    channel.remove(client_socket)
            print(f"Client disconnected: {client_socket}")
        except Exception as e:
            print(f"Error disconnecting client: {e}")

    def get_db(self):
        return self.db

Server().start()
