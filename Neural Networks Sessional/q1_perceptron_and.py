"""
Q1. Perceptron net for the AND function with BIPOLAR inputs and targets.
    Shows the convergence curve and the decision boundary line.
    ICE-4206 Neural Networks Sessional
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------- 1. Bipolar AND truth table ----------------
X = np.array([[ 1,  1],
              [ 1, -1],
              [-1,  1],
              [-1, -1]], dtype=float)
T = np.array([1, -1, -1, -1], dtype=float)      # bipolar targets

# ---------------- 2. Perceptron parameters ------------------
alpha  = 1.0        # learning rate
theta  = 0.0        # threshold of the bipolar step activation
w      = np.zeros(2)
b      = 0.0
MAX_EPOCH = 20

def activate(y_in, theta=0.0):
    """Bipolar step activation function."""
    if y_in >  theta: return  1.0
    if y_in < -theta: return -1.0
    return 0.0

# ---------------- 3. Training (perceptron learning rule) ----
errors_per_epoch, weight_hist = [], []
for epoch in range(1, MAX_EPOCH + 1):
    n_err = 0
    for xi, ti in zip(X, T):
        y_in = b + np.dot(w, xi)
        y    = activate(y_in, theta)
        if y != ti:                      # update only on misclassification
            w = w + alpha * ti * xi
            b = b + alpha * ti
            n_err += 1
    errors_per_epoch.append(n_err)
    weight_hist.append((w.copy(), b))
    print(f"Epoch {epoch:2d} : w1={w[0]:+.2f}  w2={w[1]:+.2f}  b={b:+.2f}  misclassified={n_err}")
    if n_err == 0:
        print(f"\n>> Converged after {epoch} epochs (no weight change).")
        break

print("\nFinal weights : w1 = %+.2f , w2 = %+.2f , bias = %+.2f" % (w[0], w[1], b))
print("Decision boundary : %.2f*x1 + %.2f*x2 + %.2f = 0" % (w[0], w[1], b))

# ---------------- 4. Testing --------------------------------
print("\n x1   x2   y_in    y_out  target")
for xi, ti in zip(X, T):
    y_in = b + np.dot(w, xi)
    print(f"{xi[0]:+.0f}   {xi[1]:+.0f}   {y_in:+.2f}   {activate(y_in):+.0f}     {ti:+.0f}")

# ---------------- 5. Plots ----------------------------------
fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))

ax[0].plot(range(1, len(errors_per_epoch) + 1), errors_per_epoch, "o-", color="crimson")
ax[0].set_xlabel("Epoch"); ax[0].set_ylabel("No. of misclassified patterns")
ax[0].set_title("Convergence curve (Perceptron, bipolar AND)")
ax[0].grid(alpha=.3); ax[0].set_xticks(range(1, len(errors_per_epoch) + 1))

for xi, ti in zip(X, T):
    ax[1].scatter(xi[0], xi[1], s=170,
                  marker="o" if ti > 0 else "s",
                  c="tab:green" if ti > 0 else "tab:red",
                  edgecolors="k", zorder=3)
xs = np.linspace(-2, 2, 100)
for k, (ww, bb) in enumerate(weight_hist):          # boundary after every epoch
    if abs(ww[1]) > 1e-9:
        ax[1].plot(xs, -(ww[0] * xs + bb) / ww[1],
                   lw=2.5 if k == len(weight_hist) - 1 else 1,
                   ls="-" if k == len(weight_hist) - 1 else "--",
                   alpha=1 if k == len(weight_hist) - 1 else .45,
                   label=f"epoch {k+1}")
ax[1].set_xlim(-2, 2); ax[1].set_ylim(-2, 2)
ax[1].set_xlabel("x1"); ax[1].set_ylabel("x2")
ax[1].set_title("Decision boundary  (o = +1 , square = -1)")
ax[1].legend(fontsize=8); ax[1].grid(alpha=.3)

plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q1_perceptron_and.png", dpi=130)
print("\n[Figure saved: q1_perceptron_and.png]")
