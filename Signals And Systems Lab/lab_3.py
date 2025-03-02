import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Compute the convolution
def compute_convolution(signal1, signal2):
    conv_result = convolve(signal1, signal2, mode='full', method='auto')
    return conv_result

# Generate the sine wave signal
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # Time axis

freq = 5  # Frequency of sine wave
sin_signal = np.sin(2 * np.pi * freq * t)  # Sinusoidal signal

# Compute auto-convolution (signal convolved with itself)
auto_conv = compute_convolution(sin_signal, sin_signal)

# Generate noisy signal
noise = np.random.normal(0, 0.5, fs)  # Gaussian noise
noisy_signal = sin_signal + noise  # Add noise to the signal

# Compute convolution with noisy signal
conv_noisy = compute_convolution(sin_signal, noisy_signal)

# Plot the results
plt.figure(figsize=(12, 8))

# Plot auto-convolution
plt.subplot(3, 1, 1)
plt.plot(auto_conv)
plt.title("Autoconvolution of a Sinusoidal Signal")
plt.xlabel("Samples")
plt.ylabel("Convolution Output")
plt.grid()

# Plot convolution with noisy signal
plt.subplot(3, 1, 2)
plt.plot(conv_noisy)
plt.title("Convolution with Noisy Signal")
plt.xlabel("Samples")
plt.ylabel("Convolution Output")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(sin_signal)
plt.title("Convolution with Noisy Signal")
plt.xlabel("Samples")
plt.ylabel("Convolution Output")
plt.grid()


plt.tight_layout()
plt.show()
