import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATASET_PATH = BASE_DIR / "dataset" / "creditcard.csv.csv"

# Load dataset
df = pd.read_csv(DATASET_PATH)


def show_analytics():

    st.header("📊 Fraud Analytics")

    # -------------------------
    # Fraud vs Normal
    # -------------------------

    st.subheader("Fraud vs Normal Transactions")

    fig, ax = plt.subplots(figsize=(6,4))

    df["is_fraud"].value_counts().plot(
        kind="bar",
        ax=ax
    )

    ax.set_xticklabels(["Normal", "Fraud"])

    ax.set_ylabel("Count")

    st.pyplot(fig)

    # -------------------------
    # Merchant Category
    # -------------------------

    st.subheader("Merchant Category Distribution")

    fig, ax = plt.subplots(figsize=(8,4))

    df["merchant_category"].value_counts().plot(
        kind="bar",
        ax=ax
    )

    ax.set_ylabel("Transactions")

    st.pyplot(fig)

    # -------------------------
    # Transaction Amount
    # -------------------------

    st.subheader("Transaction Amount Distribution")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.hist(df["amount"], bins=30)

    ax.set_xlabel("Amount")

    ax.set_ylabel("Frequency")

    st.pyplot(fig)

    # -------------------------
    # Transaction Hour
    # -------------------------

    st.subheader("Transaction Hour Distribution")

    fig, ax = plt.subplots(figsize=(8,4))

    df["transaction_hour"].value_counts().sort_index().plot(
        kind="line",
        marker="o",
        ax=ax
    )

    ax.set_xlabel("Hour")

    ax.set_ylabel("Transactions")

    st.pyplot(fig)