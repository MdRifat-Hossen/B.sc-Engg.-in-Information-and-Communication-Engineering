"""
Q3. Performance comparison of SGD and BATCH training with the delta learning rule.
    Same data as Q2. Both networks start from the SAME initial weights so that the
    comparison is fair.
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
sigmoid = lambda x: 1 / (1 + np.exp(-x))

def delta_sgd(W, X, D, alpha=0.9):
    for k in range(X.shape[0]):
        x = X[k].reshape(-1, 1); d = D[k]
        y = sigmoid(W @ x)
        delta = y * (1 - y) * (d - y)
        W = W + alpha * delta * x.T
    return W

def delta_batch(W, X, D, alpha=0.9):
    dWsum = np.zeros_like(W)
    for k in range(X.shape[0]):
        x = X[k].reshape(-1, 1); d = D[k]
        y = sigmoid(W @ x)
        delta = y * (1 - y) * (d - y)
        dWsum += alpha * delta * x.T          # accumulate
    return W + dWsum / X.shape[0]             # single update per epoch (average)

W0 = 2 * np.random.rand(1, 3) - 1
W1, W2 = W0.copy(), W0.copy()

E_sgd, E_batch = [], []
EPOCHS = 1000
for _ in range(EPOCHS):
    W1 = delta_sgd(W1,   X, D)
    W2 = delta_batch(W2, X, D)
    E_sgd.append(float(np.mean((D - sigmoid(X @ W1.T)) ** 2)))
    E_batch.append(float(np.mean((D - sigmoid(X @ W2.T)) ** 2)))

print("Initial weights        :", np.round(W0, 4))
print("Weights after SGD      :", np.round(W1, 4))
print("Weights after Batch    :", np.round(W2, 4))
print(f"\nMSE after {EPOCHS} epochs :  SGD = {E_sgd[-1]:.6e}   Batch = {E_batch[-1]:.6e}")
print(f"SGD is about {E_batch[-1]/E_sgd[-1]:.1f} times lower in error at the same epoch count.")

for tol in (1e-2, 1e-3):
    s = next((i for i, e in enumerate(E_sgd)   if e < tol), None)
    b = next((i for i, e in enumerate(E_batch) if e < tol), None)
    print(f"Epochs needed to reach MSE < {tol:g} :  SGD = {s}   Batch = {b}")

print("\nFinal outputs")
print(" pattern | target |    SGD     |   Batch")
ys, yb = sigmoid(X @ W1.T), sigmoid(X @ W2.T)
for k in range(4):
    print(f"  {X[k,0]:.0f} {X[k,1]:.0f}    |   {D[k,0]:.0f}    | {ys[k,0]:.6f} | {yb[k,0]:.6f}")

plt.figure(figsize=(6.5, 4.4))
plt.semilogy(E_sgd,   label="SGD (update per pattern)",  color="tab:blue")
plt.semilogy(E_batch, label="Batch (one update/epoch)", color="tab:red")
plt.xlabel("Epoch"); plt.ylabel("Mean Squared Error (log scale)")
plt.title("Q3 - SGD vs Batch training, delta rule")
plt.legend(); plt.grid(alpha=.3, which="both")
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q3_sgd_vs_batch.png", dpi=130)
print("\n[Figure saved: q3_sgd_vs_batch.png]")
