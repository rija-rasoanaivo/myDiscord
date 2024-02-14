import socket
from Message import Message

class Chatting:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1'
        self.port = 9901

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Connected to server")
            self.receive_messages()
        except Exception as e:
            print(f"Error connecting to server: {e}")

    def send_message(self, message_content):
        try:
            self.client_socket.sendall(message_content.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message: {e}")

    def receive_messages(self):
        try:
            while True:
                data = self.client_socket.recv(1024).decode('utf-8').strip()
                if data:
                    print(data)
                else:
                    print("Disconnected from server")
                    break
        except Exception as e:
            print(f"Error receiving message: {e}")

if __name__ == "__main__":
    chatting = Chatting()
    chatting.connect_to_server()
