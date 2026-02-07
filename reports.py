import streamlit as st

def export_flagged(df):
    # Filter flagged rows
    flagged = df[(df['high_value_flag']) | (df['circular_flag']) | (df.get('ml_flag', False))]
    
    # Show download button in Streamlit
    st.download_button("Download Flagged Transactions", "flagged_transactions.csv", flagged.to_csv(index=False))
