import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# ==========================
# Load Data
# ==========================

X_train = pd.read_csv("dataset/X_train_balanced.csv")
y_train = pd.read_csv("dataset/y_train_balanced.csv").squeeze()

print("=" * 60)
print("Hyperparameter Tuning Started")
print("=" * 60)

# ==========================
# Base Model
# ==========================

rf = RandomForestClassifier(random_state=42)

# ==========================
# Parameter Grid
# ==========================

param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [10, 20, None],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2]
}

# ==========================
# Grid Search
# ==========================

grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1,
    verbose=2
)

grid_search.fit(X_train, y_train)

# ==========================
# Best Results
# ==========================

print("\nBest Parameters:")
print(grid_search.best_params_)

print("\nBest F1 Score:")
print(grid_search.best_score_)

# ==========================
# Save Best Model
# ==========================

best_model = grid_search.best_estimator_

joblib.dump(best_model, "models/fraud_model.pkl")

print("\nOptimized model saved successfully!")