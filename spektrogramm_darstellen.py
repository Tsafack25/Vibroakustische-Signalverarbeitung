import numpy as np
import librosa
import librosa.display
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Lade die WAV-Datei mit Librosa
file_path = r"C:\Users\Franck Carmel\PycharmProjects\pythonProject5\audio.wav"
data, sample_rate = librosa.load(file_path, sr=None)

# Berechnung des Short-Time Fourier Transform
S = np.abs(librosa.stft(data))

# Umwandlung in dB-Skala
S_db = librosa.amplitude_to_db(S, ref=np.max)

# Darstellung des Spektrogramms
plt.figure(figsize=(10, 5))
librosa.display.specshow(S_db, sr=sample_rate, x_axis='time', y_axis='log', cmap='magma')
plt.colorbar(label='dB')
plt.title('Spektrogramm der Audiodatei')
plt.xlabel('Zeit (s)')
plt.ylabel('Frequenz (Hz)')
plt.show()
