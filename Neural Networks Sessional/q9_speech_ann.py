"""
Q9. Recognition of the spoken numbers 1..4 from a speech signal using an ANN.

    Pipeline :  waveform -> pre-emphasis -> framing + Hamming window -> FFT power
                -> Mel filter-bank (26 filters) -> log -> DCT -> 13 MFCC
                -> mean+std over frames (26-D feature vector)
                -> MLP (26 -> 64 -> 32 -> 4)   [scikit-learn MLPClassifier]

    DATASET NOTE
    ------------
    A real corpus is required for real speech. Recommended free ones:
      * Free Spoken Digit Dataset (FSDD) - https://github.com/Jakobovski/free-spoken-digit-dataset
        (3 000 wav files, 6 speakers, digits 0-9, 8 kHz)  -> keep only 1,2,3,4
      * Google Speech Commands v2 (also on Kaggle) - has the words "one".."four"
    This session builds the utterances with a simple source-filter (formant)
    model instead: each word is built from its phoneme sequence, every phoneme
    has its own formant frequencies, and speaker/pitch/duration/noise are
    randomised so the classes are not trivially separable.
    To switch to real audio just replace build_dataset() with the wav loader
    given at the bottom of this file - everything else stays the same.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.fftpack import dct
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

rng = np.random.default_rng(42)
FS = 8000

# ---------------- 1. Formant table (F1,F2,F3 in Hz) and word definitions -------
PH = {                       # phoneme : (F1, F2, F3, voiced?)
    "w":  (300,  610, 2200, True),
    "ah": (700, 1220, 2600, True),
    "n":  (250, 1700, 2400, True),
    "t":  (400, 1700, 2500, False),   # burst / unvoiced
    "uw": (300,  870, 2240, True),
    "th": (400, 1400, 2600, False),
    "r":  (350, 1100, 1600, True),
    "iy": (270, 2290, 3010, True),
    "f":  (400, 1200, 2400, False),
    "ao": (570,  840, 2410, True),
}
WORDS = {1: ["w", "ah", "n"],
         2: ["t", "uw"],
         3: ["th", "r", "iy"],
         4: ["f", "ao", "r"]}

def synth_phoneme(ph, dur, f0):
    n  = int(dur * FS); t = np.arange(n) / FS
    F1, F2, F3, voiced = PH[ph]
    if voiced:                                    # glottal pulse train excitation
        src = np.zeros(n)
        src[::max(int(FS / f0), 1)] = 1.0
    else:                                         # noise excitation
        src = rng.standard_normal(n) * 0.5
    y = np.zeros(n)
    for F, amp in zip((F1, F2, F3), (1.0, 0.6, 0.3)):   # 3 resonators
        bw = 90.0
        r  = np.exp(-np.pi * bw / FS); th = 2 * np.pi * F / FS
        a1, a2 = -2 * r * np.cos(th), r * r
        out = np.zeros(n)
        for i in range(n):
            out[i] = src[i] - a1 * (out[i-1] if i > 0 else 0) - a2 * (out[i-2] if i > 1 else 0)
        y += amp * out
    env = np.minimum(1, np.minimum(t, dur - t) * 40)     # fade in/out
    return y * env / (np.max(np.abs(y)) + 1e-9)

def synth_word(label):
    f0 = rng.uniform(90, 220)                      # speaker pitch
    sig = np.concatenate([synth_phoneme(p, rng.uniform(.10, .18), f0)
                          for p in WORDS[label]])
    sig += 0.02 * rng.standard_normal(len(sig))    # recording noise
    return sig / (np.max(np.abs(sig)) + 1e-9)

# ---------------- 2. MFCC front-end ----------------
def mel(f):    return 2595 * np.log10(1 + f / 700)
def imel(m):   return 700 * (10 ** (m / 2595) - 1)

def mel_filterbank(nfilt=26, nfft=512):
    pts = imel(np.linspace(mel(0), mel(FS / 2), nfilt + 2))
    bins = np.floor((nfft + 1) * pts / FS).astype(int)
    fb = np.zeros((nfilt, nfft // 2 + 1))
    for m in range(1, nfilt + 1):
        l, c, r = bins[m - 1], bins[m], bins[m + 1]
        for k in range(l, c): fb[m-1, k] = (k - l) / max(c - l, 1)
        for k in range(c, r): fb[m-1, k] = (r - k) / max(r - c, 1)
    return fb
FB = mel_filterbank()

def mfcc_features(sig, ncep=13, flen=0.025, fstep=0.010, nfft=512):
    sig = np.append(sig[0], sig[1:] - 0.97 * sig[:-1])          # pre-emphasis
    L, S = int(flen * FS), int(fstep * FS)
    nfr = 1 + max(0, (len(sig) - L) // S)
    frames = np.stack([sig[i*S:i*S+L] for i in range(nfr)]) * np.hamming(L)
    pw   = np.abs(np.fft.rfft(frames, nfft)) ** 2 / nfft
    ener = np.log(pw @ FB.T + 1e-10)
    c    = dct(ener, type=2, axis=1, norm="ortho")[:, :ncep]
    return np.hstack([c.mean(0), c.std(0)])                     # 26-D vector

# ---------------- 3. Build the dataset ----------------
def build_dataset(n_per_class=60):
    X, y, raw = [], [], {}
    for lbl in (1, 2, 3, 4):
        for i in range(n_per_class):
            s = synth_word(lbl)
            if i == 0: raw[lbl] = s
            X.append(mfcc_features(s)); y.append(lbl)
    return np.array(X), np.array(y), raw

print("Synthesising utterances and extracting MFCCs ...")
X, y, raw = build_dataset()
print(f"feature matrix : {X.shape}   labels : {np.bincount(y)[1:]} samples for 1,2,3,4")

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.25, stratify=y, random_state=0)
sc = StandardScaler().fit(Xtr)
Xtr, Xte = sc.transform(Xtr), sc.transform(Xte)

# ---------------- 4. ANN ----------------
clf = MLPClassifier(hidden_layer_sizes=(64, 32), activation="relu", solver="adam",
                    alpha=1e-3, max_iter=800, random_state=1)
clf.fit(Xtr, ytr)
print(f"\ntraining accuracy = {clf.score(Xtr,ytr)*100:.2f} %")
print(f"test  accuracy    = {clf.score(Xte,yte)*100:.2f} %")
pred = clf.predict(Xte)
print("\nConfusion matrix (rows = true 1..4, cols = predicted)\n", confusion_matrix(yte, pred))
print("\n", classification_report(yte, pred, digits=3))

# ---------------- 5. Plots ----------------
fig, ax = plt.subplots(2, 4, figsize=(13, 5))
for i, lbl in enumerate((1, 2, 3, 4)):
    ax[0, i].plot(np.arange(len(raw[lbl])) / FS, raw[lbl], lw=.5)
    ax[0, i].set_title(f'waveform "{["one","two","three","four"][i]}"'); ax[0, i].set_xlabel("s")
    ax[1, i].specgram(raw[lbl], NFFT=256, Fs=FS, noverlap=192, cmap="magma")
    ax[1, i].set_title("spectrogram"); ax[1, i].set_ylabel("Hz")
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q9_speech_signals.png", dpi=130)

plt.figure(figsize=(6, 4))
plt.plot(clf.loss_curve_, color="tab:orange")
plt.xlabel("Iteration"); plt.ylabel("Loss"); plt.grid(alpha=.3)
plt.title("Q9 - ANN training curve (speech digits 1-4)")
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/q9_speech_loss.png", dpi=130)
print("\n[Figures saved: q9_speech_signals.png , q9_speech_loss.png]")

# ----------------------------------------------------------------------
# REAL-AUDIO LOADER (Free Spoken Digit Dataset, files named  <digit>_<speaker>_<n>.wav)
#
# import glob, scipy.io.wavfile as wav
# X, y = [], []
# for f in glob.glob('recordings/*.wav'):
#     d = int(f.split('/')[-1].split('_')[0])
#     if d not in (1,2,3,4): continue
#     fs, s = wav.read(f); s = s.astype(float); s /= np.max(np.abs(s))
#     X.append(mfcc_features(s)); y.append(d)
# X, y = np.array(X), np.array(y)
