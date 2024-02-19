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
        pass
    
    def create_audio_from_blob(self, blob, filename="reconstructed.wav"):
        # Décodage du blob en données audio
        audio_bytes = base64.b64decode(blob)
        audio_array = np.frombuffer(audio_bytes, dtype=np.int16)
        # Écriture de l'audio dans un fichier WAV
        write(filename, 44100, audio_array)

    def play_audio(self, filename):
        # Lecture de l'audio
        rate, data = read(filename)
        sd.play(data, rate)
        sd.wait()

if __name__ == "__main__":
    vocal = Vocal()
    
    # Enregistrement de l'audio
    vocal.record_audio()

    # Création du blob à partir de l'audio enregistré
    blob = vocal.create_blob_from_audio()

    # Extraction et re-conversion du blob en audio
    vocal.create_audio_from_blob(blob, "reconstructed_audio.wav")

    # Lecture de l'audio reconstruit
    vocal.play_audio("reconstructed_audio.wav")
