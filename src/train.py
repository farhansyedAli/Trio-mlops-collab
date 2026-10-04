import yaml
import joblib
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier

params = yaml.safe_load(open("params.yaml"))
target = params["data"]["target"]

train = pd.read_csv("data/processed/train.csv")
X = train.drop(columns=[target])
y = train[target]

model = RandomForestClassifier(
    n_estimators=params["train"]["n_estimators"],
    max_depth=params["train"]["max_depth"],
    random_state=params["seed"],
)
model.fit(X, y)

Path("models").mkdir(exist_ok=True)
joblib.dump(model, "models/model.joblib")