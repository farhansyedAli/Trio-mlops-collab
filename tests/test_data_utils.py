import numpy as np
import pandas as pd
import pytest

from src.data_utils import check_digits_frame


def make_frame(n_rows=5, n_pixels=784):
    rng = np.random.default_rng(0)
    df = pd.DataFrame(
        rng.integers(0, 256, size=(n_rows, n_pixels)),
        columns=[f"pixel{i}" for i in range(n_pixels)],
    )
    df.insert(0, "label", rng.integers(0, 10, size=n_rows))
    return df


def test_valid_frame_passes():
    df = make_frame()
    assert check_digits_frame(df) is df


def test_missing_label_raises():
    with pytest.raises(ValueError, match="label"):
        check_digits_frame(make_frame().drop(columns="label"))


def test_wrong_pixel_count_raises():
    with pytest.raises(ValueError, match="pixel columns"):
        check_digits_frame(make_frame(n_pixels=100))


def test_out_of_range_pixel_raises():
    df = make_frame()
    df.iloc[0, 1] = 300
    with pytest.raises(ValueError, match="0 and 255"):
        check_digits_frame(df)


def test_null_raises():
    df = make_frame().astype(float)
    df.iloc[0, 1] = np.nan
    with pytest.raises(ValueError, match="null"):
        check_digits_frame(df)
