"""
Q7. Fine-tuning a PRETRAINED ResNet-50 on a custom dataset (flower classification).

    *** THIS PROGRAM NEEDS AN INTERNET CONNECTION AND A DATASET ***
    It downloads (a) the ImageNet ResNet-50 weights and (b) the images, so it is
    provided here as ready-to-run code rather than an executed script.

    DATASET
    -------
    Option A (automatic download, easiest):
        Oxford Flowers-102  ->  torchvision.datasets.Flowers102(root='data', download=True)
    Option B (your own folders):
        data/train/<class_name>/*.jpg
        data/val/<class_name>/*.jpg
        e.g.  data/train/rose , data/train/tulip , data/train/sunflower ...
        A good ready-made one is the TensorFlow "flower_photos" set (5 classes, 3 670 images):
        https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz
        Or from Kaggle: "Flowers Recognition" dataset (alxmamaev/flowers-recognition).

    INSTALL
    -------
        pip install torch torchvision            (CPU wheels are enough; a GPU is ~20x faster)

    STRATEGY (two-stage transfer learning)
    --------------------------------------
    Stage 1 : freeze the whole convolutional backbone, replace fc with a new
              Linear(2048, num_classes) and train only that head  (lr = 1e-3).
    Stage 2 : unfreeze layer4 (+ optionally layer3) and fine-tune the whole thing
              with a 10x smaller learning rate (lr = 1e-4) so the pretrained
              features are not destroyed.
"""
import torch, torch.nn as nn, torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models

DATA_DIR   = "data"          # must contain train/ and val/ sub-folders
BATCH      = 32
EPOCHS_1   = 5               # head-only
EPOCHS_2   = 5               # fine-tune
device     = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------- 1. Data: ImageNet normalisation is mandatory for pretrained nets ----------
mean, std = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]
tf_train = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(0.2, 0.2, 0.2),
    transforms.ToTensor(), transforms.Normalize(mean, std)])
tf_val = transforms.Compose([
    transforms.Resize(256), transforms.CenterCrop(224),
    transforms.ToTensor(), transforms.Normalize(mean, std)])

train_ds = datasets.ImageFolder(f"{DATA_DIR}/train", tf_train)
val_ds   = datasets.ImageFolder(f"{DATA_DIR}/val",   tf_val)
train_dl = DataLoader(train_ds, BATCH, shuffle=True,  num_workers=2)
val_dl   = DataLoader(val_ds,   BATCH, shuffle=False, num_workers=2)
classes  = train_ds.classes
print("classes :", classes)

# ---------- 2. Pretrained ResNet-50, new classification head ----------
model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)
for p in model.parameters():                 # stage 1: freeze backbone
    p.requires_grad = False
model.fc = nn.Sequential(nn.Dropout(0.3), nn.Linear(model.fc.in_features, len(classes)))
model = model.to(device)

criterion = nn.CrossEntropyLoss()

def run_epoch(dl, train_mode, opt=None):
    model.train() if train_mode else model.eval()
    tot = correct = 0; loss_sum = 0.0
    with torch.set_grad_enabled(train_mode):
        for xb, yb in dl:
            xb, yb = xb.to(device), yb.to(device)
            out = model(xb); loss = criterion(out, yb)
            if train_mode:
                opt.zero_grad(); loss.backward(); opt.step()
            loss_sum += loss.item() * len(xb)
            correct  += (out.argmax(1) == yb).sum().item(); tot += len(xb)
    return loss_sum / tot, correct / tot

# ---------- 3. Stage 1 : train the head only ----------
opt = optim.Adam(model.fc.parameters(), lr=1e-3)
for ep in range(EPOCHS_1):
    tl, ta = run_epoch(train_dl, True, opt)
    vl, va = run_epoch(val_dl, False)
    print(f"[head]  epoch {ep+1}/{EPOCHS_1}  train {tl:.4f}/{ta*100:.2f}%   val {vl:.4f}/{va*100:.2f}%")

# ---------- 4. Stage 2 : unfreeze layer4 and fine-tune ----------
for p in model.layer4.parameters():
    p.requires_grad = True
opt = optim.Adam([{"params": model.layer4.parameters(), "lr": 1e-4},
                  {"params": model.fc.parameters(),     "lr": 1e-3}])
sched = optim.lr_scheduler.CosineAnnealingLR(opt, T_max=EPOCHS_2)
best = 0.0
for ep in range(EPOCHS_2):
    tl, ta = run_epoch(train_dl, True, opt); sched.step()
    vl, va = run_epoch(val_dl, False)
    print(f"[fine]  epoch {ep+1}/{EPOCHS_2}  train {tl:.4f}/{ta*100:.2f}%   val {vl:.4f}/{va*100:.2f}%")
    if va > best:
        best = va; torch.save(model.state_dict(), "resnet50_finetuned.pth")
print(f"\nBest validation accuracy = {best*100:.2f} %  (weights saved to resnet50_finetuned.pth)")

# TYPICAL RESULT on flower_photos (5 classes, 10 epochs, CPU ~25 min / GPU ~2 min):
#   [head] epoch 5 : val accuracy ~ 88-90 %
#   [fine] epoch 5 : val accuracy ~ 94-96 %
# Training from scratch on the same small dataset only reaches ~65-70 %,
# which is exactly the benefit of transfer learning.
