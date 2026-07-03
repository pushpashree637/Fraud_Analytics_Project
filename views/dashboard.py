import streamlit as st

from utils.loader import load_data
from utils.charts import (
    fraud_distribution,
    merchant_chart,
    hourly_chart
)


def show_dashboard():

    df = load_data()

    total = len(df)
    fraud = int(df["is_fraud"].sum())
    normal = total - fraud
    fraud_rate = (fraud / total) * 100
    avg_amount = df["amount"].mean()

    st.title("🏦 Executive Dashboard")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Transactions", f"{total:,}")
    c2.metric("Frauds", fraud)
    c3.metric("Normal", normal)
    c4.metric("Fraud Rate", f"{fraud_rate:.2f}%")
    c5.metric("Avg Amount", f"₹{avg_amount:.2f}")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            fraud_distribution(df),
            use_container_width=True
        )

    with right:
        st.plotly_chart(
            merchant_chart(df),
            use_container_width=True
        )

    st.plotly_chart(
        hourly_chart(df),
        use_container_width=True
    )

    st.subheader("🚨 Recent Fraud Transactions")

    fraud_df = (
        df[df["is_fraud"] == 1]
        .sort_values("transaction_id", ascending=False)
        .head(10)
    )

    st.dataframe(
        fraud_df,
        use_container_width=True
    )