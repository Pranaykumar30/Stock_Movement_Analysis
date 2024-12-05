import praw
import pandas as pd

# Reddit API credentials
client_id="34-AVonXEVJsMVbftbc2cA",
client_secret="5P8SQW32l8oEWRghTMP64zEwCHmDnA",
user_agent="TeslaDataScraper/0.1 by Pranay_Kumar_30"

# Initialize Reddit instance
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

# Function to scrape subreddit data
def scrape_subreddit(subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    
    for post in subreddit.hot(limit=limit):
        posts.append({
            'post_id': post.id,
            'title': post.title,
            'content': post.selftext,
            'subreddit': subreddit_name,
            'author': str(post.author),
            'created_utc': post.created_utc
        })
    
    return pd.DataFrame(posts)

if __name__ == "__main__":
    # Example usage
    subreddit_name = "stocks"
    data = scrape_subreddit(subreddit_name, limit=100)
    data.to_csv("reddit_posts.csv", index=False)
    print(f"Scraped data saved to 'reddit_posts.csv'")
