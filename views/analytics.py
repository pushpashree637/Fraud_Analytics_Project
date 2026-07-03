import streamlit as st
from utils.loader import load_data
from utils.charts import (
    fraud_hour_chart,
    merchant_risk_chart,
    amount_distribution_chart
)


def show_analytics():

    st.title("📊 Business Intelligence Analytics")

    df = load_data()

    st.markdown("### 🔍 Filters")

    col1, col2, col3 = st.columns(3)

    with col1:
        merchant = st.multiselect(
            "Merchant Category",
            sorted(df["merchant_category"].unique()),
            default=sorted(df["merchant_category"].unique())
        )

    with col2:
        fraud_status = st.selectbox(
            "Fraud Status",
            ["All", "Fraud", "Normal"]
        )

    with col3:
        amount_range = st.slider(
            "Transaction Amount",
            float(df["amount"].min()),
            float(df["amount"].max()),
            (
                float(df["amount"].min()),
                float(df["amount"].max())
            )
        )

    filtered = df[df["merchant_category"].isin(merchant)]

    filtered = filtered[
        (filtered["amount"] >= amount_range[0]) &
        (filtered["amount"] <= amount_range[1])
    ]

    if fraud_status == "Fraud":
        filtered = filtered[filtered["is_fraud"] == 1]

    elif fraud_status == "Normal":
        filtered = filtered[filtered["is_fraud"] == 0]

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Transactions", len(filtered))
    c2.metric("Frauds", int(filtered["is_fraud"].sum()))
    c3.metric("Average Amount", f"₹{filtered['amount'].mean():.2f}")
    c4.metric("Maximum Amount", f"₹{filtered['amount'].max():.2f}")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            fraud_hour_chart(filtered),
            use_container_width=True
        )

    with right:
        st.plotly_chart(
            merchant_risk_chart(filtered),
            use_container_width=True
        )

    st.plotly_chart(
        amount_distribution_chart(filtered),
        use_container_width=True
    )

    st.subheader("📋 Filtered Transactions")

    st.dataframe(
        filtered,
        use_container_width=True,
        height=400
    )

    st.subheader("🧠 Business Insights")

    fraud_rate = filtered["is_fraud"].mean() * 100

    top = (
        filtered[filtered["is_fraud"] == 1]
        ["merchant_category"]
        .value_counts()
    )

    if len(top) > 0:
        st.info(
            f"Highest fraud activity is observed in **{top.index[0]}** merchants."
        )

    if fraud_rate > 5:
        st.error(
            f"Fraud rate is HIGH ({fraud_rate:.2f}%). Immediate monitoring is recommended."
        )

    else:
        st.success(
            f"Fraud rate is LOW ({fraud_rate:.2f}%)."
        )