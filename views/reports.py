import streamlit as st

from utils.reports import *

def show_reports():

    st.title("📄 Executive Report Center")

    metric = metrics()

    compare = comparison()

    data = transactions()

    st.subheader("⬇ Download Reports")

    col1,col2,col3 = st.columns(3)

    with col1:

        with open(pdf(),"rb") as file:

            st.download_button(

                "📄 PDF Report",

                file,

                "Fraud_Analytics_Report.pdf",

                use_container_width=True

            )

    with col2:

        st.download_button(

            "📊 Metrics CSV",

            metric.to_csv(index=False),

            "model_metrics.csv",

            use_container_width=True

        )

    with col3:

        st.download_button(

            "📈 Comparison CSV",

            compare.to_csv(index=False),

            "model_comparison.csv",

            use_container_width=True

        )

    st.divider()

    st.header("🧠 Executive AI Insights")

    fraud_rate = data["is_fraud"].mean()*100

    avg_amount = data["amount"].mean()

    fraud = data[data["is_fraud"]==1]

    merchant = fraud["merchant_category"].value_counts().idxmax()

    hour = fraud["transaction_hour"].mode()[0]

    foreign = fraud["foreign_transaction"].mean()*100

    st.success(

        f"Overall Fraud Rate : {fraud_rate:.2f}%"

    )

    st.info(

        f"Highest Risk Merchant : {merchant}"

    )

    st.warning(

        f"Peak Fraud Hour : {hour}:00"

    )

    st.success(

        f"Average Transaction Amount : ₹{avg_amount:.2f}"

    )

    st.error(

        f"{foreign:.1f}% of fraudulent transactions are foreign."

    )

    st.divider()

    st.subheader("🚨 Recent Fraud Transactions")

    st.dataframe(

        fraud.tail(20),

        use_container_width=True

    )

    st.divider()

    st.subheader("📈 Model Metrics")

    st.dataframe(

        metric,

        use_container_width=True

    )

    st.subheader("🏆 Model Comparison")

    st.dataframe(

        compare,

        use_container_width=True

    )