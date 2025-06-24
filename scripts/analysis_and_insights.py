# analysis_and_insights.py (Corrected)

import pandas as pd

print("Starting analysis to identify drivers and pain points...")

# Load the final processed data
input_path = 'data/processed/final_analyzed_reviews.csv'
try:
    df = pd.read_csv(input_path)
except FileNotFoundError:
    print(f"❌ Error: Processed data file not found. Please ensure '{input_path}' exists by running all previous scripts.")
    exit()

# Get the list of banks
banks = df['bank'].unique()

print("\n--- Analysis Results ---")

for bank in banks:
    print(f"\n===== Insights for {bank} =====")
    bank_df = df[df['bank'] == bank]

    # --- Identify Drivers (from positive reviews, 4-5 stars) ---
    drivers_df = bank_df[bank_df['rating'] >= 4]
    driver_themes = drivers_df.assign(theme=drivers_df['identified_theme(s)'].str.split(', ')).explode('theme')
    top_drivers = driver_themes[driver_themes['theme'] != 'General Feedback']['theme'].value_counts().nlargest(3)

    print("\n[+] Top Drivers of Satisfaction:")
    if not top_drivers.empty:
        for theme, count in top_drivers.items():
            print(f"  - {theme} (mentioned {count} times in positive reviews)")
    else:
        print("  - Not enough specific positive themes found.")

    # --- Identify Pain Points (from negative reviews, 1-2 stars) ---
    pain_points_df = bank_df[bank_df['rating'] <= 2]
    pain_point_themes = pain_points_df.assign(theme=pain_points_df['identified_theme(s)'].str.split(', ')).explode('theme')
    top_pain_points = pain_point_themes[pain_point_themes['theme'] != 'General Feedback']['theme'].value_counts().nlargest(3)

    print("\n[-] Top Pain Points:")
    if not top_pain_points.empty:
        for theme, count in top_pain_points.items():
            print(f"  - {theme} (mentioned {count} times in negative reviews)")
    else:
        print("  - Not enough specific negative themes found.")

print("\n--- End of Analysis ---")
print("Use these insights to write your report and suggest improvements.")