from typing import List, Optional
from sqlite3 import Connection
from ..models.revenue_projections_model import RevenueProjection

class RevenueProjectionsService:
    @staticmethod
    def create(conn: Connection, data: RevenueProjection) -> int:
        query = """
        INSERT INTO revenue_projections (stock_id, year, revenue_estimate)
        VALUES (?, ?, ?)
        """
        cursor = conn.cursor()
        cursor.execute(query, (data.stock_id, data.year, data.revenue_estimate))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def read_all(conn: Connection) -> List[RevenueProjection]:
        query = "SELECT * FROM revenue_projections"
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return [RevenueProjection(**dict(zip([column[0] for column in cursor.description], row))) for row in rows]

    @staticmethod
    def read_by_id(conn: Connection, projection_id: int) -> Optional[RevenueProjection]:
        query = "SELECT * FROM revenue_projections WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(query, (projection_id,))
        row = cursor.fetchone()
        if row:
            return RevenueProjection(**dict(zip([column[0] for column in cursor.description], row)))
        return None

    @staticmethod
    def update(conn: Connection, projection_id: int, data: RevenueProjection) -> bool:
        query = """
        UPDATE revenue_projections
        SET stock_id = ?, year = ?, revenue_estimate = ?
        WHERE id = ?
        """
        cursor = conn.cursor()
        cursor.execute(query, (data.stock_id, data.year, data.revenue_estimate, projection_id))
        conn.commit()
        return cursor.rowcount > 0

    @staticmethod
    def delete(conn: Connection, projection_id: int) -> bool:
        query = "DELETE FROM revenue_projections WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(query, (projection_id,))
        conn.commit()
        return cursor.rowcount > 0
