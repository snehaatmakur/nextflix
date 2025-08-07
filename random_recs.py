# random_recs.py

import pandas as pd #type: ignore
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer #type: ignore
from sklearn.metrics.pairwise import cosine_similarity #type: ignore
import numpy as np #type: ignore

# Load CSV
df = pd.read_csv("netflix_titles.csv")

# Create SQLite DB
conn = sqlite3.connect("netflix.db")
df.to_sql("netflix", conn, if_exists="replace", index=False)

# Ask user for genre
genre = input("🎬 Enter a genre for random recommendations: ").strip()

# Query by genre
query = f"""
SELECT title, description
FROM netflix
WHERE description IS NOT NULL
AND listed_in LIKE '%{genre}%'
LIMIT 1000;
"""
df_genre = pd.read_sql_query(query, conn)

if df_genre.empty:
    print(f"❌ No titles found in genre: {genre}")
else:
    # TF-IDF + similarity
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df_genre['description'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Randomly select one title
    index = np.random.randint(0, len(df_genre))
    selected_title = df_genre.iloc[index]['title']

    print(f"\n🎯 Random title selected: {selected_title}")
    print(f"\n📎 Similar recommendations in genre: {genre.title()}\n")

    # Get similar titles
    sim_scores = list(enumerate(cosine_sim[index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

    for i, score in sim_scores:
        print(f"- {df_genre.iloc[i]['title']}")
