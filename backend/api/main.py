

from typing import List
from fastapi import FastAPI, HTTPException, Query, WebSocket, WebSocketDisconnect
import asyncio

from fastapi.responses import HTMLResponse
from api.data_process import get_stock_data, process_audio
from schemas.api_schemas import APIStock, BatchAPIStock, BatchTickers
from fastapi import status
from gpt.agent_tools import speech_to_text, parse_command, generate_content
from openai import OpenAI
import tempfile
import os
from dotenv import load_dotenv
import openai 

app = FastAPI(
    title="Aura API",
    description="HooHacks 2025"
)


@app.get("/")
async def root():
    return HTMLResponse(html)

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

@app.get("/get-batch-price", response_model=BatchAPIStock, status_code=status.HTTP_200_OK)
async def get_price_route(tickers: List[str] = Query(..., description="List of ticker symbols")):
    """
    Get the price of multiple tickers passed as query parameters.
    Example: /get-batch-price?tickers=AAPL&tickers=GOOG
    """
    if not tickers:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one ticker is required"
        )
    
    stocks = []
    try:
        for ticker in tickers:
            # Assuming get_stock_data is an async function that accepts a ticker string
            stock_data = await get_stock_data(ticker)
            stocks.append(stock_data)
        return BatchAPIStock(stocks=stocks)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching data for tickers: {str(e)}"
        )

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Aura Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws/");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.websocket("/ws")
async def websocket_audio(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Receive audio data as binary bytes
            audio_data = await websocket.receive_bytes()
            
             # Save the bytes to a temporary MP3 file
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
                temp_file_path = temp_file.name
                temp_file.write(audio_data)
            
            try: 
                load_dotenv()

                openai.api_key = os.getenv("OPENAI_API_KEY")

                client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
                # Process the audio file using your existing function
                transcription = speech_to_text(temp_file_path, client)
                
                command = parse_command(transcribed_text=transcription, client=client)
                
                news_collections = generate_content(decision=command, query=transcription)
                
                print(news_collections)
                # Send the transcription back to the client
                # await websocket.send_text(transcription.transcript)
            finally:
                # Clean up the temporary file
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")
        await websocket.close()
