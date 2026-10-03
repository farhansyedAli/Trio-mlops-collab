"""Create the digits dataset as a CSV in data/."""

from pathlib import Path

from sklearn.datasets import load_digits


def main() -> None:
    out = Path("data")
    out.mkdir(exist_ok=True)
    df = load_digits(as_frame=True).frame
    df.to_csv(out / "digits.csv", index=False)
    print(f"Wrote {len(df)} rows to {out / 'digits.csv'}")


if __name__ == "__main__":
    main()
