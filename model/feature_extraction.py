import pandas as pd

# Feature extraction
def extract_features(df):
    # Example feature: Title length
    df['title_length'] = df['title'].apply(len)
    
    # Example feature: Content length
    df['content_length'] = df['content'].apply(len)
    
    return df

if __name__ == "__main__":
    file_path = "reddit_posts_with_sentiment.csv"
    data = pd.read_csv(file_path)
    feature_data = extract_features(data)
    feature_data.to_csv("feature_reddit_posts.csv", index=False)
    print("Features extracted and saved to 'feature_reddit_posts.csv'")
