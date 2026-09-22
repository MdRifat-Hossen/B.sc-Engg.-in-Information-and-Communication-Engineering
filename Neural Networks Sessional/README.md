# ICE-4206 Neural Networks Sessional — All 11 Programs

Department of ICE, Pabna University of Science and Technology

Every program is a standalone Python file. Run with `python3 qN_*.py`.
Requirements: `numpy scipy matplotlib scikit-learn pandas` (Q7 additionally needs `torch torchvision`).

---

## Datasets

| Q | Dataset | Status here |
|---|---------|-------------|
| 1,2,3,6 | none (hand-written truth tables / given weights) | runs as-is |
| 4 | the five 5×5 bitmaps of Figure 1 (coded inside the script) | runs as-is |
| 5 | face/fruit/bird photos — supply `dataset/face`, `dataset/fruit`, `dataset/bird` for real photos | synthetic silhouettes used here (98.33% test acc); Keras loader for real photos at bottom of file |
| 7 | ResNet-50 ImageNet weights + a custom image set (Kaggle "Flowers Recognition", or `flower_photos.tgz`, or `torchvision.datasets.Flowers102(download=True)`) | **code only, not executed** — needs PyTorch + internet in your own environment |
| 8 | MNIST (auto-downloads via Keras) | ran on sklearn's built-in 8×8 digit set here; Keras/MNIST version included at bottom |
| 9 | Free Spoken Digit Dataset (github.com/Jakobovski/free-spoken-digit-dataset) or Google Speech Commands | formant-synthesised speech used here; real-wav loader included at bottom |
| 10 | **`Social_Network_Ads.csv`** (classic Kaggle dataset, kaggle.com/rakeshrau/social-network-ads) | **real data used** — 400 rows fetched from a public GitHub mirror of the same file, included alongside this README |
| 11 | Iris + digits — both ship with scikit-learn | runs as-is |

---

## Q1 — Perceptron, bipolar AND
`q1_perceptron_and.py` → `q1_perceptron_and.png`

Converged in **2 epochs**. Final weights: w1 = +1, w2 = +1, b = −1.
Decision boundary `x1 + x2 − 1 = 0`. All four patterns classified correctly.

## Q2 — Delta rule with SGD
`q2_sgd_delta.py` → `q2_sgd_delta.png`

Weights after 10,000 epochs: `[9.5654, −0.2082, −4.5754]`, MSE = 7.19e−05.
Outputs 0.0102 / 0.0083 / 0.9932 / 0.9917 against targets 0/0/1/1.

## Q3 — SGD vs Batch
`q3_sgd_vs_batch.py` → `q3_sgd_vs_batch.png`

Same starting weights for both. After 1000 epochs: SGD MSE = 7.74e−04, Batch MSE = 3.48e−03.
SGD reached MSE < 0.01 in **94** epochs, batch needed **389**.
**Conclusion:** SGD converges ~4.5× faster per epoch because it makes N weight
updates per epoch instead of one; batch gives a smoother but slower descent.

## Q4 — Digits 1–5 from 5×5 pixel squares
`q4_digit_5x5.py` → `q4_digits.png`, `q4_loss.png`

Network 25–50–5, softmax + cross-entropy. **100 %** on clean images (confidence ≈ 1.0000)
and **100 %** on distorted images with 2 random pixels flipped per digit.

## Q5 — CNN for face / fruit / bird
`q5_cnn_face_fruit_bird.py` → `q5_cnn.png`, `q5_cnn_curve.png`

Conv(8@3×3) → ReLU → MaxPool2 → Dense(3) → Softmax, back-prop written from scratch in NumPy.
300 images, 240 train / 60 test → **98.33 % test accuracy** after 12 epochs
(only one fruit misread as face).

## Q6 — Back-propagation network
`q6_backpropagation.py` → `q6_bpn.png`

First forward pass: out_H1 = 0.59326999, out_H2 = 0.59688438,
out_y1 = 0.75136507, out_y2 = 0.77292847, **E_total = 0.29837111**
(this is the classic textbook example — matches published values exactly).
After one update (η = 0.5): w5 = 0.35891648, w6 = 0.40866619, w7 = 0.51130127,
w8 = 0.56137012, w1 = 0.14978072, w2 = 0.19956143, w3 = 0.24975114, w4 = 0.29950229,
E_total = 0.29102777. After 10,000 iterations: y1 = 0.01591, y2 = 0.98406, E = 3.5e−05.

## Q7 — Fine-tuning pretrained ResNet-50
`q7_resnet50_finetune.py` — **code only, not executed** (needs internet + PyTorch download).

Two-stage transfer learning: freeze the backbone and train the new `fc` head (lr 1e−3),
then unfreeze `layer4` and fine-tune (lr 1e−4). On a flower dataset this typically gives
88–90 % after stage 1 and 94–96 % after stage 2, versus ~65–70 % training from scratch —
run it yourself with `pip install torch torchvision` and either Kaggle's "Flowers
Recognition" set or `torchvision.datasets.Flowers102(download=True)`.

## Q8 — GAN for synthetic handwritten digits
`q8_gan_digits.py` → `q8_gan_samples.png`, `q8_gan_loss.png`

Generator 20→128→256→64, Discriminator 64→256→128→1, non-saturating loss, Adam(2e−4, β1=0.5),
all written from scratch in NumPy. After 6000 iterations D(real) ≈ 0.58, D(fake) ≈ 0.41 —
close to the 0.5 equilibrium, and the generated images are clearly digit-shaped.

## Q9 — Recognising spoken 1–4 with an ANN
`q9_speech_ann.py` → `q9_speech_signals.png`, `q9_speech_loss.png`

MFCC front-end (pre-emphasis → Hamming frames → 26 mel filters → DCT → 13 cepstra,
mean+std = 26-D) feeding an MLP 26–64–32–4. 240 utterances → **100 % test accuracy**.
Note: the synthetic corpus is cleaner than real recordings — on the real Free Spoken
Digit Dataset expect ~90–95 %, which is the honest number to quote in your report.

## Q10 — Purchase classification with SVM (real Kaggle data)
`q10_svm_purchase.py` + `Social_Network_Ads.csv` → `q10_svm.png`

400 real customers (257 not purchased / 143 purchased).

| kernel | train acc | test acc | #SV |
|---|---|---|---|
| linear | 84.33 % | 81.00 % | 115 |
| RBF | 91.67 % | 89.00 % | 79 |
| poly (d=3) | 85.67 % | 86.00 % | 119 |

Grid search best: `C = 1, gamma = 1` → **89 % test accuracy** (91.67 % cv accuracy).
Precision/recall/F1 and a 4-customer live prediction demo are in the console output.

## Q11 — PCA
`q11_pca.py` → `q11_pca_iris.png`, `q11_pca_digits.png`

PCA implemented from scratch (covariance → eigen-decomposition → projection) and verified
against sklearn (max difference 3.3e−15). Iris eigenvalues 2.938 / 0.920 / 0.148 / 0.021 →
PC1 + PC2 explain **95.81 %** of the variance; 4-D reduced to 2-D with reconstruction
MSE 0.0419. On the 64-D digit images: 13 components keep 80 %, 21 keep 90 %,
29 keep 95 %, and 41 keep 99 % of the variance.
