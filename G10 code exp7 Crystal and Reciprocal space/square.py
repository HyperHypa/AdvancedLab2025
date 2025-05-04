import numpy as np
import matplotlib.pyplot as plt

# Create time array
N = 500
t = np.linspace(-1, 1, N)

# Create square pulse: 1 between -0.2 and 0.2, 0 elsewhere
square_pulse = np.where(abs(t) < 0.2, 1, 0)

# Plot
plt.figure(figsize=(8, 4))
plt.plot(t, square_pulse, label="Square Pulse")
plt.title("Square Pulse Waveform")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
