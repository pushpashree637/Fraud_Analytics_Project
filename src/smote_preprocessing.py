import pandas as pd
from imblearn.over_sampling import SMOTE

# ==========================
# Load Processed Data
# ==========================

X_train = pd.read_csv("dataset/X_train.csv")
y_train = pd.read_csv("dataset/y_train.csv")

# Convert y_train to Series
y_train = y_train.squeeze()

print("=" * 50)
print("Before SMOTE")
print("=" * 50)
print(y_train.value_counts())

# ==========================
# Apply SMOTE
# ==========================

smote = SMOTE(random_state=42)

X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

print("\n" + "=" * 50)
print("After SMOTE")
print("=" * 50)
print(y_train_balanced.value_counts())

# ==========================
# Save Balanced Dataset
# ==========================

pd.DataFrame(X_train_balanced).to_csv(
    "dataset/X_train_balanced.csv",
    index=False
)

pd.DataFrame(y_train_balanced).to_csv(
    "dataset/y_train_balanced.csv",
    index=False
)

print("\nBalanced dataset saved successfully!")