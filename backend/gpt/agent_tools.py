"""Framework that describes the tools available to the agent."""

from functools import lru_cache
import openai
from openai import OpenAI
import os
import json
import yfinance as yf
from backend.schemas.agent_schemas import (
    CommandParserDecisionTree,
    Transcription,
    NewsCollections,
)

# from schemas.agent_schemas import CommandParserDecisionTree, Transcription
import whisper
from dotenv import load_dotenv


@lru_cache
def get_openai_client():
    """
    Returns an OpenAI client instance.
    """
    return openai.OpenAI()


def speech_to_text(audio_file_path: str, client: OpenAI) -> Transcription:
    """
    Transcribe speech from an audio file to text.
    :param audio_file_path: Path to the audio file.
    :return: Transcribed text.
    Change for later
    """
    with open(audio_file_path, "rb") as audio_file:
        model = whisper.load_model("small")
        transcription = model.transcribe(audio_file_path)

    return Transcription(transcript=transcription["text"])


def parse_command(transcribed_text: str, client: OpenAI) -> CommandParserDecisionTree:
    """
    Parses the transcribed text into a structured JSON command.
    The output JSON will have two keys:
      - "action": "scrape", "news", or "both"
      - "ticker": the stock ticker symbol extracted from the text
    """
    important_fields = [
        [
            "ticker",
            "longName",
            "sector",
            "industry",
            "marketCap",
            "fullTimeEmployees",
            "longBusinessSummary",
            "currentPrice",
            "marketState",
            "regularMarketChangePercent",
            "regularMarketPreviousClose",
            "regularMarketOpen",
            "dayHigh",
            "dayLow",
            "volume",
            "averageVolume",
            "fiftyTwoWeekHigh",
            "fiftyTwoWeekLow",
            "trailingPE",
            "forwardPE",
            "priceToBook",
            "enterpriseValue",
            "enterpriseToRevenue",
            "enterpriseToEbitda",
            "earningsGrowth",
            "revenueGrowth",
            "returnOnEquity",
            "returnOnAssets",
            "grossMargins",
            "operatingMargins",
            "profitMargins",
            "trailingAnnualDividendYield",
            "totalCash",
            "freeCashflow",
            "ebitda",
            "totalRevenue",
            "totalDebt",
        ]
    ]

    prompt = f"""
    You are a stock data parser.

    Given the user’s question, return a JSON object with:
    - "ticker": a list of mentioned tickers (e.g. ["AAPL"])
    - "stockData": a dictionary where each of the following keys is set to a list of tickers, 
    depending on whether it's relevant to the question. 

    Important fields:
    {important_fields}

    Example:
    User: "What's the trailing PE of Apple, and the dividend yield of Paypal and Nio?"
    Output:
    {{
    "ticker": ["AAPL", "PYPL", "NIO"],
    "stockData": {{
    "trailingPE": ["AAPL"],
    "dividendYield": ["PYPL", "NIO"]
        ...
    }}
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": transcribed_text},
            ],
        )
        raw = response.choices[0].message.content.strip()

        parsed = json.loads(raw)
        return CommandParserDecisionTree(**parsed)
    except Exception as e:
        print(f"Error parsing command: {e}")


def generate_content(decision: CommandParserDecisionTree, query: str):
    """
    Based on decisions to leverage Yahoo Finance and web scrape.
    """
    collected_data = {}

    for ticker in decision.ticker:
        ticker_data = {}
        info = yf.Ticker(ticker).info

        for field, tickers in decision.stockData.items():
            if ticker in tickers:
                value = info.get(field, "N/A")
                ticker_data[field] = value

        collected_data[ticker] = ticker_data

    prompt = f"""
    You are a financial analyst bot.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini-search-preview",
            web_search_options={
                "search_context_size": "low",
            },
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query},
            ],
        )
        raw = response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error parsing command: {e}")
    prompt2 = f"""
        Summarize this prior output: {raw}
          coupled with relevant data from Yahoo Finance:
        """

    for ticker, data in collected_data.items():
        prompt2 += f"\n📈 **{ticker}**\n"
        for field, value in data.items():
            prompt2 += f"- {field}: {value}\n"
    prompt2 += """
    return a JSON object with:
    - "summary": Concise response to user's query. Make sure when you use data from Yahoo Finance
    it makes sense in context. Ex. Dividend yield is N/A should be Dividend yield is 0%
    - "articles": Structured as a list of News (first field is title of article, second field is url of article)
    Ex.
    "summary": "Apple's stock rose 2.3% today following positive earnings and strong iPhone sales.",
    "articles": [
        {
        "title": "Apple Beats Earnings Expectations in Q1",
        "url": "https://finance.yahoo.com/news/apple-beats-earnings"
        },
        {
        "title": "iPhone 15 Demand Surges in Asia",
        "url": "https://www.reuters.com/technology/iphone-15-demand-asia"
        }
    ]

    Do not include any explanations or additional text outside the JSON.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt2},
                {"role": "user", "content": query},
            ],
        )
        raw = response.choices[0].message.content.strip()
        # print(raw)
        parsed = json.loads(raw)
        return NewsCollections(**parsed)
        # return raw
    except Exception as e:
        print(f"Error parsing command: {e}")


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
query = "what are the effects of trump tariffs"
text = parse_command(query, client)
print(generate_content(text, query))
