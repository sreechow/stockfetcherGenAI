
from .database import get_db_connection

def insert_stock_price(stock_id, date, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO stock_prices (stock_id, date, price) VALUES (?, ?, ?)",
        (stock_id, date, price)
    )
    conn.commit()
    conn.close()

def update_stock_price(price_id, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE stock_prices SET price = ? WHERE id = ?", (price, price_id))
    conn.commit()
    conn.close()

def delete_stock_price(price_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stock_prices WHERE id = ?", (price_id,))
    conn.commit()
    conn.close()