import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy

print("🔍 Loading data...")
df = pd.read_csv("data/sentiment_reviews.csv")
print("✅ Data shape:", df.shape)

nlp = spacy.load("en_core_web_sm")

print("🧹 Cleaning reviews...")
def clean_text(text):
    doc = nlp(str(text).lower())
    tokens = [
        token.lemma_ for token in doc
        if not token.is_stop and token.is_alpha and len(token) > 2
    ]
    return " ".join(tokens)

df['cleaned_review'] = df['review'].apply(clean_text)

print("🔑 Extracting keywords by bank...")
themes = {}
for bank in df['bank'].unique():
    bank_text = df[df['bank'] == bank]['cleaned_review']
    vectorizer = TfidfVectorizer(max_df=0.9, min_df=5, max_features=50)
    X = vectorizer.fit_transform(bank_text)
    bank_keywords = vectorizer.get_feature_names_out().tolist()
    themes[bank] = bank_keywords[:10]
    print(f"📌 {bank}: {bank_keywords[:10]}")

# Save
theme_df = pd.DataFrame.from_dict(themes, orient='index').transpose()
theme_df.to_csv("data/bank_themes_keywords.csv", index=False)

print("✅ Thematic keywords extracted and saved.")