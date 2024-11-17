import numpy as np
import Unit_simple
import Unit_step
import matplotlib.pyplot as plt

def sigadd(x1, x2, n1, n2):
    """
    Implements Y[n] = x1[n] + x2[n]
    """
    # Determine the combined range of n
    n = np.arange(min(min(n1), min(n2)), max(max(n1), max(n2)) + 1)
    
    # Initialize y1 and y2 to zeros over the range of n
    y1 = np.zeros_like(n, dtype='float')
    y2 = np.zeros_like(n, dtype='float')
    
    # Map x1 and x2 values to the appropriate indices
    y1[np.isin(n, n1)] = x1
    y2[np.isin(n, n2)] = x2
    
    # Add the sequences
    y = y1 / y2
    return y, n

# Generate signals
x1, n1 = Unit_simple.impseq(0, -5, 5)  # Impulse at n=0
x2, n2 = Unit_step.unit_step(0, -5, 5)       # Step starting at n=0

# Add signals
y, n = sigadd(x1, x2, n1, n2)

# Plot the result
plt.stem(n, y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Signal Addition: Impulse / Step')
plt.grid()
plt.show()
