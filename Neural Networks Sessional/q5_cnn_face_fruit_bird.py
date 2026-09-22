"""
Q5. Convolutional Neural Network (CNN) to classify FACE / FRUIT / BIRD.

    Architecture :  input 32x32x1
                    -> Conv 8 filters 3x3  -> ReLU -> MaxPool 2x2
                    -> Flatten (8*15*15)   -> Dense 3 -> Softmax
    Implemented from scratch with NumPy (im2col convolution + back-propagation).

    DATASET NOTE
    ------------
    This offline machine has no internet access, so the script builds a small
    SYNTHETIC face/fruit/bird silhouette dataset (300 images) so that the whole
    pipeline runs end-to-end.  To use REAL photographs, put your images in

        dataset/face/*.jpg   dataset/fruit/*.jpg   dataset/bird/*.jpg

    and replace make_dataset() with the loader given at the bottom of this file.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)
H = W = 32

# ------------------------------------------------------------------ dataset
def draw_face(img):
    cy, cx, r = 16 + rng.integers(-2, 3), 16 + rng.integers(-2, 3), 10 + rng.integers(-1, 2)
    y, x = np.ogrid[:H, :W]
    img[(y - cy) ** 2 + (x - cx) ** 2 <= r * r] = 1.0            # round head
    img[cy - 4:cy - 2, cx - 5:cx - 3] = 0.0                      # eyes
    img[cy - 4:cy - 2, cx + 3:cx + 5] = 0.0
    img[cy + 4:cy + 5, cx - 4:cx + 4] = 0.0                      # mouth
    return img

def draw_fruit(img):                                             # apple-like blob + stem
    cy, cx = 18 + rng.integers(-2, 3), 16 + rng.integers(-2, 3)
    ry, rx = 9 + rng.integers(-1, 2), 11 + rng.integers(-1, 2)
    y, x = np.ogrid[:H, :W]
    img[((y - cy) / ry) ** 2 + ((x - cx) / rx) ** 2 <= 1] = 1.0
    img[max(cy - ry - 4, 0):cy - ry + 1, cx:cx + 2] = 1.0        # stem
    return img

def draw_bird(img):                                              # two wings + body (V shape)
    cy, cx = 14 + rng.integers(-2, 3), 16 + rng.integers(-2, 3)
    for t in range(11):
        img[np.clip(cy - t // 2, 0, H - 1), np.clip(cx - t, 0, W - 1)] = 1.0
        img[np.clip(cy - t // 2, 0, H - 1), np.clip(cx + t, 0, W - 1)] = 1.0
        img[np.clip(cy - t // 2 + 1, 0, H - 1), np.clip(cx - t, 0, W - 1)] = 1.0
        img[np.clip(cy - t // 2 + 1, 0, H - 1), np.clip(cx + t, 0, W - 1)] = 1.0
    img[cy:cy + 6, cx - 1:cx + 2] = 1.0                          # body
    return img

def make_dataset(n_per_class=100):
    Xs, ys = [], []
    for lbl, fn in enumerate((draw_face, draw_fruit, draw_bird)):
        for _ in range(n_per_class):
            im = fn(np.zeros((H, W)))
            im += 0.12 * rng.standard_normal((H, W))             # sensor noise
            Xs.append(np.clip(im, 0, 1)); ys.append(lbl)
    Xs = np.array(Xs)[:, None, :, :]                             # N,1,32,32
    return Xs, np.array(ys)

X, y = make_dataset()
idx = rng.permutation(len(X)); X, y = X[idx], y[idx]
ntr = int(.8 * len(X))
Xtr, ytr, Xte, yte = X[:ntr], y[:ntr], X[ntr:], y[ntr:]
classes = ["face", "fruit", "bird"]
print(f"dataset : {len(X)} images  ->  train {len(Xtr)} / test {len(Xte)}   classes = {classes}")

# ------------------------------------------------------------------ layers
def im2col(x, k):                       # x: N,1,H,W  -> N, k*k, out*out
    N, C, Hh, Ww = x.shape
    o = Hh - k + 1
    cols = np.empty((N, C * k * k, o * o))
    c = 0
    for i in range(k):
        for j in range(k):
            cols[:, c, :] = x[:, 0, i:i + o, j:j + o].reshape(N, -1); c += 1
    return cols, o

F, K = 8, 3                                     # 8 filters of size 3x3
Wc = rng.standard_normal((F, K * K)) * np.sqrt(2 / (K * K))
bc = np.zeros((F, 1))
POUT = (H - K + 1) // 2                         # 15
Wf = rng.standard_normal((3, F * POUT * POUT)) * np.sqrt(2 / (F * POUT * POUT))
bf = np.zeros((3, 1))

def forward(xb):
    cols, o = im2col(xb, K)                     # N, 9, o*o
    conv = np.einsum('fk,nkp->nfp', Wc, cols) + bc[None]         # N,F,o*o
    relu = np.maximum(conv, 0)
    r = relu.reshape(-1, F, o, o)
    pool = r.reshape(-1, F, o // 2, 2, o // 2, 2).max(axis=(3, 5))   # N,F,15,15
    flat = pool.reshape(len(xb), -1)
    logits = flat @ Wf.T + bf.T
    e = np.exp(logits - logits.max(1, keepdims=True))
    prob = e / e.sum(1, keepdims=True)
    return cols, o, conv, r, pool, flat, prob

def train(epochs=12, lr=0.02, bs=16):
    global Wc, bc, Wf, bf
    hist = []
    for ep in range(epochs):
        p = rng.permutation(len(Xtr))
        tot = 0.0
        for s in range(0, len(Xtr), bs):
            b = p[s:s + bs]; xb, yb = Xtr[b], ytr[b]
            cols, o, conv, r, pool, flat, prob = forward(xb)
            n = len(xb)
            onehot = np.zeros_like(prob); onehot[np.arange(n), yb] = 1
            tot += -np.sum(np.log(prob[np.arange(n), yb] + 1e-12))
            dlog = (prob - onehot) / n
            dWf, dbf = dlog.T @ flat, dlog.sum(0)[:, None]
            dflat = dlog @ Wf
            dpool = dflat.reshape(n, F, POUT, POUT)
            # max-pool backward
            rs = r.reshape(n, F, POUT, 2, POUT, 2)
            mx = rs.max(axis=(3, 5), keepdims=True)
            mask = (rs == mx)
            dr = (mask * dpool[:, :, :, None, :, None]).reshape(n, F, o, o)
            dconv = dr.reshape(n, F, o * o) * (conv > 0)
            dWc = np.einsum('nfp,nkp->fk', dconv, cols)
            dbc = dconv.sum(axis=(0, 2))[:, None]
            Wf -= lr * dWf; bf -= lr * dbf; Wc -= lr * dWc; bc -= lr * dbc
        acc = (forward(Xte)[-1].argmax(1) == yte).mean()
        hist.append((tot / len(Xtr), acc))
        print(f"epoch {ep+1:2d}   train loss = {tot/len(Xtr):.4f}   test accuracy = {acc*100:5.2f} %")
    return hist

hist = train()
prob = forward(Xte)[-1]; pred = prob.argmax(1)
print(f"\nFinal test accuracy : {(pred==yte).mean()*100:.2f} %")
cm = np.zeros((3, 3), int)
for t, p_ in zip(yte, pred): cm[t, p_] += 1
print("\nConfusion matrix (rows = true, cols = predicted)")
print("            " + "".join(f"{c:>8}" for c in classes))
for i, c in enumerate(classes):
    print(f"{c:>10}  " + "".join(f"{v:>8}" for v in cm[i]))

fig, ax = plt.subplots(2, 6, figsize=(12, 4.5))
for i in range(6):
    ax[0, i].imshow(Xte[i, 0], cmap="gray"); ax[0, i].axis("off")
    ax[0, i].set_title(f"{classes[yte[i]]}\npred:{classes[pred[i]]}", fontsize=9)
for f in range(6):
    ax[1, f].imshow(Wc[f].reshape(3, 3), cmap="viridis"); ax[1, f].axis("off")
    ax[1, f].set_title(f"filter {f+1}", fontsize=9)
plt.suptitle("Q5 - CNN test samples (top) and learned 3x3 filters (bottom)")
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q5_cnn.png", dpi=130)

plt.figure(figsize=(6, 4))
plt.plot([h[0] for h in hist], "o-", label="train loss")
plt.plot([h[1] for h in hist], "s-", label="test accuracy")
plt.xlabel("Epoch"); plt.grid(alpha=.3); plt.legend(); plt.title("Q5 - CNN learning curve")
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q5_cnn_curve.png", dpi=130)
print("\n[Figures saved: q5_cnn.png , q5_cnn_curve.png]")

# ----------------------------------------------------------------------
# REAL-DATA VERSION (needs tensorflow / keras and a folder 'dataset/'):
#
# from tensorflow.keras import layers, models
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# gen = ImageDataGenerator(rescale=1/255., validation_split=0.2)
# tr = gen.flow_from_directory('dataset', target_size=(64,64), batch_size=32,
#                              class_mode='categorical', subset='training')
# va = gen.flow_from_directory('dataset', target_size=(64,64), batch_size=32,
#                              class_mode='categorical', subset='validation')
# m = models.Sequential([
#     layers.Conv2D(32,3,activation='relu',input_shape=(64,64,3)), layers.MaxPooling2D(),
#     layers.Conv2D(64,3,activation='relu'), layers.MaxPooling2D(),
#     layers.Conv2D(64,3,activation='relu'), layers.MaxPooling2D(),
#     layers.Flatten(), layers.Dense(128,activation='relu'), layers.Dropout(0.4),
#     layers.Dense(3,activation='softmax')])
# m.compile('adam','categorical_crossentropy',metrics=['accuracy'])
# m.fit(tr, validation_data=va, epochs=20)
