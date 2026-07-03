import streamlit as st

def show_landing():

    st.markdown("""
    <div style='text-align:center;padding-top:30px;'>

    <h1 style='font-size:48px;color:#2563EB;'>
    💳 AI Fraud Analytics Platform
    </h1>

    <h4 style='color:gray;'>
    Detect • Analyze • Prevent Financial Fraud using Artificial Intelligence
    </h4>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    c1,c2,c3=st.columns(3)

    c1.metric("Transactions","10,000+")

    c2.metric("Model Accuracy","98.72%")

    c3.metric("Fraud Cases","151")

    st.write("")
    st.write("")

    st.success("""
Welcome to the AI Fraud Analytics Platform.

This application helps financial institutions detect fraudulent
transactions using Machine Learning and Data Analytics.

✔ Executive Dashboard

✔ Business Intelligence

✔ Fraud Prediction

✔ Model Performance

✔ Executive Reports
""")

    st.info("""
### Technologies Used

• Python

• Streamlit

• Scikit-Learn

• Pandas

• Plotly

• Power BI

• Matplotlib
""")

    st.write("")

    st.markdown("---")

    st.caption("Version 1.0 | Final Year Data Science Project")