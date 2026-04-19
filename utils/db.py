import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root123",
            database="jobs_db"
        )
        return conn
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None