"""
Q6. Three-layer ANN trained with the Back-Propagation Network (BPN) algorithm.

    Inputs      x1 = 0.05 , x2 = 0.10
    Hidden      H1, H2  (sigmoid)      bias b1 = 0.35
    Output      y1, y2  (sigmoid)      bias b2 = 0.60
    Weights     w1=0.15 w2=0.20 w3=0.25 w4=0.30   (input  -> hidden)
                w5=0.40 w6=0.45 w7=0.50 w8=0.55   (hidden -> output)
    Targets     T1 = 0.01 , T2 = 0.99
    Learning rate  eta = 0.5 ,  error  E = 1/2 * sum (t - y)^2
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x  = np.array([[0.05], [0.10]])
t  = np.array([[0.01], [0.99]])
W1 = np.array([[0.15, 0.20],        # H1 <- x1, x2
               [0.25, 0.30]])       # H2 <- x1, x2
W2 = np.array([[0.40, 0.45],        # y1 <- H1, H2
               [0.50, 0.55]])       # y2 <- H1, H2
b1, b2 = 0.35, 0.60
eta = 0.5

sig = lambda v: 1 / (1 + np.exp(-v))

def forward(W1, W2):
    net_h = W1 @ x + b1;  h = sig(net_h)
    net_y = W2 @ h + b2;  y = sig(net_y)
    E = 0.5 * float(np.sum((t - y) ** 2))
    return net_h, h, net_y, y, E

# ---------------- first forward pass (hand-check values) ----------------
net_h, h, net_y, y, E0 = forward(W1, W2)
print("=========== FORWARD PASS (iteration 1) ===========")
print(f"net_H1 = {float(net_h[0,0]):.8f}   out_H1 = {float(h[0,0]):.8f}")
print(f"net_H2 = {float(net_h[1,0]):.8f}   out_H2 = {float(h[1,0]):.8f}")
print(f"net_y1 = {float(net_y[0,0]):.8f}   out_y1 = {float(y[0,0]):.8f}")
print(f"net_y2 = {float(net_y[1,0]):.8f}   out_y2 = {float(y[1,0]):.8f}")
print(f"E1 = {0.5*(t[0,0]-y[0,0])**2:.8f}   E2 = {0.5*(t[1,0]-y[1,0])**2:.8f}   E_total = {E0:.8f}")

# ---------------- first backward pass ----------------
delta_o = -(t - y) * y * (1 - y)                 # dE/dnet at output
gradW2  = delta_o @ h.T
delta_h = (W2.T @ delta_o) * h * (1 - h)         # dE/dnet at hidden
gradW1  = delta_h @ x.T

print("\n=========== BACKWARD PASS (iteration 1) ===========")
print("delta_o1 = %.8f   delta_o2 = %.8f" % (delta_o[0,0], delta_o[1,0]))
print("delta_h1 = %.8f   delta_h2 = %.8f" % (delta_h[0,0], delta_h[1,0]))
names2 = ["w5", "w6", "w7", "w8"]; names1 = ["w1", "w2", "w3", "w4"]
newW2 = W2 - eta * gradW2
newW1 = W1 - eta * gradW1
print("\nUpdated hidden->output weights")
for n, o_, g, nw in zip(names2, W2.ravel(), gradW2.ravel(), newW2.ravel()):
    print(f"  {n}: old = {o_:.4f}  dE/d{n} = {g:+.8f}  new = {nw:.8f}")
print("Updated input->hidden weights")
for n, o_, g, nw in zip(names1, W1.ravel(), gradW1.ravel(), newW1.ravel()):
    print(f"  {n}: old = {o_:.4f}  dE/d{n} = {g:+.8f}  new = {nw:.8f}")

W1, W2 = newW1, newW2
print(f"\nE_total after 1 update = {forward(W1,W2)[4]:.8f}   (was {E0:.8f})")

# ---------------- full training ----------------
hist = [E0]
EPOCHS = 10000
for ep in range(EPOCHS):
    net_h, h, net_y, y, E = forward(W1, W2)
    delta_o = -(t - y) * y * (1 - y)
    delta_h = (W2.T @ delta_o) * h * (1 - h)
    W2 = W2 - eta * (delta_o @ h.T)
    W1 = W1 - eta * (delta_h @ x.T)
    hist.append(E)
    if (ep + 1) in (10, 100, 1000, 10000):
        print(f"iteration {ep+1:6d}   E_total = {E:.10f}   y1 = {float(y[0,0]):.6f}   y2 = {float(y[1,0]):.6f}")

*_, y, E = forward(W1, W2)
print("\n=========== AFTER TRAINING ===========")
print(f"y1 = {float(y[0,0]):.6f}  (target 0.01)")
print(f"y2 = {float(y[1,0]):.6f}  (target 0.99)")
print(f"E_total = {E:.10f}")
print("Final W1 (input->hidden) =\n", np.round(W1, 6))
print("Final W2 (hidden->output) =\n", np.round(W2, 6))

plt.figure(figsize=(6, 4))
plt.semilogy(hist, color="tab:green")
plt.xlabel("Iteration"); plt.ylabel("Total error E (log scale)")
plt.title("Q6 - Back-propagation convergence"); plt.grid(alpha=.3, which="both")
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q6_bpn.png", dpi=130)
print("\n[Figure saved: q6_bpn.png]")
