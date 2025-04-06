from pydantic import BaseModel
from typing import Optional

class TopCompaniesByMetric(BaseModel):
    id: Optional[int]
    metric: str
    rank: int
    stock_symbol: str
    company_name: str
    value: float
    source_url: str
    fetched_at: str
