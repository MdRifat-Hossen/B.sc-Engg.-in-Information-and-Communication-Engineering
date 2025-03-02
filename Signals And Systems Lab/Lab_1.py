import numpy as np
import matplotlib.pyplot as plt

# Define the discrete-time index
n = np.arange(-10, 10, 1)

# Impulse Function
impulse = np.where(n == 0, 1, 0)

# Step Function
step = np.where(n >= 0, 1, 0)

# Ramp Function
ramp = np.where(n >= 0, n, 0)

# Plot the signals
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.stem(n, impulse)
plt.title("Impulse Function δ[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(1, 3, 2)
plt.stem(n, step)
plt.title("Step Function u[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(1, 3, 3)
plt.stem(n, ramp)
plt.title("Ramp Function r[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
