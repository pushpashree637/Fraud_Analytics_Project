import pandas as pd

# Load original dataset
df = pd.read_csv("D:\Fraud_Analytics_Project\dataset\creditcard.csv.csv")

print("=" * 50)
print("Class Distribution")
print("=" * 50)

print(df["is_fraud"].value_counts())

print("\nPercentage:")

print(df["is_fraud"].value_counts(normalize=True) * 100)