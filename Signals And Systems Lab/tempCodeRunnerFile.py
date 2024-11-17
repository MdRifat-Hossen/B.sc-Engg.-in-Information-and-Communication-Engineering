def impseq(n0, n1, n2):
#     """
#     Generates x[n] = delta(n-n0); n1 <= n <= n2
#     Parameters:
#         n0: int, the index where the impulse occurs
#         n1: int, start index of the sequence
#         n2: int, end index of the sequence
#     Returns:
#         n: numpy array, the range of indices
#         x: numpy array, the impulse sequence
#     """
#     n = np.arange(n1, n2 + 1)  # Generate the range of indices
#     x = (n == n0) # Create the impulse sequence
#     # x=[]
#     # for i in n:
#     #     if i==0:
#     #         x.append(1)
#     #     else:
#     #         x.append(0)
#     return x, n