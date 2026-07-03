from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

REPORT = BASE_DIR / "reports"

DATASET = BASE_DIR / "dataset" / "creditcard.csv"


def metrics():

    return pd.read_csv(
        REPORT / "model_metrics.csv"
    )


def comparison():

    return pd.read_csv(
        REPORT / "model_comparison.csv"
    )


def transactions():

    return pd.read_csv(DATASET)


def pdf():

    return REPORT / "Fraud_Analytics_Report.pdf"