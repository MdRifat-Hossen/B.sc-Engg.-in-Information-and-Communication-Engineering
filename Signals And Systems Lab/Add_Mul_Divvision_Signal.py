import numpy as np
import Unit_simple
import Unit_step
import matplotlib.pyplot as plt

def sigadd(x1, x2, n1, n2):
    """
    Implements Y[n] = x1[n] + x2[n]
    """
    n = np.arange(min(min(n1), min(n2)), max(max(n1), max(n2)) + 1)
    
    y1 = np.zeros_like(n, dtype='float')
    y2 = np.zeros_like(n, dtype='float')

    y1[np.isin(n, n1)] = x1
    y2[np.isin(n, n2)] = x2
    
    y = y1 + y2
    return y, n

def sigmul(x1, x2, n1, n2):
    """
    Implements Y[n] = x1[n] * x2[n] (Multiplication)
    """
    n = np.arange(min(min(n1), min(n2)), max(max(n1), max(n2)) + 1)
    
    y1 = np.zeros_like(n, dtype='float')
    y2 = np.zeros_like(n, dtype='float')

    y1[np.isin(n, n1)] = x1
    y2[np.isin(n, n2)] = x2
    
    y = y1 * y2  # Element-wise multiplication
    return y, n

def sigdiv(x1, x2, n1, n2):
    """
    Implements Y[n] = x1[n] / x2[n] (Division), with zero division handling
    """
    n = np.arange(min(min(n1), min(n2)), max(max(n1), max(n2)) + 1)
    
    y1 = np.zeros_like(n, dtype='float')
    y2 = np.zeros_like(n, dtype='float')

    y1[np.isin(n, n1)] = x1
    y2[np.isin(n, n2)] = x2
    
    # Avoid division by zero by setting it to zero where x2 is zero
    y = np.divide(y1, y2, where=(y2 != 0))  # Safe division

    return y, n

# Generate signals
x1, n1 = Unit_simple.impseq(0, -5, 5)  # Impulse at n=0
x2, n2 = Unit_step.unit_step(0, -5, 5)       # Step starting at n=0

# Add, multiply, and divide signals
y_add, n_add = sigadd(x1, x2, n1, n2)
y_mul, n_mul = sigmul(x1, x2, n1, n2)
y_div, n_div = sigdiv(x1, x2, n1, n2)

# Plot the results
# plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(n_add, y_add)
plt.title('Signal Addition: Impulse + Step')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(n_mul, y_mul)
plt.title('Signal Multiplication: Impulse * Step')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(n_div, y_div)
plt.title('Signal Division: Impulse / Step')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid()

plt.tight_layout()
plt.show()
