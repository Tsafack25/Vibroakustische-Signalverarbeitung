import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Lade die WAV-Datei ---
file_path = r"C:\Users\Franck Carmel\PycharmProjects\pythonProject5\audio.wav"
sample_rate, data = wavfile.read(file_path)
print(len(data), data.shape, sample_rate)

# Prüfe, ob die Datei Mono oder Stereo ist
if len(data.shape) == 1:
    print("Mono-Datei erkannt.")
else:
    print("Stereo-Datei erkannt. Nur ein Kanal wird verwendet.")
    Channel_1 = data[:, 0]
    Channel_2 = data[:, 1]


# Zeitachse berechnen ---
time = np.arange(len(data)) / sample_rate
print(f"Dieses Signal ist {time} Sekunden lang")


# Darstellung der Channel_2
plt.figure(figsize=(12, 5))
plt.plot(time, Channel_1, label="Originales Signal", color='blue', alpha=0.5)
plt.title("Waveform eines Audiosignals(Channel-1)")
plt.xlabel("Zeit (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# Darstellung der Channel_2
plt.figure(figsize=(12, 5))
plt.plot(time, Channel_2, label="Originales Signal", color='red', alpha=0.5)
plt.title("Waveform eines Audiosignals (Channel_2)")
plt.xlabel("Zeit (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()