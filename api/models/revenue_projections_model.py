from .database import get_db_connection

def insert_revenue_projection(stock_id, year, revenue_estimate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO revenue_projections (stock_id, year, revenue_estimate) VALUES (?, ?, ?)",
        (stock_id, year, revenue_estimate)
    )
    conn.commit()
    conn.close()

def update_revenue_projection(projection_id, revenue_estimate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE revenue_projections SET revenue_estimate = ? WHERE id = ?", (revenue_estimate, projection_id))
    conn.commit()
    conn.close()

def delete_revenue_projection(projection_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM revenue_projections WHERE id = ?", (projection_id,))
    conn.commit()
    conn.close()

def read_all_revenue_projections():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM revenue_projections")
    rows = cursor.fetchall()
    conn.close()
    return rows