import pandas as pd

LABEL_COL = "label"
N_PIXELS = 784


def check_digits_frame(
    df: pd.DataFrame, label_col: str = LABEL_COL, n_pixels: int = N_PIXELS
) -> pd.DataFrame:
    """Validate a digits dataframe (label + pixel columns) and return it unchanged.

    Raises ValueError if the label column is missing, the pixel column count is
    wrong, any value is null, or a pixel is outside 0-255.
    """
    if label_col not in df.columns:
        raise ValueError(f"missing label column '{label_col}'")
    pixels = df.drop(columns=label_col)
    if pixels.shape[1] != n_pixels:
        raise ValueError(f"expected {n_pixels} pixel columns, got {pixels.shape[1]}")
    if df.isnull().any().any():
        raise ValueError("dataframe contains null values")
    if pixels.min().min() < 0 or pixels.max().max() > 255:
        raise ValueError("pixel values must be between 0 and 255")
    return df
