from Chatting import *
import socket
import pyaudio

# Class to record audio and send it to the server
class Vocal:
    def __init__(self, host='127.0.0.1', port=8000):
        self.host = host
        self.port = port

        # setting 
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024

    
        self.audio = pyaudio.PyAudio()

        # Create a socket to connect to the server
        print("Connecting to server...")
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print("Connected to server.")

        # Flag to check if the audio is being recorded
        self.is_recording = False

    # Method to send audio to the server
    def send_audio(self):
        print("Recording and sending audio...")
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        try:
            while self.is_recording:
                data = stream.read(self.CHUNK)
                self.client_socket.sendall(data)
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            stream.stop_stream()
            stream.close()
            print("Audio stream stopped and closed.")

    # Method to start recording audio
    def start(self):
        self.is_recording = True
        try:
            self.send_audio()
        finally:
            self.client_socket.close()
            print("Connection closed.")

    # Method to stop recording audio
    def stop(self):
        print("Stopping audio recording on vocal...")
        self.is_recording = False


if __name__ == "__main__":
    vocal = Vocal()
    vocal.start()