# database/load_data_to_postgres.py
import psycopg2
from psycopg2 import extras
import pandas as pd
import os

# --- Configuration ---
# Default PostgreSQL connection settings for a local install
# Your Mac username is the default user.
DB_USER = "Abeni"
DB_NAME = "postgres"  # Connect to the default administrative database
DB_PASSWORD = ""  # Usually no password is needed for local default setup
DB_HOST = "localhost"
DB_PORT = "5432"

SCHEMA_FILE = 'database/schema.sql'
# --- IMPORTANT: UPDATE THIS PATH ---
CLEANED_CSV_PATH = 'data/processed/cleaned_reviews.csv'

def setup_database():
    """Connects to PostgreSQL, runs the schema, and populates the tables."""
    try:
        # Establish the connection
        with psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        ) as conn:
            with conn.cursor() as cur:
                print("✅ Successfully connected to PostgreSQL.")

                # --- Execute the schema script ---
                print(f"⏳ Executing schema from {SCHEMA_FILE}...")
                with open(SCHEMA_FILE, 'r') as f:
                    cur.execute(f.read())
                print("✅ Schema created successfully.")

                # --- Load and Insert Data ---
                print(f"⏳ Loading data from {CLEANED_CSV_PATH}...")
                df = pd.read_csv(CLEANED_CSV_PATH)
                df['date'] = pd.to_datetime(df['date']).dt.date

                # --- Populate Banks Table ---
                bank_map = {}
                for bank_name in df['bank'].unique():
                    cur.execute(
                        "INSERT INTO Banks (bank_name) VALUES (%s) RETURNING bank_id",
                        (bank_name,)
                    )
                    bank_id = cur.fetchone()[0]
                    bank_map[bank_name] = bank_id
                print(f"✅ Populated Banks table with {len(bank_map)} banks.")

                # --- Populate Reviews Table ---
                review_records = []
                for _, row in df.iterrows():
                    bank_id = bank_map[row['bank']]
                    review_records.append((
                        bank_id, row.get('review'), row.get('rating'), row.get('date'),
                        row.get('source'), row.get('sentiment_label'),
                        row.get('sentiment_score'), row.get('identified_theme(s)')
                    ))
                
                # Use executemany for efficient bulk insertion
                psycopg2.extras.execute_values(cur,
                    """
                    INSERT INTO Reviews (bank_id, review_text, rating, review_date, source, sentiment_label, sentiment_score, identified_theme)
                    VALUES %s
                    """,
                    review_records
                )
                print(f"✅ Successfully inserted {cur.rowcount} entries into the Reviews table.")

    except FileNotFoundError:
        print(f"❌ ERROR: The file was not found. Please check your path: {CLEANED_CSV_PATH}")
    except psycopg2.Error as e:
        print(f"❌ ERROR: A database error occurred: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    setup_database()