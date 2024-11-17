import numpy as np
import matplotlib.pyplot as plt

def unit_step(n0, n1, n2):
    """
    Generates x[n] = delta(n-n0); n1 <= n <= n2
    Parameters:
        n0: int, the index where the impulse occurs
        n1: int, start index of the sequence
        n2: int, end index of the sequence
    Returns:
        n: numpy array, the range of indices
        x: numpy array, the impulse sequence
    """
    n = np.arange(n1, n2 + 1)  # Generate the range of indices
    # x = []# Create the impulse sequence?\
    x=(n-n0>=0).astype(int)
    # you can use for loop
    # for i in n:
    #     if i-n0>=0:
    #         x.append(1)
    #     else:
    #         x.append(0)
    return x, n

# Example usage
x, n = unit_step(0, -3, 4)

# Plot the impulse sequence
plt.stem(n, x)  # Discrete plot
plt.title('Impulse Sequence')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()
