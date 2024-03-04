from MyDb import *
import socket
import pyaudio
import threading

class Server:
    db = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord")
    db.connexion()

    def __init__(self):
        # audio settings
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024

        # Initialize the PyAudio instance
        self.audio = pyaudio.PyAudio()

        self.server_socket = None  

    def create_server_socket(self, host='127.0.0.1', port=8000):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server_socket.bind((host, port))
            self.server_socket.listen(10)  # Accepts up to 10 connections
            print("Serveur en attente de connexions...")
        except Exception as e:
            print(f"Erreur lors de la liaison du socket : {e}")
            if self.server_socket:
                self.server_socket.close()
            self.server_socket = None

    def handle_client(self, client_socket):
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, output=True, frames_per_buffer=self.CHUNK)
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                stream.write(data)
        except Exception as e:
            print(f"Erreur lors de la gestion du client : {e}")
        finally:
            client_socket.close()

    def accept_clients(self):
        while True:
            try:
                client_socket, addr = self.server_socket.accept()
                print(f"Connexion établie avec {addr}")
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
            except Exception as e:
                print(f"Erreur lors de l'acceptation des clients : {e}")

    def start_server(self):
        if not self.server_socket:
            self.create_server_socket()  
        else:
            print("Le socket serveur existe déjà. Attendez que le serveur actuel se termine.")
            return  

        try:
            accept_thread = threading.Thread(target=self.accept_clients)
            accept_thread.start()
            accept_thread.join()  
        finally:
            self.server_socket.close()
            self.audio.terminate()

    def stop_server(self):
        if self.server_socket:
            self.server_socket.close()
            print("Socket serveur fermé.")
        if self.audio:
            self.audio.terminate()
            print("Audio arrêté.")


# Usage
if __name__ == "__main__":
    server = Server()
    server.create_server_socket()  
    server.start_server()  
    server.stop_server()