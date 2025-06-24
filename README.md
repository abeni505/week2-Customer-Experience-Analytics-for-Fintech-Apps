
# Customer Experience Analytics for Ethiopian Fintech Apps

This project is a comprehensive data engineering and analysis challenge focused on understanding customer satisfaction with mobile banking applications in Ethiopia. By scraping, processing, and analyzing user reviews from the Google Play Store, the project simulates the role of a Data Analyst at a consulting firm tasked with providing actionable insights to leading banks.

The analysis centers on three major Ethiopian banks:
- **Commercial Bank of Ethiopia (CBE)**
- **Bank of Abyssinia (BOA)**
- **Dashen Bank**

---

## Project Pipeline

The project follows a structured data pipeline to achieve its objectives:

1.  **Data Collection:** Scraped over 1,200 user reviews for the three banking apps from the Google Play Store using the `google-play-scraper` library.
2.  **Preprocessing:** Cleaned the raw data by handling duplicates, normalizing date formats, and structuring the dataset for analysis.
3.  **Sentiment Analysis:** Applied NLP techniques using `TextBlob` to classify each review's sentiment as Positive, Negative, or Neutral and assigned a polarity score.
4.  **Thematic Analysis:** Implemented a rule-based keyword matching system to categorize each review into predefined themes such as "UI & Experience," "Performance," or "Login & Security." This step added a crucial `identified_theme(s)` column to the dataset.
5.  **Database Storage:** Designed a relational database schema and used PostgreSQL to persistently store the final, enriched data, simulating an enterprise data warehousing workflow.
6.  **Insights & Visualization:** Analyzed the final dataset to identify key drivers of satisfaction and customer pain points, creating compelling visualizations with Matplotlib and Seaborn to support the findings.

---

## Folder Structure

The project is organized with the following directory structure:

```
├── data/
│   ├── raw/         # Stores raw scraped data from Google Play
│   └── processed/   # Stores cleaned and fully analyzed data
├── database/
│   ├── schema.sql
│   └── load_data_to_postgres.py
├── reports/
│   ├── visuals/     # Stores generated plots and charts
│   └── final_report.md
├── scripts/
│   ├── scrape_reviews.py
│   ├── preprocess_reviews.py
│   ├── sentiment_analysis.py
│   ├── thematic_analysis.py
│   ├── analysis_and_insights.py
│   └── create_visuals.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Setup and Installation

To run this project locally, please follow these steps. This setup is optimized for **macOS users with Homebrew**.

**1. Clone the Repository:**
```bash
git clone [https://github.com/abeni505/week2-Customer-Experience-Analytics-for-Fintech-Apps.git](https://github.com/abeni505/week2-Customer-Experience-Analytics-for-Fintech-Apps.git)
cd week2-Customer-Experience-Analytics-for-Fintech-Apps
```

**2. Create and Activate Virtual Environment:**
```bash
python3 -m venv week2-venv
source week2-venv/bin/activate
```

**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**4. Set Up PostgreSQL Database:**
This project uses PostgreSQL as a reliable local database.
```bash
brew install postgresql
brew services start postgresql
```

---

## How to Run the Full Pipeline

Execute the scripts from the project's root directory **in the following order** to run the entire data pipeline from scraping to analysis.

```bash
# Ensure your virtual environment is active
source week2-venv/bin/activate

# 1. Scrape raw data from the Google Play Store
echo "--- Running Step 1: Scrape Reviews ---"
python scrape_reviews.py

# 2. Preprocess and clean the raw data
echo "\n--- Running Step 2: Preprocess Reviews ---"
python preprocess_reviews.py

# 3. Analyze review sentiment
echo "\n--- Running Step 3: Sentiment Analysis ---"
python sentiment_analysis.py

# 4. Perform thematic analysis to categorize reviews
echo "\n--- Running Step 4: Thematic Analysis ---"
python thematic_analysis.py

# 5. Load the final, enriched data into the PostgreSQL database
echo "\n--- Running Step 5: Load Data to Database ---"
python database/load_data_to_postgres.py

# 6. Run the final analysis to get text-based insights
echo "\n--- Running Step 6: Generate Insights ---"
python scripts/analysis_and_insights.py

# 7. Generate visualizations for the final report
echo "\n--- Running Step 7: Create Visuals ---"
python scripts/create_visuals.py

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


## Final Deliverables

The key outputs of this project are:

-   **Actionable Insights:** The `scripts/analysis_and_insights.py` script prints the top drivers and pain points for each bank to the console.
-   **Visualizations:** All generated plots and charts are saved as `.png` files in the `reports/visuals/` directory.
-   **Final Report:** The comprehensive analysis and recommendations are detailed in the `reports/final_report.md` file.

## 👨‍💻 Author

Abenezer M. Woldesenbet 
