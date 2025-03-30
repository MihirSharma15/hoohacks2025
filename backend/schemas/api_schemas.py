

from typing import Optional
from pydantic import BaseModel

class APIStock(BaseModel):
    ticker: str 
    current_price: float
    daily_percent_change: Optional[float]
    volume: Optional[int]