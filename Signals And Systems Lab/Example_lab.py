import numpy as np
import matplotlib.pyplot as plt

# Define the unit step function u(n)
# def unit(n, k):
#     """Returns the unit step function u(n-k)"""
#     return np.where(n >= k, 1, 0)

# # Define the range of n
# n = np.arange(0, 21)

# # Compute x(n)
# x = n * (unit(n, 0) - unit(n, 10)) + 10 * np.exp(-0.3 * (n - 10)) * (unit(n, 10) - unit(n, 20))

# # Plot the signal
# plt.figure(figsize=(8, 4))
# plt.stem(n, x)
# plt.xlabel("n")
# plt.ylabel("Amplitude")
# plt.title(r"$x(n) = n [u(n) − u(n − 10)] + 10e^{-0.3(n−10)} [u(n − 10) − u(n − 20)]$")
# plt.grid(True)
# plt.show()

# convualtion math for the 

x=np.array([3,11,7,0,-1,4,2])
h=np.array([2,3,0,-5,2,1])

convulation=np.convolve(x,h,mode='full')

print(convulation)
# Plot the signals
plt.figure(figsize=(10,5))

plt.subplot(3,1,1)
plt.stem(x)
plt.title("Input Signal x(n)")
plt.grid()

plt.subplot(3,1,2)
plt.stem(h)
plt.title("Impulse Response h(n)")
plt.grid()

plt.subplot(3,1,3)
plt.stem(convulation)
plt.title("Output Signal y(n) = x(n) * h(n)")
plt.grid()

plt.tight_layout()
plt.show()