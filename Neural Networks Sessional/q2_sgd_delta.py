"""
Q2. Delta (Widrow-Hoff) learning rule trained with STOCHASTIC GRADIENT DESCENT (SGD)
    X = [0 0 1 ; 0 1 1 ; 1 0 1 ; 1 1 1]      (3rd column = bias input)
    D = [0 ; 0 ; 1 ; 1]
    Single-layer network,  sigmoid activation.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.random.seed(3)

X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]], dtype=float)
D = np.array([[0], [0], [1], [1]], dtype=float)

sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))

def delta_sgd(W, X, D, alpha=0.9):
    """One epoch of the delta rule, weights updated after EVERY pattern."""
    for k in range(X.shape[0]):
        x = X[k, :].reshape(-1, 1)          # 3 x 1
        d = D[k]
        v = W @ x                           # weighted sum
        y = sigmoid(v)
        e     = d - y                       # error
        delta = y * (1 - y) * e             # sigmoid derivative * error
        dW    = alpha * delta * x.T         # 1 x 3
        W     = W + dW
    return W

W = 2 * np.random.rand(1, 3) - 1
print("Initial weights :", np.round(W, 4))

EPOCHS = 10000
mse_hist = []
for epoch in range(EPOCHS):
    W = delta_sgd(W, X, D, alpha=0.9)
    y = sigmoid(X @ W.T)
    mse_hist.append(float(np.mean((D - y) ** 2)))
    if (epoch + 1) in (1, 10, 100, 1000, 5000, 10000):
        print(f"epoch {epoch+1:5d}  MSE = {mse_hist[-1]:.6e}")

print("\nTrained weights :", np.round(W, 4))
print("\n x1 x2 bias | target | output    | rounded")
y = sigmoid(X @ W.T)
for k in range(4):
    print(f" {X[k,0]:.0f}  {X[k,1]:.0f}   {X[k,2]:.0f}  |   {D[k,0]:.0f}    | {y[k,0]:.6f} |   {round(y[k,0]):.0f}")

plt.figure(figsize=(6, 4.2))
plt.semilogy(mse_hist, color="tab:blue")
plt.xlabel("Epoch"); plt.ylabel("Mean Squared Error (log)")
plt.title("Q2 - Delta rule with SGD : learning curve")
plt.grid(alpha=.3, which="both")
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q2_sgd_delta.png", dpi=130)
print("\n[Figure saved: q2_sgd_delta.png]")
