import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    RocCurveDisplay
)

from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)

# ===============================
# Create Reports Folder
# ===============================

os.makedirs("reports", exist_ok=True)

# ===============================
# Load Dataset
# ===============================

df = pd.read_csv("dataset/creditcard.csv")

# Remove Transaction ID
X = df.drop(columns=["transaction_id", "is_fraud"])

y = df["is_fraud"]

# Encode Merchant Category
encoder = joblib.load("models/label_encoder.pkl")
X["merchant_category"] = encoder.transform(X["merchant_category"])

# Scale Features
scaler = joblib.load("models/scaler.pkl")
X = scaler.transform(X)

# ===============================
# Train Test Split
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ===============================
# Load Model
# ===============================

model = joblib.load("models/fraud_model.pkl")

# ===============================
# Predictions
# ===============================

y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)[:, 1]

# ===============================
# Metrics
# ===============================

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

roc = roc_auc_score(y_test, y_prob)

cv = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy"
).mean()

metrics = pd.DataFrame({

    "Metric":[
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC",
        "Cross Validation"
    ],

    "Value":[
        accuracy,
        precision,
        recall,
        f1,
        roc,
        cv
    ]

})

metrics.to_csv(
    "reports/model_metrics.csv",
    index=False
)

# ===============================
# Model Comparison
# ===============================

comparison = pd.DataFrame({

    "Model":["Random Forest"],

    "Accuracy":[accuracy],

    "Precision":[precision],

    "Recall":[recall],

    "F1":[f1],

    "ROC":[roc]

})

comparison.to_csv(
    "reports/model_comparison.csv",
    index=False
)

# ===============================
# Confusion Matrix
# ===============================

cm = confusion_matrix(
    y_test,
    y_pred
)

disp = ConfusionMatrixDisplay(cm)

disp.plot()

plt.savefig(
    "reports/confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ===============================
# ROC Curve
# ===============================

RocCurveDisplay.from_predictions(
    y_test,
    y_prob
)

plt.savefig(
    "reports/roc_curve.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("=" * 50)
print("Performance reports generated successfully!")
print("=" * 50)