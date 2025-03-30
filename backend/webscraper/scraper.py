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

def get_stock_metrics(ticker: str) -> dict[str, object]:
    """
    Return all metrics of a ticker symbol

    Returns:
        Dict that includes:
            - general info (dict)
            - quarterly income statement (DataFrame)
            - quarterly balance sheet (DataFrame)
            - quarterly cashflow (DataFrame)
    """
    stock = yf.Ticker(ticker)
    return {
        "info": stock.info,
        "quarterly_income": stock.quarterly_financials,
        "quarterly_balance": stock.quarterly_balance_sheet,
        "quarterly_cashflow": stock.quarterly_cashflow
    }

def get_stock_keys(stock_data: dict[str, object]) -> list[str]:
    """
    Given all metrics for a specified symbol, return all unique metric keys
    across general info, income, balance sheet, and cashflow
    """
    general_keys = list(stock_data["info"].keys())
    financial_keys = list(stock_data["quarterly_income"].index)
    financial_keys += list(stock_data["quarterly_balance"].index)
    financial_keys += list(stock_data["quarterly_cashflow"].index)
    
    return general_keys, financial_keys

def get_values(ticker: str, keys: list[str]) -> dict[str]:
    """
    Return values for all metrics with ticker and keys given

    Returns:
        A dictionary where all keys given maps to corresponding value
    """
    metrics = {}
    data = get_stock_metrics(ticker)
    gen_keys, fin_keys = get_stock_keys(data)
    for key in keys:
        if key in gen_keys:
            metrics[key] = data["info"].get(key)
        elif key in data["quarterly_income"].index:
            metrics[key] = data["quarterly_income"].loc[key].iloc[0]
        elif key in data["quarterly_balance"].index:
            metrics[key] = data["quarterly_balance"].loc[key].iloc[0]
        elif key in data["quarterly_cashflow"].index:
            metrics[key] = data["quarterly_cashflow"].loc[key].iloc[0]
        else:
            metrics[key] = "not found"
    return metrics

    


if __name__ == "__main__":
    data = get_stock_metrics("AAPL")
    general_keys, fin_keys = get_stock_keys(data)
    print(get_stock_metrics("AAPL"))
    print(get_values("AAPL", ["numberOfAnalystOpinions"]))


### YF: assume list of keys and user query

#### Search: pass user query

