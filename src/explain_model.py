import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt

# Load model
model = joblib.load("models/fraud_model.pkl")

# Load training data
X_train = pd.read_csv("dataset/X_train_balanced.csv")

# Create SHAP Explainer
explainer = shap.TreeExplainer(model)

# Take only 200 samples
X_sample = X_train.sample(200, random_state=42)

# Calculate SHAP values
shap_values = explainer.shap_values(X_sample)

# Summary Plot
shap.summary_plot(
    shap_values,
    X_sample,
    show=False
)
plt.savefig("reports/shap_summary.png", dpi=300)
plt.show()

print("SHAP summary plot saved successfully!")