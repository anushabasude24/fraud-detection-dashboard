import streamlit as st
import plotly.express as px
from data_processing import load_transactions
from anomaly_detection import flag_high_value, detect_circular_flows, isolation_forest_anomaly
from reports import export_flagged

st.title("Fraud Detection Dashboard")

# Upload CSV/JSON
uploaded_file = st.file_uploader("Upload transaction CSV/JSON", type=['csv','json'])

if uploaded_file:
    df = load_transactions(uploaded_file)
    
    # Apply anomaly detection
    df = flag_high_value(df)
    df = detect_circular_flows(df)
    df = isolation_forest_anomaly(df)
    
    # Filter by account
    account = st.selectbox("Select account", df['from_account'].unique())
    filtered = df[df['from_account'] == account]
    
    # Timeline plot
    fig = px.line(filtered, x='transaction_date', y='amount', color='high_value_flag', markers=True,
                  title=f"Transaction Timeline for {account}")
    st.plotly_chart(fig)
    
    # Show flagged transactions
    st.subheader("Flagged Transactions")
    st.dataframe(filtered[(filtered['high_value_flag']) | (filtered['circular_flag']) | (filtered['ml_flag'])])
    
    # Export flagged transactions
    export_flagged(df)
