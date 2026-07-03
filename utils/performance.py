import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

REPORT_DIR = BASE_DIR / "reports"


def load_metrics():

    return pd.read_csv(
        REPORT_DIR / "model_metrics.csv"
    )


def load_comparison():

    return pd.read_csv(
        REPORT_DIR / "model_comparison.csv"
    )


def confusion():

    return REPORT_DIR / "confusion_matrix.png"


def roc():

    return REPORT_DIR / "roc_curve.png"