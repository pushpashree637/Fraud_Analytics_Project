import streamlit as st
from views.about import show_about
from views.landing import show_landing
from views.dashboard import show_dashboard
from views.analytics import show_analytics
from views.prediction import show_prediction
from views.performance import show_performance
from views.reports import show_reports

st.set_page_config(

    page_title="AI Fraud Analytics",

    page_icon="💳",

    layout="wide",

    initial_sidebar_state="expanded"

)

with open("assets/style.css") as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True

    )

st.sidebar.markdown("# 💳 AI Fraud Analytics")

st.sidebar.caption("Enterprise Risk Intelligence")

st.sidebar.markdown("---")

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Home",

        "📊 Dashboard",

        "📈 Analytics",

        "🤖 AI Prediction",

        "📉 Model Performance",

        "📄 Reports",

        "ℹ About"

    ]

)

st.sidebar.markdown("---")

st.sidebar.success("Model : Random Forest")

st.sidebar.info("Accuracy : 98.72%")

st.sidebar.caption("Version 1.0")

if page=="🏠 Home":

    show_landing()

elif page=="📊 Dashboard":

    show_dashboard()

elif page=="📈 Analytics":

    show_analytics()

elif page=="🤖 AI Prediction":

    show_prediction()

elif page=="📉 Model Performance":

    show_performance()

elif page=="📄 Reports":

    show_reports()
elif page=="ℹ About":

    show_about()
st.markdown("---")

st.markdown("""
<div style="text-align:center;color:gray">

<b>AI Fraud Analytics Platform</b><br>

Version 1.0<br>

Developed using Python • Streamlit • Scikit-Learn • Power BI<br>

© 2026 Final Year Data Science Project

</div>
""", unsafe_allow_html=True)