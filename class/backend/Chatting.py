import socket
from Message import *
import threading

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

    def send_message(self):
        while True:
            message_content = input("Enter message: ")
            if message_content:
                self.client_socket.sendall(message_content.encode("utf-8"))
            else:
                print("Message cannot be empty")

    def run(self):
        try:
            room_choice = input("Choose a room by entering its number: ")
            self.client_socket.sendall(room_choice.encode("utf-8"))
            
            # Vous pouvez continuer ici pour recevoir et afficher les messages dans la salle choisie
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat = Chatting()
    chat.connect_to_server()
    chat.run()