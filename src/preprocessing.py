import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


# ===========================
# Load Dataset
# ===========================

df = pd.read_csv("D:\Fraud_Analytics_Project\dataset\creditcard.csv.csv")

print("=" * 50)
print("Dataset Loaded Successfully")
print("=" * 50)


# ===========================
# Remove Duplicate Rows
# ===========================

duplicates = df.duplicated().sum()
print(f"Duplicate Rows: {duplicates}")

df.drop_duplicates(inplace=True)


# ===========================
# Drop Unnecessary Columns
# ===========================

if "transaction_id" in df.columns:
    df.drop("transaction_id", axis=1, inplace=True)

print("\nColumns after dropping transaction_id:")
print(df.columns)


# ===========================
# Encode Categorical Column
# ===========================

encoder = LabelEncoder()

df["merchant_category"] = encoder.fit_transform(df["merchant_category"])

print("\nMerchant Category Encoded Successfully")


# ===========================
# Separate Features and Target
# ===========================

X = df.drop("is_fraud", axis=1)

y = df["is_fraud"]


print("\nFeature Shape:", X.shape)
print("Target Shape :", y.shape)


# ===========================
# Train Test Split
# ===========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTrain Shape :", X_train.shape)
print("Test Shape  :", X_test.shape)


# ===========================
# Feature Scaling
# ===========================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

print("\nFeature Scaling Completed")

# ==========================
# Save Preprocessing Objects
# ==========================

joblib.dump(encoder, "models/label_encoder.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("\nLabel Encoder saved successfully!")
print("Scaler saved successfully!")
# ===========================
# Save Processed Data
# ===========================

feature_names = X.columns

X_train = pd.DataFrame(X_train, columns=feature_names)
X_test = pd.DataFrame(X_test, columns=feature_names)

X_train.to_csv("dataset/X_train.csv", index=False)
X_test.to_csv("dataset/X_test.csv", index=False)
pd.DataFrame(y_train).to_csv("dataset/y_train.csv", index=False)

pd.DataFrame(y_test).to_csv("dataset/y_test.csv", index=False)


print("\nProcessed datasets saved successfully!")

print("\nPreprocessing Completed Successfully.")