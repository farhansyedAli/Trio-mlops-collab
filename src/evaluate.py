import json
import subprocess

import joblib
import pandas as pd
import yaml
from sklearn.metrics import accuracy_score, f1_score

with open("params.yaml") as f:
    params = yaml.safe_load(f)
target = params["data"]["target"]

test = pd.read_csv("data/processed/test.csv")
X = test.drop(columns=[target])
y = test[target]

model = joblib.load("models/model.joblib")
pred = model.predict(X)

sha = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()

metrics = {
    "accuracy": accuracy_score(y, pred),
    "f1_macro": f1_score(y, pred, average="macro"),
    "commit_sha": sha,
}
with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)
