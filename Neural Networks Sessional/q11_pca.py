"""
Q11. Dimensionality reduction into a new coordinate system using PCA.

     Part A : PCA written FROM SCRATCH (covariance -> eigen-decomposition) on the
              Iris dataset (4-D -> 2-D), verified against sklearn.decomposition.PCA
     Part B : PCA on the 64-D handwritten digits set, image reconstruction from a
              reduced number of components.

     DATASET : both `load_iris` and `load_digits` ship inside scikit-learn, so
               nothing has to be downloaded.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

np.set_printoptions(precision=4, suppress=True)

# ================= PART A : PCA from scratch on Iris =================
iris = load_iris()
X, y, names = iris.data, iris.target, iris.feature_names
print("Iris data :", X.shape, " features :", names)

Xs = StandardScaler().fit_transform(X)          # standardise (mean 0, var 1)

C = np.cov(Xs, rowvar=False)                    # 1. covariance matrix
print("\nCovariance matrix\n", C)

evals, evecs = np.linalg.eigh(C)                # 2. eigen-decomposition
order = np.argsort(evals)[::-1]                 # 3. sort descending
evals, evecs = evals[order], evecs[:, order]
print("\nEigenvalues :", evals)
print("Eigenvectors (columns = principal axes)\n", evecs)

ratio = evals / evals.sum()
print("\nExplained variance ratio :", np.round(ratio * 100, 2), "%")
print("Cumulative               :", np.round(np.cumsum(ratio) * 100, 2), "%")

k = 2
W = evecs[:, :k]                                # 4. projection matrix
Z = Xs @ W                                      # 5. new coordinate system
print(f"\nProjected data shape : {Z.shape}  (first 5 rows)\n", Z[:5])

# verification with sklearn (signs of eigenvectors may be flipped - that is fine)
Zsk = PCA(n_components=2).fit_transform(Xs)
print("\nMax |difference| vs sklearn (after sign alignment) :",
      np.abs(np.abs(Z) - np.abs(Zsk)).max())

# reconstruction error
Xrec = Z @ W.T
print(f"Reconstruction MSE with {k} of 4 components : {np.mean((Xs - Xrec)**2):.6f}")

fig, ax = plt.subplots(1, 3, figsize=(14, 4.3))
for t, c, n in zip(range(3), "rgb", iris.target_names):
    ax[0].scatter(Z[y == t, 0], Z[y == t, 1], c=c, label=n, edgecolors="k", s=35)
ax[0].set_xlabel("PC1 (%.1f %%)" % (ratio[0]*100)); ax[0].set_ylabel("PC2 (%.1f %%)" % (ratio[1]*100))
ax[0].set_title("Iris projected onto PC1-PC2"); ax[0].legend(); ax[0].grid(alpha=.3)

ax[1].bar(range(1, 5), ratio*100, color="tab:cyan", edgecolor="k")
ax[1].plot(range(1, 5), np.cumsum(ratio)*100, "o-r")
ax[1].set_xlabel("Principal component"); ax[1].set_ylabel("Variance explained (%)")
ax[1].set_title("Scree plot"); ax[1].grid(alpha=.3)

im = ax[2].imshow(evecs[:, :2].T, cmap="coolwarm", vmin=-1, vmax=1)
ax[2].set_xticks(range(4)); ax[2].set_xticklabels([n.replace(" (cm)", "") for n in names],
                                                  rotation=30, ha="right", fontsize=8)
ax[2].set_yticks([0, 1]); ax[2].set_yticklabels(["PC1", "PC2"])
ax[2].set_title("Loadings of each original feature")
plt.colorbar(im, ax=ax[2])
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q11_pca_iris.png", dpi=130)

# ================= PART B : PCA on 64-D digit images =================
dg = load_digits()
Xd = dg.data
print("\n\nDigits data :", Xd.shape)
p = PCA().fit(Xd)
cum = np.cumsum(p.explained_variance_ratio_)
for thr in (0.80, 0.90, 0.95, 0.99):
    print(f"components needed for {thr*100:.0f} % of the variance : {np.argmax(cum>=thr)+1} / 64")

fig, ax = plt.subplots(4, 8, figsize=(12, 6.2))
for j, ncomp in enumerate([64, 30, 15, 5]):
    pj = PCA(n_components=ncomp).fit(Xd)
    rec = pj.inverse_transform(pj.transform(Xd))
    for i in range(8):
        ax[j, i].imshow(rec[i].reshape(8, 8), cmap="gray"); ax[j, i].axis("off")
    ax[j, 0].set_ylabel(f"{ncomp}")
    ax[j, 3].set_title(f"reconstruction with {ncomp} components "
                       f"(MSE {np.mean((Xd-rec)**2):.3f})", fontsize=9)
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q11_pca_digits.png", dpi=130)
print("\n[Figures saved: q11_pca_iris.png , q11_pca_digits.png]")
