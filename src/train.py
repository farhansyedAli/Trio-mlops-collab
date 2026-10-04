import joblib
import pandas as pd
import yaml
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC

params = yaml.safe_load(open("params.yaml"))
target = params["data"]["target"]
cfg = params["train"]
seed = params["seed"]

train = pd.read_csv("data/processed/train.csv")
X = train.drop(columns=[target])
y = train[target]

name = cfg.get("model", "random_forest")
if name == "random_forest":
    model = RandomForestClassifier(
        n_estimators=cfg["n_estimators"],
        max_depth=cfg["max_depth"],
        class_weight=cfg.get("class_weight"),
        max_features=cfg.get("max_features", "sqrt"),
        random_state=seed,
    )
elif name == "logistic_regression":
    model = make_pipeline(
        MinMaxScaler(),
        LogisticRegression(C=cfg["C"], max_iter=cfg["max_iter"], random_state=seed),
    )
elif name == "svm":
    model = make_pipeline(
        MinMaxScaler(),
        SVC(C=cfg["C"], kernel=cfg["kernel"], random_state=seed),
    )
else:
    raise ValueError(f"unknown model '{name}'")

model.fit(X, y)

Path("models").mkdir(exist_ok=True)
joblib.dump(model, "models/model.joblib")
