import pandas as pd

def load_transactions(file):
    """
    Load transaction data from uploaded CSV or JSON and clean it.
    """
    # Check the type of uploaded file
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith('.json'):
        df = pd.read_json(file)
    else:
        raise ValueError("Unsupported file type")
    
    # Convert date column to datetime
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    
    # Fill missing values with 0 or empty string
    df.fillna(0, inplace=True)
    
    return df

