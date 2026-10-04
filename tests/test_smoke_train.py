import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def test_smoke_train(tmp_path):
    """Train on 300 fake rows to prove src/train.py runs end to end."""
    rng = np.random.default_rng(0)
    df = pd.DataFrame(
        rng.integers(0, 256, size=(300, 20)),
        columns=[f"pixel{i}" for i in range(20)],
    )
    df["label"] = rng.integers(0, 10, size=300)

    (tmp_path / "data" / "processed").mkdir(parents=True)
    df.to_csv(tmp_path / "data" / "processed" / "train.csv", index=False)
    shutil.copy(ROOT / "params.yaml", tmp_path / "params.yaml")

    subprocess.run(
        [sys.executable, str(ROOT / "src" / "train.py")],
        cwd=tmp_path,
        check=True,
    )
    assert (tmp_path / "models" / "model.joblib").exists()
