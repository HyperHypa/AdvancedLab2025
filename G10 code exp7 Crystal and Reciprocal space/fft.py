import numpy as np
import matplotlib.pyplot as plt

N = 500
t = np.linspace(-1, 1, N)
square_pulse = np.where(abs(t) < 0.2, 1, 0)


fft_result = np.fft.fftshift(np.fft.fft(square_pulse))
freq = np.fft.fftshift(np.fft.fftfreq(N, d=(t[1]-t[0])))


plt.plot(freq, abs(fft_result))
plt.title("FFT of Square Pulse")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.grid()
plt.show()
