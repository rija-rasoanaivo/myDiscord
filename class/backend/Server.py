import socket
import select
from MyDb import MyDb

class Server:
    db = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord")
    db.connexion()

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_objects = [self.server_socket]
        self.room_sockets = {}  # Dictionnaire pour stocker les sockets des rooms
        self.clients = {}
        self.host = '127.0.0.1'
        self.port = 9901

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
        self.socket_objects.append(user_socket)
        self.clients[user_socket] = address

        # Récupérer les détails des salles de discussion depuis la base de données
        rooms = self.db.executeRequete("SELECT id_room, name, type_room FROM chatRoom")

        # Créer un socket pour chaque room et les ajouter au dictionnaire
        for room in rooms:
            room_id, room_name, room_type = room
            room_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            room_port = 9000 + room_id  # Utilisez un port différent pour chaque room
            room_socket.bind((self.host, room_port))
            room_socket.listen(10)
            self.socket_objects.append(room_socket)
            self.room_sockets[room_id] = (room_socket, room_name)

        # Envoyer la liste des salles disponibles à l'utilisateur
        room_list = "\n".join([f"{room[0]} - {room[1]}" for room in rooms])
        user_socket.sendall(f"Welcome to the J.M.R Server\nPlease choose a room:\n{room_list}\n".encode('utf-8'))

    def handle_client_message(self, client_socket):
        try:
            data = client_socket.recv(1024).decode('utf-8').strip()
            if data:
                # Gérer la sélection de la salle de discussion par le client
                room_id = int(data)
                if room_id in self.room_sockets:
                    room_socket, _ = self.room_sockets[room_id]
                    # Connecter le client au socket de la room sélectionnée
                    client_socket.sendall(f"Joined room: {room_id}\n".encode('utf-8'))
                    room_socket.accept()
                else:
                    client_socket.sendall(b"Invalid room selection\n")
        except Exception as e:
            print(f"Error handling message: {e}")
            self.disconnect_client(client_socket)

    def disconnect_client(self, client_socket):
        try:
            client_socket.close()
            self.socket_objects.remove(client_socket)
            del self.clients[client_socket]
            print(f"{client_socket.getpeername()} disconnected from the server.")
        except Exception as e:
            print(f"Error disconnecting client: {e}")

if __name__ == "__main__":
    server = Server()
    server.start()
