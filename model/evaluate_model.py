import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Evaluate model
def evaluate_model(df):
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    X = tfidf.fit_transform(df['content'])
    le = LabelEncoder()
    y = le.fit_transform(df['sentiment_label'])

    model = joblib.load("stock_movement_model.pkl")
    y_pred = model.predict(X)
    
    accuracy = accuracy_score(y, y_pred)
    precision = precision_score(y, y_pred, average='weighted')
    recall = recall_score(y, y_pred, average='weighted')
    f1 = f1_score(y, y_pred, average='weighted')
    
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1-Score: {f1}")

if __name__ == "__main__":
    file_path = "reddit_posts_with_sentiment.csv"
    data = load_data(file_path)
    evaluate_model(data)
