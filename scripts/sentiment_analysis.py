import pandas as pd
from textblob import TextBlob

df = pd.read_csv("data/cleaned_reviews.csv")

def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "Positive", polarity
    elif polarity < -0.1:
        return "Negative", polarity
    else:
        return "Neutral", polarity

df[["sentiment_label", "sentiment_score"]] = df["review"].apply(
    lambda x: pd.Series(analyze_sentiment(str(x)))
)

df.to_csv("data/sentiment_reviews.csv", index=False)