import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import hilbert

# Lade die WAV-Datei
file_path = r"C:\Users\Franck Carmel\PycharmProjects\pythonProject5\audio.wav"
# Datei laden
sample_rate, data = wavfile.read(file_path)
print(len(data),data.shape, sample_rate)

# Prüfe, ob die Datei Mono oder Stereo ist
if len(data.shape) == 1:
    print("Mono-Datei erkannt.")
else:
    print("Stereo-Datei erkannt. Nur ein Kanal wird verwendet.")
    data = data[:, 0]  # Falls Stereo, nutze nur den linken Kanal

# Berechnung der Amplitude Envelope mit Hilbert-Transformation
analytic_signal = hilbert(data)
amplitude_envelope = np.abs(analytic_signal).flatten()

# Darstellung der originalen Waveform und der Amplitude Envelope
time = np.linspace(0, len(data) / sample_rate, num=len(data))
print(f'dieses Signal ist {time} sekunden lang')

plt.figure(figsize=(10, 4))
plt.plot(time, data, label="Originales Signal", color='blue', alpha=0.6)
plt.plot(time, amplitude_envelope, label="Amplitude Envelope", color = 'red')
#plt.plot(time, data, label="Original Signal")
plt.title("Amplitude Envelope")
plt.xlabel("Zeit (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

