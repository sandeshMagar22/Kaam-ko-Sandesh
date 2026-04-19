import csv
import os
from utils.db import get_connection

def load_to_mysql(jobs):
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    csv_path = os.path.join('data', 'jobs_extracted.csv')
    
    # Save to CSV
    try:
        with open(csv_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Company', 'Title', 'Location', 'Link', 'Source'])
            writer.writerows(jobs)
        print(f"Data also saved to {csv_path}")
    except Exception as e:
        print("CSV backup Error:", e)

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO raw_jobs (company, title, location, link, source)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.executemany(query, jobs)
        conn.commit()

        print("Data inserted into MySQL")

    except Exception as e:
        print("Database Error (MySQL not configured, using CSV fallback):", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()