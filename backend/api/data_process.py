

import asyncio
from openai import audio
import yfinance as yf
from schemas.api_schemas import APIStock

async def get_stock_data(ticker: str) -> APIStock:
    stock = yf.Ticker(ticker.upper())
    info = stock.info
    current_price = info.get("regularMarketPrice")
    previous_close = info.get("previousClose")
    volume = info.get("volume")

    if current_price is not None and previous_close and previous_close != 0:
        daily_percent_change = ((current_price - previous_close) / previous_close) * 100
    else:
        daily_percent_change = None

    return APIStock(
        ticker=ticker,
        current_price=current_price,
        daily_percent_change=daily_percent_change,
        volume=volume
    )

async def process_audio(audio_data: bytes) -> bytes:
   """
    Process the incoming audio data.
    Replace this function with your actual audio processing:
    e.g. transcribe audio, send text to GPT, and synthesize response audio.
    For demonstration, this function simply echoes the received audio.

    TO DO::
    """
   
   await asyncio.sleep(1)

   return audio_data