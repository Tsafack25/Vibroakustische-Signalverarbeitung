import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import hilbert, butter, filtfilt

# Lade die WAV-Datei ---
file_path = r"C:\Users\Franck Carmel\PycharmProjects\pythonProject5\audio.wav"
sample_rate, data = wavfile.read(file_path)
print(len(data), data.shape, sample_rate)

# Prüfe, ob die Datei Mono oder Stereo ist
if len(data.shape) == 1:
    print("Mono-Datei erkannt.")
else:
    print("Stereo-Datei erkannt. Nur ein Kanal wird verwendet.")
    #data = data[:,0]  # Falls Stereo, nutze nur den linken Kanal

# Berechnung der Amplitude Envelope ---
analytic_signal = hilbert(data)
amplitude_envelope = np.abs(analytic_signal)

# Glättung der Amplitude Envelope mit Tiefpassfilter ---
def lowpass_filter(signal, cutoff_freq, sample_rate, order=5):
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff_freq / nyquistSSSS
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, signal)

cutoff_frequency = 10  # Grenzfrequenz für die Glättung in Hz
#smoothed_envelope = lowpass_filter(amplitude_envelope, cutoff_frequency, sample_rate)

# Zeitachse berechnen ---
time = np.arange(len(data)) / sample_rate
print(f"Dieses Signal ist {time} Sekunden lang")

# Darstellung der Waveform und der geglätteten Amplitude Envelope ---
plt.figure(figsize=(12, 5))
plt.plot(time, data[:,0], label="Originales Signal", color='blue', alpha=0.5)
plt.plot(time, data[:,1], label="Geglättete Amplitude Envelope", color='red', alpha=0.5)
plt.title("Amplitude Envelope (Geglättet)")
plt.xlabel("Zeit (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
