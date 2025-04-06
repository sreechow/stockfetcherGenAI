import sqlite3

DATABASE_PATH = "/Users/SreeChow/stockfetcherGenAI/utils/stockfetcher.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # To return rows as dictionaries
    return conn
