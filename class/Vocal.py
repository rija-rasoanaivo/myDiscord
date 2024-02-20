import sounddevice as sd
import numpy as np
from scipy.io.wavfile import read, write
from Chatting import *
from MyDb import MyDb

class Vocal:
    
    def __init__(self):
        self.db = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord")

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

    def get_audio_from_db(self, name):
        # Récupérer l'audio de la base de données par son nom
        sql = "SELECT vocal_message FROM vocalChatRoom WHERE name = %s"
        result = self.db.fetch(sql, (name,))
        if result:
            return result[0][0]
        else:
            print("Aucun enregistrement audio trouvé avec le nom spécifié.")
            return None

    def play_audio(self, audio_array, freq=70000):
        # Lecture de l'audio
        sd.play(audio_array, freq)
        sd.wait()

# Utilisation
if __name__ == "__main__":
    vocal = Vocal()
    
    # Enregistrement de l'audio dans la base de données
    vocal.record_audio()
    binary_data = vocal.convert_into_binary("recording.wav")
    vocal.insert_audio_into_db("Recording", binary_data, "room_type")

    # Récupération de l'audio depuis la base de données
    audio_from_db = vocal.get_audio_from_db("Recording")

    # Lecture de l'audio récupéré
    if audio_from_db:
        decoded_audio = np.frombuffer(audio_from_db, dtype=float)
        vocal.play_audio(decoded_audio)