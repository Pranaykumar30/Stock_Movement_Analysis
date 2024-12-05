import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Train model
def train_model(df):
    # Example features and target
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    X = tfidf.fit_transform(df['content'])
    le = LabelEncoder()
    y = le.fit_transform(df['sentiment_label'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save the model
    joblib.dump(model, "stock_movement_model.pkl")
    print("Model saved as 'stock_movement_model.pkl'")

if __name__ == "__main__":
    file_path = "reddit_posts_with_sentiment.csv"
    data = load_data(file_path)
    train_model(data)
