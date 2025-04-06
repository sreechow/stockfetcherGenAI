from .database import get_db_connection

def insert_stock(symbol, name, market):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO stocks (symbol, name, market) VALUES (?, ?, ?)",
        (symbol, name, market)
    )
    conn.commit()
    conn.close()

def update_stock(stock_id, name=None, market=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE stocks SET name = ? WHERE id = ?", (name, stock_id))
    if market:
        cursor.execute("UPDATE stocks SET market = ? WHERE id = ?", (market, stock_id))
    conn.commit()
    conn.close()

def delete_stock(stock_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stocks WHERE id = ?", (stock_id,))
    conn.commit()
    conn.close()
