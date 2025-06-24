-- schema.sql (for PostgreSQL)

-- Drop tables if they already exist to ensure a clean start
DROP TABLE IF EXISTS Reviews;
DROP TABLE IF EXISTS Banks;

-- Create the Banks table to store bank information
CREATE TABLE Banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(255) NOT NULL UNIQUE
);

-- Create the Reviews table to store scraped and processed review data
CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INTEGER,
    review_text TEXT,
    rating INTEGER,
    review_date DATE,
    source VARCHAR(100),
    sentiment_label VARCHAR(50),
    sentiment_score NUMERIC,
    identified_theme VARCHAR(255),
    FOREIGN KEY (bank_id) REFERENCES Banks (bank_id)
);