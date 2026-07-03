import plotly.express as px


def fraud_distribution(df):

    fig = px.pie(
        df,
        names="is_fraud",
        title="Fraud Distribution",
        color="is_fraud",
        color_discrete_map={
            0: "#22C55E",
            1: "#EF4444"
        }
    )

    fig.update_traces(textposition="inside")

    return fig


def merchant_chart(df):

    temp = (
        df["merchant_category"]
        .value_counts()
        .reset_index()
    )

    temp.columns = [
        "merchant_category",
        "count"
    ]

    fig = px.bar(
        temp,
        x="merchant_category",
        y="count",
        title="Merchant Category Distribution"
    )

    return fig


def hourly_chart(df):

    temp = (
        df.groupby("transaction_hour")
        .size()
        .reset_index(name="Transactions")
    )

    fig = px.line(
        temp,
        x="transaction_hour",
        y="Transactions",
        markers=True,
        title="Transactions by Hour"
    )

    return fig


def fraud_hour_chart(df):

    temp = (
        df[df["is_fraud"] == 1]
        .groupby("transaction_hour")
        .size()
        .reset_index(name="Frauds")
    )

    fig = px.bar(
        temp,
        x="transaction_hour",
        y="Frauds",
        title="Fraud Transactions by Hour"
    )

    return fig


def merchant_risk_chart(df):

    temp = (
        df[df["is_fraud"] == 1]
        .groupby("merchant_category")
        .size()
        .reset_index(name="Frauds")
    )

    fig = px.bar(
        temp,
        x="merchant_category",
        y="Frauds",
        title="High Risk Merchants"
    )

    return fig


def amount_distribution_chart(df):

    fig = px.histogram(
        df,
        x="amount",
        nbins=30,
        title="Transaction Amount Distribution"
    )

    return fig