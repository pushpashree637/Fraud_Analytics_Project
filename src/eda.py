import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_csv("D:\Fraud_Analytics_Project\dataset\creditcard.csv.csv")


print("===== First 5 Rows =====")
print(df.head())


print("\n===== Shape =====")
print(df.shape)


print("\n===== Information =====")
print(df.info())


print("\n===== Missing Values =====")
print(df.isnull().sum())


print("\n===== Fraud Count =====")
print(df["is_fraud"].value_counts())


# Fraud percentage
fraud_percentage = df["is_fraud"].mean()*100

print("\nFraud Percentage:")
print(fraud_percentage)


# Merchant category analysis
print("\nMerchant Categories:")
print(df["merchant_category"].value_counts())


# Fraud visualization

sns.countplot(x="is_fraud", data=df)

plt.title("Fraud vs Normal Transactions")

plt.savefig("reports/fraud_distribution.png")

plt.show()