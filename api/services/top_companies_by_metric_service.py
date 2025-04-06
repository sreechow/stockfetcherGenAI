from typing import List, Optional
from sqlite3 import Connection
from ..models.top_companies_by_metric_model import TopCompaniesByMetric

class TopCompaniesByMetricService:
    @staticmethod
    def create(conn: Connection, data: TopCompaniesByMetric) -> int:
        query = """
        INSERT INTO top_companies_by_metric (metric, rank, stock_symbol, company_name, value, source_url, fetched_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor = conn.cursor()
        cursor.execute(query, (data.metric, data.rank, data.stock_symbol, data.company_name, data.value, data.source_url, data.fetched_at))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def read_all(conn: Connection) -> List[TopCompaniesByMetric]:
        query = "SELECT * FROM top_companies_by_metric"
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return [TopCompaniesByMetric(**dict(zip([column[0] for column in cursor.description], row))) for row in rows]

    @staticmethod
    def read_by_id(conn: Connection, record_id: int) -> Optional[TopCompaniesByMetric]:
        query = "SELECT * FROM top_companies_by_metric WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(query, (record_id,))
        row = cursor.fetchone()
        if row:
            return TopCompaniesByMetric(**dict(zip([column[0] for column in cursor.description], row)))
        return None

    @staticmethod
    def update(conn: Connection, record_id: int, data: TopCompaniesByMetric) -> bool:
        query = """
        UPDATE top_companies_by_metric
        SET metric = ?, rank = ?, stock_symbol = ?, company_name = ?, value = ?, source_url = ?, fetched_at = ?
        WHERE id = ?
        """
        cursor = conn.cursor()
        cursor.execute(query, (data.metric, data.rank, data.stock_symbol, data.company_name, data.value, data.source_url, data.fetched_at, record_id))
        conn.commit()
        return cursor.rowcount > 0

    @staticmethod
    def delete(conn: Connection, record_id: int) -> bool:
        query = "DELETE FROM top_companies_by_metric WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(query, (record_id,))
        conn.commit()
        return cursor.rowcount > 0
