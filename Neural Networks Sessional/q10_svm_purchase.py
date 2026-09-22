"""
Q10. Purchase Classification Prediction using SVM.

     Features : Age , EstimatedSalary        Target : Purchased (0 / 1)

     DATASET
     -------
     Social_Network_Ads.csv (400 rows: User ID, Gender, Age, EstimatedSalary,
     Purchased) - the classic Kaggle dataset for this experiment
     (kaggle.com/rakeshrau/social-network-ads). Downloaded here from a public
     GitHub mirror of the same file so it runs with REAL data, not synthetic.

     Compares LINEAR, RBF and POLYNOMIAL kernels and plots decision regions.
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# ---------------- real Kaggle data ----------------
df = pd.read_csv('Social_Network_Ads.csv')
X = df[['Age', 'EstimatedSalary']].values
y = df['Purchased'].values
N = len(df)
print(f"dataset : Social_Network_Ads.csv  ({N} customers)   purchased = {y.sum()}   not purchased = {N-y.sum()}")

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.25, random_state=0, stratify=y)
sc = StandardScaler().fit(Xtr)
Xtr_s, Xte_s = sc.transform(Xtr), sc.transform(Xte)

# ---------------- compare kernels ----------------
print("\nKernel comparison")
print(f"{'kernel':<12}{'train acc':>11}{'test acc':>11}{'#SV':>7}")
models = {}
for k, kw in [("linear", {}), ("rbf", {"gamma": "scale"}), ("poly", {"degree": 3, "gamma": "scale"})]:
    m = SVC(kernel=k, C=1.0, **kw).fit(Xtr_s, ytr)
    models[k] = m
    print(f"{k:<12}{m.score(Xtr_s,ytr)*100:>10.2f}%{m.score(Xte_s,yte)*100:>10.2f}%{len(m.support_):>7}")

# ---------------- grid search on the RBF kernel ----------------
gs = GridSearchCV(SVC(kernel="rbf"),
                  {"C": [0.1, 1, 10, 100], "gamma": [0.01, 0.1, 0.5, 1, "scale"]},
                  cv=5, n_jobs=-1).fit(Xtr_s, ytr)
print(f"\nbest parameters : {gs.best_params_}   (cv accuracy = {gs.best_score_*100:.2f} %)")
best = gs.best_estimator_
pred = best.predict(Xte_s)
print(f"test accuracy with the tuned model = {accuracy_score(yte,pred)*100:.2f} %")
cm = confusion_matrix(yte, pred)
print("\nConfusion matrix\n            pred:0  pred:1")
print(f"true:0   {cm[0,0]:>7}{cm[0,1]:>8}\ntrue:1   {cm[1,0]:>7}{cm[1,1]:>8}")
print("\n", classification_report(yte, pred, target_names=["Not purchased", "Purchased"], digits=3))

# ---------------- prediction on new customers ----------------
new = np.array([[30, 87000], [45, 26000], [52, 110000], [22, 20000]], float)
pn  = best.predict(sc.transform(new))
print("New customers")
for (a, s), q in zip(new, pn):
    print(f"  age {a:.0f}, salary {s:,.0f}  ->  {'WILL BUY' if q else 'will not buy'}")

# ---------------- decision-region plots ----------------
xx, yy = np.meshgrid(np.linspace(Xte_s[:, 0].min()-1, Xte_s[:, 0].max()+1, 300),
                     np.linspace(Xte_s[:, 1].min()-1, Xte_s[:, 1].max()+1, 300))
grid = np.c_[xx.ravel(), yy.ravel()]
fig, ax = plt.subplots(1, 3, figsize=(14, 4.4))
for i, (k, m) in enumerate(models.items()):
    Z = m.predict(grid).reshape(xx.shape)
    ax[i].contourf(xx, yy, Z, alpha=.25, cmap="coolwarm")
    ax[i].scatter(Xte_s[yte==0, 0], Xte_s[yte==0, 1], c="tab:blue", edgecolors="k", s=28, label="not purchased")
    ax[i].scatter(Xte_s[yte==1, 0], Xte_s[yte==1, 1], c="tab:red",  edgecolors="k", s=28, label="purchased")
    ax[i].set_title(f"{k} kernel  (test {m.score(Xte_s,yte)*100:.1f} %)")
    ax[i].set_xlabel("Age (standardised)"); ax[i].set_ylabel("Salary (standardised)")
ax[0].legend(fontsize=8)
plt.suptitle("Q10 - SVM purchase classification (Social_Network_Ads.csv), decision regions on the test set")
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q10_svm.png", dpi=130)
print("\n[Figure saved: q10_svm.png]")
