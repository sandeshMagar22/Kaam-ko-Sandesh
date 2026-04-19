import pandas as pd
from utils.db import get_connection


def transform_and_load():

    conn = get_connection()

    # -------------------------------
    # 🔹 LOAD DATA
    # -------------------------------
    df = pd.read_sql("SELECT * FROM raw_jobs", conn)

    # -------------------------------
    # 🔹 BASIC CLEANING
    # -------------------------------
    df.drop_duplicates(subset=['link'], inplace=True)

    df['title'] = df['title'].fillna("").str.strip().str.lower()
    df['company'] = df['company'].fillna("").str.strip()
    df['location'] = df['location'].fillna("").str.strip().str.lower()

    # -------------------------------
    # 🔹 ROLE FILTER (ALL COMPANIES)
    # -------------------------------
    keywords = [
        "data engineer",
        "data analyst",
        "business analyst",
        "intern",
        "trainee"
    ]

    df = df[
        df['title'].apply(lambda x: any(k in x for k in keywords))
    ]

   # -------------------------------
# 🔹 LOCATION FILTER (ONLY SPECIFIC COMPANIES)
# -------------------------------
    special_companies = ["Cedargate", "Fusemachine", "Leapfrog"]

    nepal_filter = df['location'].str.contains(
        r"\bnepal\b|\bnp\b", case=False, na=False
    )

    df = df[
        (
            df['company'].isin(special_companies) &
            nepal_filter
        )
        |
        (
            ~df['company'].isin(special_companies)
        )
    ]

    # -------------------------------
    # 🔹 FINAL CLEANING
    # -------------------------------
    df = df[df['title'] != ""]

    # -------------------------------
    # 🔹 INSERT INTO clean_jobs
    # -------------------------------
    cursor = conn.cursor()

    # ✅ CLEAR OLD DATA (IMPORTANT)
    cursor.execute("TRUNCATE TABLE clean_jobs")

    query = """
    INSERT INTO clean_jobs (company, title, location, link, source)
    VALUES (%s, %s, %s, %s, %s)
    """

    data = [
        (
            row['company'],
            row['title'],
            row['location'],
            row['link'],
            row.get('source', 'unknown')
        )
        for _, row in df.iterrows()
    ]

    cursor.executemany(query, data)

    conn.commit()

    cursor.close()
    conn.close()

    print(f"✅ Clean data inserted: {len(data)} rows")


# -----------------------------------
# 🚀 ENTRY POINT (IMPORTANT)
# -----------------------------------
if __name__ == "__main__":
    transform_and_load()