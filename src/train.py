import pandas as pd
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# ==========================
# Load Data
# ==========================

X_train = pd.read_csv("dataset/X_train_balanced.csv")
y_train = pd.read_csv("dataset/y_train_balanced.csv").squeeze()

X_test = pd.read_csv("dataset/X_test.csv")
y_test = pd.read_csv("dataset/y_test.csv").squeeze()

# ==========================
# Models
# ==========================

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(
        random_state=42,
        eval_metric="logloss"
    )
}

results = []

best_model = None
best_f1 = 0

# ==========================
# Train Models
# ==========================

for name, model in models.items():

    print("=" * 60)
    print(name)
    print("=" * 60)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    results.append([
        name,
        accuracy,
        precision,
        recall,
        f1
    ])

    if f1 > best_f1:
        best_f1 = f1
        best_model = model

# ==========================
# Save Best Model
# ==========================

joblib.dump(best_model, "models/fraud_model.pkl")

print("\nBest model saved successfully!")

# ==========================
# Save Results
# ==========================

results_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
)

results_df.to_csv(
    "reports/model_comparison.csv",
    index=False
)

print("\nModel comparison saved.")
print(results_df)