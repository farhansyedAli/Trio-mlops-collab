import json
import subprocess
import yaml
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

params = yaml.safe_load(open("params.yaml"))
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
json.dump(metrics, open("metrics.json", "w"), indent=2)