import sounddevice as sd
import base64
import numpy as np
from scipy.io.wavfile import read, write
from Chatting import *

class Vocal:
    
    def __init__(self):
        self.db = Server.db

    def record_audio(self, filename="recording.wav", duration=5):
        # Enregistrement de l'audio
        freq = 44100  # Fréquence d'échantillonnage
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
        sd.wait()

        # Écriture de l'audio dans un fichier WAV
        write(filename, freq, recording)

    def convert_into_binary(self, filename):
        # Conversion de l'audio en données binaires
        audio_array = np.array(read(filename)[1], dtype=float)
        audio_array /= np.max(np.abs(audio_array))  # Normalisation entre -1 et 1
        audio_bytes = audio_array.tobytes()
        return audio_bytes
    
    def insert_audio_into_db(self, name, audio_binary, type_room):
        # Insérer l'audio dans la base de données
        sql = "INSERT INTO vocalChatRoom (name, vocal_message, type_room) VALUES (%s, %s, %s)"
        values = (name, audio_binary, type_room)
        self.db.executeRequete(sql, values)
        self.db.fetch()

if __name__ == "__main__":
    vocal = Vocal()
    vocal.record_audio()
    binary_data = vocal.convert_into_binary("recording.wav")

    # Insérer l'audio dans la base de données
    vocal.insert_audio_into_db("Recording", binary_data, "room_type")
