import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy.io import wavfile
import librosa
import librosa.display

# Lade die WAV-Datei (SciPy für Waveform-Darstellung)
file_path = r"C:\Users\Franck Carmel\PycharmProjects\pythonProject5\audio.wav"
sample_rate, data = wavfile.read(file_path)

# Prüfe, ob die Datei Mono oder Stereo ist
if len(data.shape) == 1:
    print("Mono-Datei erkannt.")
else:
    print("Stereo-Datei erkannt. Nur ein Kanal wird verwendet.")
    data = data[:, 0]  # Falls Stereo, nutze nur den linken Kanal

# Zeitachse berechnen
time = np.arange(len(data)) / sample_rate
print(f'Dieses Signal ist {time[-1]:.2f} Sekunden lang')

# Wellenform (Zeitbereich) darstellen
plt.figure(figsize=(10, 4))
plt.plot(time, data, color='blue')
plt.title("Waveform des Audiosignals")
plt.xlabel("Zeit (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# Lade die WAV-Datei mit Librosa für das Spektrogramm
data_librosa, sample_rate = librosa.load(file_path, sr=None)

# Berechnung des Short-Time Fourier Transform (STFT)
S = np.abs(librosa.stft(data_librosa))

# Umwandlung in dB-Skala
S_db = librosa.amplitude_to_db(S, ref=np.max)

#  Spektrogramm darstellen
plt.figure(figsize=(10, 5))
librosa.display.specshow(S_db, sr=sample_rate, x_axis='time', y_axis='log', cmap='magma')
plt.colorbar(label='dB')
plt.title('Spektrogramm der Audiodatei')
plt.xlabel('Zeit (s)')
plt.ylabel('Frequenz (Hz)')
plt.show()
