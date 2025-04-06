from typing import List, Optional
from sqlite3 import Connection
from ..models.stock_prices_model import StockPrice

class StockPricesService:
    @staticmethod
    def create(conn: Connection, data: StockPrice) -> int:
        query = """
        INSERT INTO stock_prices (stock_id, date, price)
        VALUES (?, ?, ?)
        """
        cursor = conn.cursor()
        cursor.execute(query, (data.stock_id, data.date, data.price))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def read_all(conn: Connection) -> List[StockPrice]:
        query = "SELECT * FROM stock_prices"
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return [StockPrice(**dict(zip([column[0] for column in cursor.description], row))) for row in rows]

    @staticmethod
    def read_by_id(conn: Connection, price_id: int) -> Optional[StockPrice]:
        query = "SELECT * FROM stock_prices WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(query, (price_id,))
        row = cursor.fetchone()
        if row:
            return StockPrice(**dict(zip([column[0] for column in cursor.description], row)))
        return None

    @staticmethod
    def update(conn: Connection, price_id: int, data: StockPrice) -> bool:
        query = """
        UPDATE stock_prices
        SET stock_id = ?, date = ?, price = ?
        WHERE id = ?
        """
        cursor = conn.cursor()
        cursor.execute(query, (data.stock_id, data.date, data.price, price_id))
        conn.commit()
        return cursor.rowcount > 0

    @staticmethod
    def delete(conn: Connection, price_id: int) -> bool:
        query = "DELETE FROM stock_prices WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(query, (price_id,))
        conn.commit()
        return cursor.rowcount > 0
