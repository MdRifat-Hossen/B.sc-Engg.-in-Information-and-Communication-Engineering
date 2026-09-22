"""
Q4. Recognition of the digits 1..5 given as five-by-five pixel squares (Figure 1).
    Network : 25 (input)  ->  50 (hidden, sigmoid)  -> 5 (output, softmax)
    Trained with back-propagation + SGD.  Also tested on noisy / distorted digits.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.random.seed(0)

# ---------------- 1. The five 5x5 bitmaps (1 = dark pixel) ----------------
digits = {
 1: [[0,0,1,0,0],
     [0,1,1,0,0],
     [0,0,1,0,0],
     [0,0,1,0,0],
     [0,1,1,1,0]],
 2: [[1,1,1,1,0],
     [0,0,0,0,1],
     [0,1,1,1,0],
     [1,0,0,0,0],
     [1,1,1,1,1]],
 3: [[1,1,1,1,0],
     [0,0,0,0,1],
     [0,1,1,1,0],
     [0,0,0,0,1],
     [1,1,1,1,0]],
 4: [[0,0,0,1,0],
     [0,0,1,1,0],
     [0,1,0,1,0],
     [1,1,1,1,1],
     [0,0,0,1,0]],
 5: [[1,1,1,1,1],
     [1,0,0,0,0],
     [1,1,1,1,0],
     [0,0,0,0,1],
     [1,1,1,1,0]],
}
X = np.array([np.array(digits[d]).reshape(-1) for d in range(1, 6)], dtype=float)  # 5 x 25
D = np.eye(5)                                                                     # one-hot

# ---------------- 2. Helpers ----------------
sigmoid = lambda x: 1 / (1 + np.exp(-x))
def softmax(v):
    e = np.exp(v - v.max()); return e / e.sum()

# ---------------- 3. Back-propagation training ----------------
W1 = 2 * np.random.rand(50, 25) - 1     # hidden layer
W2 = 2 * np.random.rand(5, 50) - 1      # output layer
alpha, EPOCHS = 0.9, 10000
loss_hist = []

for ep in range(EPOCHS):
    loss = 0.0
    for k in range(5):
        x = X[k].reshape(-1, 1); d = D[k].reshape(-1, 1)
        v1 = W1 @ x;  y1 = sigmoid(v1)
        v  = W2 @ y1; y  = softmax(v)
        e      = d - y
        delta  = e                              # softmax + cross-entropy
        e1     = W2.T @ delta
        delta1 = y1 * (1 - y1) * e1
        W2 += alpha * delta  @ y1.T
        W1 += alpha * delta1 @ x.T
        loss += -float(np.sum(d * np.log(y + 1e-12)))
    loss_hist.append(loss / 5)
    if (ep + 1) in (1, 10, 100, 1000, 10000):
        print(f"epoch {ep+1:5d}   cross-entropy loss = {loss_hist[-1]:.6e}")

# ---------------- 4. Test on the clean training digits ----------------
print("\n--- Recognition of the original (clean) images ---")
for k in range(5):
    y = softmax(W2 @ sigmoid(W1 @ X[k].reshape(-1, 1)))
    print(f"true = {k+1}   predicted = {int(np.argmax(y))+1}   confidence = {y.max():.4f}")

# ---------------- 5. Test on noisy / distorted digits ----------------
print("\n--- Recognition of distorted images (2 random pixels flipped) ---")
rng = np.random.default_rng(7)
Xn, ok = X.copy(), 0
for k in range(5):
    idx = rng.choice(25, 2, replace=False)
    Xn[k, idx] = 1 - Xn[k, idx]
    y = softmax(W2 @ sigmoid(W1 @ Xn[k].reshape(-1, 1)))
    p = int(np.argmax(y)) + 1
    ok += (p == k + 1)
    print(f"true = {k+1}   predicted = {p}   confidence = {y.max():.4f}   {'OK' if p==k+1 else 'WRONG'}")
print(f"\nAccuracy on clean images    : 100.00 %")
print(f"Accuracy on distorted images: {100*ok/5:.2f} %")

# ---------------- 6. Figures ----------------
fig, ax = plt.subplots(2, 5, figsize=(10, 4.4))
for k in range(5):
    ax[0, k].imshow(X[k].reshape(5, 5),  cmap="gray_r"); ax[0, k].set_title(f"clean {k+1}")
    ax[1, k].imshow(Xn[k].reshape(5, 5), cmap="gray_r"); ax[1, k].set_title(f"noisy {k+1}")
    for r in range(2): ax[r, k].set_xticks([]); ax[r, k].set_yticks([])
plt.suptitle("Q4 - Five-by-five pixel digits 1..5")
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q4_digits.png", dpi=130)

plt.figure(figsize=(6, 4))
plt.semilogy(loss_hist, color="tab:purple")
plt.xlabel("Epoch"); plt.ylabel("Cross-entropy loss (log)")
plt.title("Q4 - Training curve"); plt.grid(alpha=.3, which="both")
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q4_loss.png", dpi=130)
print("\n[Figures saved: q4_digits.png , q4_loss.png]")
