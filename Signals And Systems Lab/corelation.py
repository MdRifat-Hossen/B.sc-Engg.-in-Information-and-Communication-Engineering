import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Define the input signals
x = [1, 2, 3, 4]  # Signal 1
h = [1, 0.5, 0.25]  # Signal 2

# Perform Auto-correlation (Signal correlated with itself)
auto_corr = np.correlate(x, x, mode='full')

# Perform Cross-correlation (Signal x correlated with h)
cross_corr = np.correlate(x, h, mode='full')

# Print the results
print("Signal 1 (x):", x)
print("Signal 2 (h):", h)
print("Auto-correlation of x (y):", auto_corr)
print("Cross-correlation of x and h (y):", cross_corr)

# Plotting the signals and correlations
plt.figure(figsize=(14, 8))

# Signal 1 (x)
plt.subplot(4, 1, 1)
plt.stem(range(len(x)), x)
plt.title("Signal 1 (x)")
plt.xlabel("n")
plt.ylabel("x[n]")

# Signal 2 (h)
plt.subplot(4, 1, 2)
plt.stem(range(len(h)), h)
plt.title("Signal 2 (h)")
plt.xlabel("n")
plt.ylabel("h[n]")

# Auto-correlation
plt.subplot(4, 1, 3)
plt.stem(range(-(len(x) - 1), len(x)), auto_corr)
plt.title("Auto-correlation of Signal 1 (x)")
plt.xlabel("Lag (n)")
plt.ylabel("Auto-corr")

# Cross-correlation
plt.subplot(4, 1, 4)
plt.stem(range(-(len(h) - 1), len(x)), cross_corr)
plt.title("Cross-correlation of x and h")
plt.xlabel("Lag (n)")
plt.ylabel("Cross-corr")

plt.tight_layout()
plt.show()
