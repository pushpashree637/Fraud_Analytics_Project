import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

from sklearn.model_selection import cross_val_score

# ==========================
# Load Data
# ==========================

X_train = pd.read_csv("dataset/X_train_balanced.csv")
y_train = pd.read_csv("dataset/y_train_balanced.csv").squeeze()

X_test = pd.read_csv("dataset/X_test.csv")
y_test = pd.read_csv("dataset/y_test.csv").squeeze()

# ==========================
# Load Best Model
# ==========================

model = joblib.load("models/fraud_model.pkl")

# ==========================
# Predictions
# ==========================

y_pred = model.predict(X_test)

# Probability (needed for ROC-AUC)
y_prob = model.predict_proba(X_test)[:, 1]

# ==========================
# Evaluation Metrics
# ==========================

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc = roc_auc_score(y_test, y_prob)

print("=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"ROC-AUC  : {roc:.4f}")

# ==========================
# Classification Report
# ==========================

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# ==========================
# Confusion Matrix
# ==========================

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Normal","Fraud"],
    yticklabels=["Normal","Fraud"]
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.savefig("reports/confusion_matrix.png")

plt.show()

# ==========================
# Cross Validation
# ==========================

scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="f1"
)

print("\nCross Validation F1 Scores")
print(scores)

print(f"\nAverage F1 Score: {scores.mean():.4f}")

# ==========================
# Save Metrics
# ==========================

metrics = pd.DataFrame({
    "Metric":[
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC",
        "Cross Validation F1"
    ],
    "Value":[
        accuracy,
        precision,
        recall,
        f1,
        roc,
        scores.mean()
    ]
})

metrics.to_csv(
    "reports/model_metrics.csv",
    index=False
)

print("\nEvaluation completed successfully!")