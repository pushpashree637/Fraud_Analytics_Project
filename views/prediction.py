import streamlit as st

from utils.predictor import predict_transaction
from utils.predictor import ENCODER


def show_prediction():

    st.title("🤖 AI Fraud Detection")

    st.markdown(
        "Analyze a financial transaction and estimate its fraud risk."
    )

    left, right = st.columns([2, 1])

    with left:

        amount = st.number_input(
            "Transaction Amount",
            value=250.0
        )

        merchant = st.selectbox(
            "Merchant Category",
            ENCODER.classes_
        )

        hour = st.slider(
            "Transaction Hour",
            0,
            23,
            12
        )

        foreign = st.selectbox(
            "Foreign Transaction",
            [0, 1]
        )

        mismatch = st.selectbox(
            "Location Mismatch",
            [0, 1]
        )

        trust = st.slider(
            "Device Trust Score",
            0,
            100,
            75
        )

        velocity = st.slider(
            "Transactions in Last 24 Hours",
            0,
            20,
            2
        )

        age = st.slider(
            "Cardholder Age",
            18,
            80,
            35
        )

        predict = st.button(
            "🚀 Analyze Transaction",
            use_container_width=True
        )

    with right:

        st.info("""
### 💡 Risk Guide

🟢 0–30% → Low Risk

🟡 31–70% → Medium Risk

🔴 71–100% → High Risk
""")

    if predict:

        prediction, probability = predict_transaction(
            amount,
            hour,
            merchant,
            foreign,
            mismatch,
            trust,
            velocity,
            age
        )

        st.divider()

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Fraud Probability",
            f"{probability*100:.2f}%"
        )

        if probability < 0.30:
            risk = "🟢 LOW"

        elif probability < 0.70:
            risk = "🟡 MEDIUM"

        else:
            risk = "🔴 HIGH"

        c2.metric(
            "Risk Level",
            risk
        )

        c3.metric(
            "Prediction",
            "Fraud" if prediction else "Normal"
        )

        st.progress(float(probability))

        st.subheader("🧠 AI Recommendation")

        if probability > 0.70:

            st.error("""
**Recommended Action**

• Block transaction

• Send OTP verification

• Notify customer immediately

• Escalate to fraud investigation team
""")

        elif probability > 0.30:

            st.warning("""
**Recommended Action**

• Additional verification

• Monitor account

• Request identity confirmation
""")

        else:

            st.success("""
**Recommended Action**

• Approve transaction

• Continue monitoring
""")