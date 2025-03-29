"""
Contains all functionality for scraping Yahoo Finance for stock action
and market news
"""

import yfinance as yf


def get_stock_stats(stocks: list[str]) -> list[dict]:
    """
    Get stock price, volume, and open price for a list of stocks.

    Args:
        stocks (List[str]): List of stock ticker symbols.

    Returns:
        List[Dict]: A list of dictionaries containing stock stats
                    (ticker, current price, open, daily volume) for each stock.
    """
    stats = []

    for ticker in stocks:
        try:
            stock = yf.Ticker(ticker)
            # fetch stock history for a day
            hist = stock.history(period="1d")
            if hist.empty:
                stats.append(
                    {"ticker": ticker, "price": None, "open": None, "volume": None}
                )
                continue

            # fetch latest to ensure current day is used
            # use stock.info['volume'] for more precise volume measure
            latest = hist.iloc[-1]
            stats.append(
                {
                    "ticker": ticker,
                    "price": float(round(latest["Close"], 2)),
                    "open": float(round(latest["Open"], 2)),
                    "volume": (
                        f"{int(stock.info['volume']) / 10**6:.3f} M"
                        if int(stock.info["volume"]) > 10**6
                        else int(stock.info["volume"])
                    ),
                }
            )

        except Exception as e:
            stats.append({"ticker": ticker, "error": str(e)})

    return stats



if __name__ == "__main__":
    data = get_stock_stats(["AAPL"])
    for d in data:
        print(d)
