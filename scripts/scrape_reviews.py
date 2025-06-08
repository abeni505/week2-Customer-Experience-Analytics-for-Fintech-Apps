from google_play_scraper import Sort, reviews
import pandas as pd

apps = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

def fetch_reviews(app_id, bank_name):
    all_reviews = []
    for score in range(1, 6):  # fetch 1 to 5 star reviews
        result, _ = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=200,
            filter_score_with=score
        )
        for r in result:
            all_reviews.append({
                'review': r['content'],
                'rating': r['score'],
                'date': r['at'].strftime('%Y-%m-%d'),
                'bank': bank_name,
                'source': 'Google Play'
            })
    return pd.DataFrame(all_reviews)

frames = []
for name, app_id in apps.items():
    df = fetch_reviews(app_id, name)
    frames.append(df)

all_reviews = pd.concat(frames, ignore_index=True)
all_reviews.to_csv("data/raw_reviews.csv", index=False)