import pyaudio
import numpy as np
import librosa

pyau = pyaudio.PyAudio()
CHUNK = 1024 * 2
RATE = 44100

stream = pyau.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = RATE,
    frames_per_buffer = CHUNK,
    input = True,
    output = True)

while stream.is_active():
    # input audio
    au_in = stream.read(CHUNK)
    # convert wave
    au_in_wave = np.frombuffer(au_in, dtype = "int16") / float(2**15)
    # process
    pitch, temp = librosa.beat.beat_track(y = au_in_wave, sr = RATE)
    print(pitch)
    # output audio
    au_out = stream.write(au_in)

stream.stop_stream()
stream.close()
pyau.terminate()

print("stop")
