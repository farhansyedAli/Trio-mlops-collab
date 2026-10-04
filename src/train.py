from pathlib import Path

import joblib
import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

with open("params.yaml") as f:
    params = yaml.safe_load(f)
target = params["data"]["target"]
tp = params["train"]

train = pd.read_csv("data/processed/train.csv")
X = train.drop(columns=[target])
y = train[target]

rf = RandomForestClassifier(
    n_estimators=tp["n_estimators"],
    max_depth=tp["max_depth"],
    class_weight=tp.get("class_weight"),
    random_state=params["seed"],
)
model = make_pipeline(StandardScaler(), rf) if tp.get("scale", False) else rf
model.fit(X, y)

Path("models").mkdir(exist_ok=True)
joblib.dump(model, "models/model.joblib")
