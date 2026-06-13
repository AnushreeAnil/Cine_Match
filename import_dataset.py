import pandas as pd
import sqlite3
import os

def import_movies():
    # Load the CSV file
    df = pd.read_csv("movie_dataset.csv")
    print(f"Total movies in dataset: {len(df)}")

    # Clean up the data - drop rows where important fields are missing
    df = df.dropna(subset=["Movie_Title", "Movie_Genre"])
    df["Movie_Director"] = df["Movie_Director"].fillna("Unknown")
    df["Movie_Cast"] = df["Movie_Cast"].fillna("Unknown")
    df["Movie_Overview"] = df["Movie_Overview"].fillna("No description available.")
    df["Movie_Vote"] = df["Movie_Vote"].fillna(0)
    df["Movie_Release_Date"] = df["Movie_Release_Date"].fillna("2000-01-01")

    # Extract year from release date
    def get_year(date_str):
        try:
            return int(str(date_str)[:4])
        except:
            return 2000

    df["year"] = df["Movie_Release_Date"].apply(get_year)

    print(f"Movies after cleaning: {len(df)}")

    # Connect to database
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    # Drop old table and recreate fresh
    cursor.execute("DROP TABLE IF EXISTS movies")
    cursor.execute("DROP TABLE IF EXISTS user_ratings")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            director TEXT,
            cast TEXT,
            description TEXT,
            rating REAL,
            year INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            movie_id INTEGER NOT NULL,
            rating REAL NOT NULL,
            FOREIGN KEY (movie_id) REFERENCES movies(id)
        )
    """)

    # Insert movies into database
    count = 0
    for _, row in df.iterrows():
        title = str(row["Movie_Title"]).strip()
        genre = str(row["Movie_Genre"]).strip()
        director = str(row["Movie_Director"]).strip()
        cast = str(row["Movie_Cast"]).strip()
        description = str(row["Movie_Overview"]).strip()
        rating = float(row["Movie_Vote"])
        year = int(row["year"])

        # Skip if title is empty
        if not title or title == "nan":
            continue

        cursor.execute("""
            INSERT INTO movies (title, genre, director, cast, description, rating, year)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (title, genre, director, cast, description, rating, year))
        count += 1

    conn.commit()
    conn.close()
    print(f"Successfully imported {count} movies into the database!")

if __name__ == "__main__":
    import_movies()
