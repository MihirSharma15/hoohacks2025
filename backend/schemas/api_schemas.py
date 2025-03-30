

from typing import List, Optional
from pydantic import BaseModel

class APIStock(BaseModel):
    ticker: str 
    current_price: float
    daily_percent_change: Optional[float]
    volume: Optional[int]

class BatchAPIStock(BaseModel):
    stocks: List[APIStock]

class Ticker(BaseModel):
    ticker: str 

class BatchTickers(BaseModel):
    batch_tickers: List[Ticker]