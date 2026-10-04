from pathlib import Path

import pandas as pd
import yaml
from sklearn.model_selection import train_test_split

with open("params.yaml") as f:
    params = yaml.safe_load(f)
target = params["data"]["target"]

df = pd.read_csv(params["data"]["train_path"])

train, holdout = train_test_split(
    df,
    test_size=params["split"]["test_size"],
    random_state=params["seed"],
    stratify=df[target],
)

Path("data/processed").mkdir(parents=True, exist_ok=True)
train.to_csv("data/processed/train.csv", index=False)
holdout.to_csv("data/processed/test.csv", index=False)
