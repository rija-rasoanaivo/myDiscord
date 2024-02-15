import socket
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
            self.get_room_list()
        except Exception as e:
            print(f"Error connecting to server: {e}")

    def get_room_list(self):
        try:
            room_list = self.client_socket.recv(1024).decode('utf-8')
            print(room_list)  # Afficher la liste des rooms proposées par le serveur
        except Exception as e:
            print(f"Error getting room list: {e}")

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
            
            while True:
                # Recevoir et afficher les messages de la salle choisie
                server_message = self.client_socket.recv(1024).decode('utf-8').strip()
                if server_message:
                    print(server_message)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat = Chatting()
    chat.connect_to_server()
    chat.run()
