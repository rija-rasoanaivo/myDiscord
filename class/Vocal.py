# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io.wavfile import read
import wavio as wv

class Vocal:
    
    def __init__(self):
        pass


    def register(self):
        # Sampling frequency # 44100 is the standard for audio in image per second
        freq = 44100

        # Recording duration
        duration = 5

        # Start recorder with the given values of 
        # duration and sample frequency
        recording = sd.rec(int(duration * freq), 
                        samplerate=freq, channels=2)

        # Record audio for the given number of seconds
        sd.wait()

        # This will convert the NumPy array to an audio
        # file with the given sampling frequency
        write("recording0.wav", freq, recording)

    def play(self):
        # Read the audio file using scipy
        rate, data = read("recording0.wav")

        # Play the audio file
        sd.play(data, rate)
        sd.wait()



if __name__ == "__main__":
    vocal = Vocal()
    # vocal.register()
    vocal.play()
    