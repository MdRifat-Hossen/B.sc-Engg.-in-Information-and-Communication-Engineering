import numpy as np
import matplotlib.pyplot as plt

# Generate signals
n = np.arange(-10, 11)
x = np.sin(2 * np.pi * 0.1 * n)  # Sinusoidal signal
y = np.cos(2 * np.pi * 0.1 * n)  # Cosine signal

# Compute autocorrelation and cross-correlation
auto_corr = np.correlate(x, x, mode='full')
cross_corr = np.correlate(x, y, mode='full')

# Plot results
plt.figure(figsize=(12, 5))

plt.subplot(2, 1, 1)
plt.stem(auto_corr)
plt.title("Autocorrelation of x(n)")
plt.xlabel("Lag")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(cross_corr)
plt.title("Cross-correlation between x(n) and y(n)")
plt.xlabel("Lag")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
