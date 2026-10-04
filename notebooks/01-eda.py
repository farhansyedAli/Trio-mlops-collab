# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
# ---

# %% [markdown]
# # 01 - EDA: handwritten digits (train.csv)
# Kaggle Digit Recognizer format: 28x28 grayscale images flattened into
# 784 pixel columns, plus a `label` column (the digit 0-9).

# %%
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Find the repo root so the notebook works from any folder (no hardcoded paths).
ROOT = next(
    p for p in [Path.cwd(), *Path.cwd().parents] if (p / "pyproject.toml").exists()
)
sys.path.insert(0, str(ROOT))

from src.data_utils import check_digits_frame  # noqa: E402

# %% [markdown]
# ## Load and validate

# %%
df = pd.read_csv(ROOT / "data" / "raw" / "train.csv")
df = check_digits_frame(df)  # raises if the file is malformed
print(df.shape)
df.head()

# %% [markdown]
# ## Class balance

# %%
counts = df["label"].value_counts().sort_index()
ax = counts.plot.bar(figsize=(7, 3), rot=0)
ax.set_xlabel("digit")
ax.set_ylabel("images")
plt.show()
print((counts / len(df)).round(3))

# %% [markdown]
# ## Missing values and duplicates

# %%
print("missing values:", int(df.isnull().sum().sum()))
print("duplicate rows:", int(df.duplicated().sum()))

# %% [markdown]
# ## Pixel statistics

# %%
pixels = df.drop(columns="label")
print("min / max pixel:", pixels.min().min(), pixels.max().max())
print("share of zero pixels:", round(float((pixels == 0).mean().mean()), 3))

plt.imshow(pixels.mean().to_numpy().reshape(28, 28), cmap="gray_r")
plt.title("mean pixel value across all images")
plt.colorbar()
plt.show()

# %% [markdown]
# ## Sample images

# %%
images = pixels.to_numpy().reshape(-1, 28, 28)
labels = df["label"].to_numpy()
fig, axes = plt.subplots(4, 10, figsize=(12, 5))
for i, ax in enumerate(axes.ravel()):
    ax.imshow(images[i], cmap="gray_r")
    ax.set_title(str(labels[i]), fontsize=9)
    ax.axis("off")
plt.show()

# %% [markdown]
# ## Average image per digit

# %%
fig, axes = plt.subplots(2, 5, figsize=(10, 4))
for digit, ax in enumerate(axes.ravel()):
    mean_img = pixels[df["label"] == digit].mean().to_numpy().reshape(28, 28)
    ax.imshow(mean_img, cmap="gray_r")
    ax.set_title(str(digit))
    ax.axis("off")
plt.show()

# %% [markdown]
# ## Findings
# (Write 3 short bullets after running: class balance, duplicates/missing,
# anything odd in the images.)
