import numpy as np

# Given sequences
x_n = np.array([1, 1, 1, 1])  # Time-domain sequence
X_k = np.array([4, 0, 0, 0])  # Frequency-domain sequence

# Compute 4-point DFT
X_dft = np.fft.fft(x_n, n=4)

# Compute 4-point IDFT
x_idft = np.fft.ifft(X_k, n=4)

# Display Results
print("4-Point DFT of x(n):", X_dft)
print("4-Point IDFT of X(k):", x_idft)
