# scripts/05_create_visuals.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

print("Starting visualization generation...")

# --- Load Data and Setup ---
input_path = 'data/processed/final_analyzed_reviews.csv'
visuals_dir = 'reports/visuals/'

try:
    df = pd.read_csv(input_path)
except FileNotFoundError:
    print(f"❌ Error: Processed data file not found at {input_path}.")
    exit()

# --- Plot 1: Rating Distribution by Bank ---
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='rating', hue='bank', palette='viridis')
plt.title('Rating Distribution Across Banks')
plt.xlabel('Star Rating')
plt.ylabel('Number of Reviews')
plt.legend(title='Bank')
plt.tight_layout()
plt.savefig(os.path.join(visuals_dir, 'rating_distribution.png'))
plt.close()
print("✅ Saved rating_distribution.png")

# --- Plot 2: Sentiment Trends by Bank ---
plt.figure(figsize=(12, 7))
sns.countplot(data=df, x='bank', hue='sentiment_label', hue_order=['Positive', 'Neutral', 'Negative'], palette='plasma')
plt.title('Sentiment Trends by Bank')
plt.xlabel('Bank')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=10)
plt.tight_layout()
plt.savefig(os.path.join(visuals_dir, 'sentiment_trends.png'))
plt.close()
print("✅ Saved sentiment_trends.png")

# --- Plot 3: Keyword Cloud for Pain Points ---
plt.figure(figsize=(10, 7))
negative_text = " ".join(review for review in df[df['rating'] <= 2]['review'].dropna())
if negative_text:
    wordcloud = WordCloud(width=1600, height=800, background_color='white', colormap='Reds').generate(negative_text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Common Words in Negative Reviews (Pain Points)', size=20)
    plt.savefig(os.path.join(visuals_dir, 'keyword_cloud_pain_points.png'))
    plt.close()
    print("✅ Saved keyword_cloud_pain_points.png")

print(f"\nVisualizations saved to '{visuals_dir}'")