import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend("TkAgg")

from scipy.io import wavfile

file_path = r"C:\Users\Franck Carmel\PycharmProjects\pythonProject5\audio.wav"

# Datei laden
sample_rate, data = wavfile.read(file_path)
print(len(data),data, sample_rate)

# Prüfe, ob die Datei Mono oder Stereo ist
if len(data.shape) == 1:
    print("Mono-Datei erkannt.")
else:
    print("Stereo-Datei erkannt. Nur ein Kanal wird verwendet.")
    data = data[:, 0]  # Falls Stereo, nutze nur den linken Kanal

# Zeitachse berechnen
time = np.arange(len(data)) / sample_rate
print(f'dieses Signal ist {time} sekunden lang')
# Waveform plotten
plt.figure(figsize=(10, 4))
plt.plot(time, data)
plt.title("Waveform eines Audiosignals")
plt.xlabel("Zeit (s)")
plt.ylabel("Amplitude")
plt.show()

