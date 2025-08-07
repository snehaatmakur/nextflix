# Nextflix
## 🎬 Netflix Recommendation System (Python + SQL + NLP)

Welcome to a fun and simple project that recommends Netflix shows and movies based on **genre** using **Python**, **SQLite**, and **NLP (TF-IDF)**.

This project contains two Python scripts:

---

## 📁 Files

- `top_recs.py` – Recommends the **top 5 most representative titles** in a genre  
- `random_recs.py` – Picks a **random title** in a genre and recommends **5 similar shows/movies**

Both scripts use:
- `netflix_titles.csv` – Public Netflix dataset from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- `sqlite3` – Local SQL database to store and query data
- `scikit-learn` – For TF-IDF vectorization and cosine similarity

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/netflix-recommendations.git
cd netflix-recommendations
