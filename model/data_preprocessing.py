import pandas as pd
import numpy as np

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Clean and preprocess data
def preprocess_data(df):
    # Fill missing values
    df['content'].fillna("No Content", inplace=True)
    df['author'].fillna("Anonymous", inplace=True)
    
    # Convert UTC to datetime
    df['created_datetime'] = pd.to_datetime(df['created_utc'], unit='s')
    df.drop('created_utc', axis=1, inplace=True)
    
    return df

if __name__ == "__main__":
    # Example usage
    file_path = "reddit_posts.csv"
    data = load_data(file_path)
    clean_data = preprocess_data(data)
    clean_data.to_csv("clean_reddit_posts.csv", index=False)
    print("Cleaned data saved to 'clean_reddit_posts.csv'")
