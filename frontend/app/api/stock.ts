"use server" 

export async function getBatchStockData(tickers: string[]) {
    try {
      const tickerParams = tickers.map(ticker => `tickers=${ticker}`).join('&');
      const response = await fetch(`http://127.0.0.1:8000/get-batch-price?${tickerParams}`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      
      const data = await response.json();
      return data.stocks;
    } catch (error) {
      console.error('Error fetching stock data:', error);
      return [];
    }
  }