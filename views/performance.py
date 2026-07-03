import streamlit as st

from utils.performance import *

def show_performance():

    st.title("📈 AI Model Performance Center")

    metrics = load_metrics()

    comparison = load_comparison()

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric(
        "Accuracy",
        f"{metrics.iloc[0,1]*100:.2f}%"
    )

    c2.metric(
        "Precision",
        f"{metrics.iloc[1,1]*100:.2f}%"
    )

    c3.metric(
        "Recall",
        f"{metrics.iloc[2,1]*100:.2f}%"
    )

    c4.metric(
        "F1 Score",
        f"{metrics.iloc[3,1]*100:.2f}%"
    )

    c5.metric(
        "ROC AUC",
        f"{metrics.iloc[4,1]*100:.2f}%"
    )

    st.divider()

    st.success("🏆 Best Performing Model : Random Forest")

    left,right = st.columns(2)

    with left:

        st.subheader("Confusion Matrix")

        st.image(
            confusion(),
            use_container_width=True
        )

    with right:

        st.subheader("ROC Curve")

        st.image(
            roc(),
            use_container_width=True
        )

    st.divider()

    st.subheader("📊 Model Comparison")

    st.dataframe(
        comparison,
        use_container_width=True,
        height=300
    )

    st.divider()

    st.subheader("🧪 Cross Validation")

    cv = metrics[
        metrics["Metric"]=="Cross Validation"
    ]["Value"].values[0]

    st.metric(
        "Average CV Score",
        f"{cv*100:.2f}%"
    )

    st.progress(float(cv))