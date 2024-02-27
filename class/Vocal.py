from Chatting import *
import socket
import pyaudio

class Vocal:
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
        print("Connecting to server...")
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print("Connected to server.")

    # Fonction pour envoyer l'audio au serveur
    def send_audio(self):
        print("Recording and sending audio...")
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        try:
            while True:
                data = stream.read(self.CHUNK)
                self.client_socket.sendall(data)
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            stream.stop_stream()
            stream.close()
            print("Audio stream stopped and closed.")

    def start(self):
        try:
            self.send_audio()
        finally:
            self.client_socket.close()
            print("Connection closed.")

# Utilisation
if __name__ == "__main__":
    vocal = Vocal()
    vocal.start()