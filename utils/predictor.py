import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL = joblib.load(BASE_DIR / "models" / "fraud_model.pkl")
SCALER = joblib.load(BASE_DIR / "models" / "scaler.pkl")
ENCODER = joblib.load(BASE_DIR / "models" / "label_encoder.pkl")


def predict_transaction(
    amount,
    hour,
    merchant,
    foreign,
    mismatch,
    trust,
    velocity,
    age
):

    merchant = ENCODER.transform([merchant])[0]

    df = pd.DataFrame([{
        "amount": amount,
        "transaction_hour": hour,
        "merchant_category": merchant,
        "foreign_transaction": foreign,
        "location_mismatch": mismatch,
        "device_trust_score": trust,
        "velocity_last_24h": velocity,
        "cardholder_age": age
    }])

    scaled = SCALER.transform(df)

    prediction = MODEL.predict(scaled)[0]

    probability = MODEL.predict_proba(scaled)[0][1]

    return prediction, probability