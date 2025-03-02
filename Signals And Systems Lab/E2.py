# # import numpy as np
# # import matplotlib.pyplot as plt

# # def shift(x,n,k):
# #     # index
# #     n_new=n+k
# #     n_new=np.roll(x,k)
# #     return n_new


# # n=np.arange(-2,11)
# # x=np.concatenate([np.arange(1,7),np.arange(6,1,-1)])
# # # শিফট করা সংকেত বের করা
# # x_n5 = shift(x, n, 5)  # x(n-5)
# # x_p4 = shift(x, n, -4) # x(n+4)

# # # সূত্র অনুযায়ী হিসাব করা
# # X1 = 2 * x_n5 - 3 * x_p4

# # # প্লট করা
# # plt.stem(n, X1)
# # plt.title("x1(n) = 2x(n-5) - 3x(n+4)")
# # plt.xlabel("n")
# # plt.ylabel("x1(n)")
# # plt.grid(True)
# # plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# def shift(x,n, k):
#     """
#     Shifts the sequence x by k positions using np.roll.
#     """
#     return np.roll(x,n+ k)

# # Define the index range
# n = np.arange(-2, 11)

# # Define the original signal x(n)
# x = np.concatenate([np.arange(1, 7), np.arange(6, 1, -1)])

# # Shifted signals
# x_n5 = shift(x,n, 5)   # x(n-5)
# x_p4 = shift(x, n,-4)  # x(n+4)

# # Compute the new signal using the given formula
# X1 = 2 * x_n5 - 3 * x_p4

# # Plot the result
# plt.stem(n, X1)
# plt.title("x1(n) = 2x(n-5) - 3x(n+4)")
# plt.xlabel("n")
# plt.ylabel("x1(n)")
# plt.grid(True)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

def shift(x, k):
    """
    Shifts the sequence x by k positions with zero padding.
    """
    x_shifted = np.zeros_like(x)  # Initialize with zeros
    if k > 0:
        x_shifted[k:] = x[:-k]  # Shift right and pad left with zeros
    elif k < 0:
        x_shifted[:k] = x[-k:]  # Shift left and pad right with zeros
    else:
        x_shifted = x  # No shift
    return x_shifted

# Define the index range
n = np.arange(-2, 11)  # 13 elements

# Define the original signal x(n)
x = np.concatenate([np.arange(1,7), np.arange(6,1,-1)])  # Also 13 elements now

# Shifted signals
x_n5 = shift(x, 5)   # x(n-5)
x_p4 = shift(x, -4)  # x(n+4)

# Compute the new signal using the given formula
X1 = 2 * x_n5 - 3 * x_p4

# Plot the result
plt.stem(n, X1)
plt.title("x1(n) = 2x(n-5) - 3x(n+4)")
plt.xlabel("n")
plt.ylabel("x1(n)")
plt.grid(True)
plt.show()
