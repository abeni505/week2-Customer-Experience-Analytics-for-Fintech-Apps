# thematic_analysis.py (Corrected)

import pandas as pd
import os

print("🔍 Loading data with sentiment...")
input_path = "data/processed/sentiment_reviews.csv"
try:
    df = pd.read_csv(input_path)
    print("✅ Data shape:", df.shape)
except FileNotFoundError:
    print(f"❌ Error: File not found at {input_tath}. Please run sentiment_analysis.py first.")
    exit()


print("⏳ Performing thematic analysis...")

# Define keywords for each theme
theme_keywords = {
    'UI & Experience': ['ui', 'interface', 'design', 'look', 'easy to use', 'user friendly', 'simple', 'clean'],
    'Performance': ['slow', 'fast', 'crash', 'bug', 'lag', 'performance', 'loading', 'stuck', 'error'],
    'Login & Security': ['login', 'password', 'fingerprint', 'otp', 'security', 'authentication', 'sign in', 'secure'],
    'Transactions': ['transfer', 'payment', 'transaction', 'send money', 'receive', 'fee', 'charge'],
    'Customer Support': ['support', 'help', 'customer service', 'call center', 'response'],
    'Feature Request': ['feature', 'add', 'implement', 'suggestion', 'dark mode', 'wish', 'hope']
}

def identify_theme(review):
    """Identifies one or more themes based on keywords found in the review."""
    review_lower = str(review).lower()
    found_themes = []
    for theme, keywords in theme_keywords.items():
        if any(keyword in review_lower for keyword in keywords):
            found_themes.append(theme)
    # If no specific theme is found, categorize as 'General Feedback'
    return ', '.join(found_themes) if found_themes else 'General Feedback'

# This creates the crucial 'identified_theme(s)' column
df['identified_theme(s)'] = df['review'].apply(identify_theme)
print("✅ Thematic analysis complete.")

# Save the final, fully analyzed file
output_path = "data/processed/final_analyzed_reviews.csv"
df.to_csv(output_path, index=False)

print(f"🎉 Final analyzed data saved to {output_path}")