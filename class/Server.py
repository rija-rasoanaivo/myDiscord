from MyDb import *
import socket
import pyaudio
import threading

class Server:
    db = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord")
    db.connexion()

    def __init__(self, host='127.0.0.1', port=8000):
        self.host = host
        self.port = port

        # Paramètres audio
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024

        # Initialisation de PyAudio
        self.audio = pyaudio.PyAudio()

        # Création du socket TCP
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(10)  # Attente de connexions
        print("Serveur en attente de connexions...")

    # Fonction pour gérer les clients et leur audio
    def handle_client(self, client_socket):
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, output=True, frames_per_buffer=self.CHUNK)
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                stream.write(data)
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            client_socket.close()

    # Nouvelle fonction pour gérer les connexions entrantes
    def accept_clients(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connexion établie avec {addr}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def start(self):
        try:
            accept_thread = threading.Thread(target=self.accept_clients)
            accept_thread.start()
            accept_thread.join()  # Attente indéfinie pour que le thread d'acceptation ne se termine pas
        finally:
            self.server_socket.close()

# Utilisation
if __name__ == "__main__":
    server = Server()
    server.start()
