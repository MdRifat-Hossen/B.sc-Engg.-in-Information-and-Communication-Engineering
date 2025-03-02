import numpy as np
import matplotlib.pyplot as plt

# Given signals
n = np.arange(-2, 2)  # Original indices for z
n1 = np.arange(0, 4)  # Indices for x and y
x = np.array([1, 0, 3, 4])
y = np.array([1, 1, 1, 1])
z = np.array([3, -1, 0, -4])
n3=np.arange(-2,2)
# Signal Addition
sum_xy = x + y

# Folding (Reversing) of signal z
z1=np.flip(z)

# Plot results
plt.figure(figsize=(10, 4))

# Plot x + y
plt.subplot(1, 2, 1)
plt.stem(n1, sum_xy)
plt.title("Signal Addition (x + y)")
plt.xlabel("Index")
plt.ylabel("Amplitude")
plt.grid()

# Plot folded z
plt.subplot(1, 2, 2)
plt.stem(n3,z1)  # Fixing the index range
plt.title("Folding of Signal z")
plt.xlabel("Index")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
