import pandas as pd #type: ignore
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer #type: ignore
from sklearn.metrics.pairwise import cosine_similarity #type: ignore
import numpy as np #type: ignore

# Load CSV
df = pd.read_csv("netflix_titles.csv")

# Connect to SQLite
conn = sqlite3.connect("netflix.db")
df.to_sql("netflix", conn, if_exists="replace", index=False)

# Prompt user for genre
genre = input("🎬 Enter a genre (e.g., Drama, Comedy, Action, Horror): ").strip()

# Query movies/shows by genre
query = f"""
SELECT title, description
FROM netflix
WHERE description IS NOT NULL
AND listed_in LIKE '%{genre}%'
LIMIT 1000;
"""
df_genre = pd.read_sql_query(query, conn)

# Handle case where no results found
if df_genre.empty:
    print(f"❌ No titles found in genre: {genre}")
else:
    # TF-IDF vectorization
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df_genre['description'])

    # Cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Compute average similarity for each title
    avg_sim_scores = cosine_sim.mean(axis=1)

    # Get top 5 most representative titles
    top_indices = avg_sim_scores.argsort()[::-1][:5]

    print(f"\n🔍 Top 5 recommended titles in the genre: {genre.title()}\n")
    for i in top_indices:
        print(f"- {df_genre.iloc[i]['title']}")

    