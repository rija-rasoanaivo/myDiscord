import sounddevice as sd
import base64
import numpy as np
from scipy.io.wavfile import read, write

class Vocal:
    
    def __init__(self):
        pass

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
        audio_bytes = audio_array.tobytes()
        return base64.b64encode(audio_bytes).decode("utf-8")
    
    def decode_from_binary(self, binary_data):
        # Décodage des données binaires en audio
        audio_bytes = base64.b64decode(binary_data)
        audio_array = np.frombuffer(audio_bytes, dtype=float)
        return audio_array

    def play_audio(self, filename):
        # Lecture de l'audio
        freq, audio_array = read(filename)
        sd.play(audio_array, freq)
        sd.wait()

if __name__ == "__main__":
    vocal = Vocal()
    vocal.record_audio()
    binary_data = vocal.convert_into_binary("recording.wav")
    audio_array = vocal.decode_from_binary(binary_data)
    vocal.play_audio(audio_array)