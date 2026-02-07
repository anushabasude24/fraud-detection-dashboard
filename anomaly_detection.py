from sklearn.ensemble import IsolationForest

# Rule-based: high-value transactions
def flag_high_value(df, threshold=10000):
    df['high_value_flag'] = df['amount'] > threshold
    return df

# Rule-based: circular flows
def detect_circular_flows(df):
    df['circular_flag'] = df.duplicated(subset=['from_account', 'to_account'], keep=False)
    return df

# Optional ML: detect anomalies using Isolation Forest
def isolation_forest_anomaly(df):
    model = IsolationForest(contamination=0.05, random_state=42)
    df['ml_flag'] = model.fit_predict(df[['amount']])
    df['ml_flag'] = df['ml_flag'] == -1  # True = anomaly
    return df
