from typing import List
from sqlite3 import Connection
from ..models.stock_metrics_model import insert_stock_metric, update_stock_metric, delete_stock_metric, StockMetric

class StockMetricsService:
    @staticmethod
    def add_stock_metric(stock_id, current_price, week52_low, week52_high, percent_from_52low, percent_from_52high, percent_change_30d, percent_change_90d, created_at):
        try:
            insert_stock_metric(stock_id, current_price, week52_low, week52_high, percent_from_52low, percent_from_52high, percent_change_30d, percent_change_90d, created_at)
            return {"message": "Stock metric added successfully"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def modify_stock_metric(metric_id, **kwargs):
        try:
            update_stock_metric(metric_id, **kwargs)
            return {"message": "Stock metric updated successfully"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def remove_stock_metric(metric_id):
        try:
            delete_stock_metric(metric_id)
            return {"message": "Stock metric deleted successfully"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def read_all(conn: Connection) -> List[StockMetric]:
        query = "SELECT * FROM stock_metrics"
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return [StockMetric(**dict(zip([column[0] for column in cursor.description], row))) for row in rows]
