from .database import get_db_connection

def insert_stock_metric(stock_id, current_price, week52_low, week52_high, percent_from_52low, percent_from_52high, percent_change_30d, percent_change_90d, created_at):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO stock_metrics 
        (stock_id, current_price, week52_low, week52_high, percent_from_52low, percent_from_52high, percent_change_30d, percent_change_90d, created_at) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (stock_id, current_price, week52_low, week52_high, percent_from_52low, percent_from_52high, percent_change_30d, percent_change_90d, created_at)
    )
    conn.commit()
    conn.close()

def update_stock_metric(metric_id, **kwargs):
    conn = get_db_connection()
    cursor = conn.cursor()
    for column, value in kwargs.items():
        cursor.execute(f"UPDATE stock_metrics SET {column} = ? WHERE id = ?", (value, metric_id))
    conn.commit()
    conn.close()

def delete_stock_metric(metric_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stock_metrics WHERE id = ?", (metric_id,))
    conn.commit()
    conn.close()
