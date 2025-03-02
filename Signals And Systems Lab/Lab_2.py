import numpy as np
import matplotlib.pyplot as plt

n = np.array([-2, -1, 0, 1, 2])
x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([5, 4, 3, 2, 1])

# Basic operations
add = x1 + x2
mul = x1 * x2
scaling = 0.2 * x1  # Scaling with alpha = 0.2
shifting_n = n - 2  # Correct shifting
folding = np.flip(x1)

plt.figure(figsize=(12, 10))

plt.subplot(4, 2, 1)
plt.stem(n, x1)
plt.xlabel('Time')
plt.ylabel("Amplitude")
plt.title("Original Signal X1")
plt.grid()

plt.subplot(4, 2, 2)
plt.stem(n, x2)
plt.xlabel('Time')
plt.ylabel("Amplitude")
plt.title("Original Signal X2")
plt.grid()

plt.subplot(4, 2, 3)
plt.stem(n, add)
plt.xlabel('Time')
plt.ylabel("Amplitude")
plt.title("Addition: X1 + X2")
plt.grid()

plt.subplot(4, 2, 4)
plt.stem(n, mul)
plt.xlabel('Time')
plt.ylabel("Amplitude")
plt.title("Multiplication: X1 * X2")
plt.grid()

plt.subplot(4, 2, 5)
plt.stem(n, scaling)
plt.xlabel('Time')
plt.ylabel("Amplitude")
plt.title("Scaling: 0.2 * X1")
plt.grid()

plt.subplot(4, 2, 6)
plt.stem(shifting_n, x1)  # Correcting the shifting
plt.xlabel('Time')
plt.ylabel("Amplitude")
plt.title("Time Shifting: X1[n-2]")
plt.grid()
plt.tight_layout()
plt.show()
