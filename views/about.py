import streamlit as st


def show_about():

    st.title("ℹ About AI Fraud Analytics Platform")

    st.markdown("""
---
## 🎯 Project Objective

The AI Fraud Analytics Platform is designed to detect fraudulent financial
transactions using Machine Learning techniques.

The system provides:

- Fraud Detection
- Business Intelligence Analytics
- Executive Dashboard
- Model Performance Evaluation
- Automated Reports
- Power BI Integration

---
""")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📂 Dataset")

        st.write("""
- Dataset Name : Credit Card Transactions

- Records : 10,000

- Fraud Cases : 151

- Features : 9

- Target : is_fraud
""")

    with col2:

        st.subheader("🤖 Machine Learning")

        st.write("""
Algorithm

• Random Forest Classifier

Evaluation

• Accuracy

• Precision

• Recall

• F1 Score

• ROC-AUC

• Cross Validation
""")

    st.markdown("---")

    st.subheader("🛠 Technologies Used")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:

        st.success("""
Python

Pandas

NumPy

Matplotlib
""")

    with tech2:

        st.success("""
Scikit-Learn

Joblib

SHAP

Plotly
""")

    with tech3:

        st.success("""
Streamlit

Power BI

ReportLab

GitHub
""")

    st.markdown("---")

    st.subheader("✨ Key Features")

    st.write("""
✔ Executive Dashboard

✔ Fraud Prediction

✔ Interactive Analytics

✔ Model Evaluation

✔ Cross Validation

✔ ROC Curve

✔ Confusion Matrix

✔ Automated PDF Reports

✔ Power BI Dashboard

✔ Business Intelligence
""")

    st.markdown("---")

    st.subheader("🚀 Future Enhancements")

    st.info("""
• Deep Learning Model

• Live Banking API

• SMS / Email Alerts

• Real-Time Fraud Monitoring

• Cloud Deployment

• Multi-User Authentication
""")

    st.markdown("---")

    st.caption(
        "AI Fraud Analytics Platform | Final Year Data Science Project | Version 1.0"
    )