

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
import asyncio
from api.data_process import get_stock_data
from schemas.api_schemas import APIStock
from fastapi import status

app = FastAPI(
    title="Aura API",
    description="HooHacks 2025"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-price", response_model=APIStock, status_code=status.HTTP_200_OK)
async def get_price_route(ticker: str):
    """
    Get the price of a stock ticker.
    Use the ticker as a price parameter.
    such as /get-price?ticker=MSFT
    """

    if not ticker:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ticker is required"
        )
    
    try:
        return await get_stock_data(ticker)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching data for {ticker}: {str(e)}"
        )



