
# 📊 Week 2 – Customer Experience Analytics for Fintech Apps

This project analyzes customer reviews from the Google Play Store for three major Ethiopian banks using scraping, sentiment analysis, and keyword-based thematic clustering.

## 🏦 Banks Analyzed

- Commercial Bank of Ethiopia (CBE)
- Dashen Bank
- Bank of Abyssinia (BOA)

---

## 📌 Project Objectives

- Scrape user reviews from the Play Store using `google-play-scraper`.
- Preprocess the data by cleaning and normalizing.
- Perform sentiment analysis using TextBlob.
- Extract keywords to begin thematic clustering.
- Prepare data for future storage and insights.

---

## 🛠️ Project Structure

```bash
week2-Customer-Experience-Analytics-for-Fintech-Apps/
│
├── data/
│   ├── raw_reviews.csv                # Raw scraped reviews
│   └── cleaned_reviews.csv            # Cleaned/preprocessed reviews
│
├── scripts/
│   ├── scrape_reviews.py              # Script to scrape Google Play Store
│   └── preprocess_reviews.py          # Script to clean and normalize review data
│
├── notebooks/
│   └── (optional Jupyter notebooks)
│
├── README.md                          # You're here!
├── requirements.txt                   # Project dependencies
├── .gitignore                         # Files and folders to ignore
```

---

## ⚙️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Scrape Google Play Reviews

```bash
python scripts/scrape_reviews.py
```

### 3. Preprocess the Reviews

```bash
python scripts/preprocess_reviews.py
```

---

## 📊 Sample Data Schema

| Column Name | Description                        |
|-------------|------------------------------------|
| review      | Text content of the review         |
| rating      | User rating (1–5 stars)            |
| date        | Date of posting (YYYY-MM-DD)       |
| bank        | Bank the review belongs to         |
| source      | Always "Google Play"               |

---

## ✅ Task 1 Progress

- [x] 400+ reviews scraped per bank (1,200+ total)
- [x] Duplicate and null values removed
- [x] Date normalized
- [x] Final cleaned CSV created

---

## 🚧 Task 2 (In Progress)

- [x] Sentiment analysis using TextBlob
- [ ] Keyword extraction and theme clustering
- [ ] Save results with sentiment + theme labels

---

## 👨‍💻 Author

Abenezer Mulugeta Woldesenbet (@abeni505)

---

## 📎 Resources

- [`google-play-scraper`](https://pypi.org/project/google-play-scraper/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [Pandas Docs](https://pandas.pydata.org/)
