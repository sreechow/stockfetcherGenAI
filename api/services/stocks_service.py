from typing import List, Optional
from sqlite3 import Connection
from ..models.stocks_model import Stock

class StocksService:
    @staticmethod
    def create(conn: Connection, data: Stock) -> int:
        query = """
        INSERT INTO stocks (symbol, name, market)
        VALUES (?, ?, ?)
        """
        cursor = conn.cursor()
        cursor.execute(query, (data.symbol, data.name, data.market))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def read_all(conn: Connection) -> List[Stock]:
        query = "SELECT * FROM stocks"
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Stock(**dict(zip([column[0] for column in cursor.description], row))) for row in rows]

    @staticmethod
    def read_by_id(conn: Connection, stock_id: int) -> Optional[Stock]:
        query = "SELECT * FROM stocks WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(query, (stock_id,))
        row = cursor.fetchone()
        if row:
            return Stock(**dict(zip([column[0] for column in cursor.description], row)))
        return None

    @staticmethod
    def update(conn: Connection, stock_id: int, data: Stock) -> bool:
        query = """
        UPDATE stocks
        SET symbol = ?, name = ?, market = ?
        WHERE id = ?
        """
        cursor = conn.cursor()
        cursor.execute(query, (data.symbol, data.name, data.market, stock_id))
        conn.commit()
        return cursor.rowcount > 0

    @staticmethod
    def delete(conn: Connection, stock_id: int) -> bool:
        query = "DELETE FROM stocks WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(query, (stock_id,))
        conn.commit()
        return cursor.rowcount > 0
