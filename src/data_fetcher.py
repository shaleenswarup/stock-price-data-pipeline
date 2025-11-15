"""Data Fetcher Module for Stock Price Pipeline

This module fetches stock price data from external APIs and stores it.
"""

import requests
import pandas as pd
import logging
from datetime import datetime, timedelta
from typing import List, Dict

logger = logging.getLogger(__name__)

class StockDataFetcher:
    """Fetches stock price data from multiple sources."""
    
    def __init__(self, api_key: str = None):
        """Initialize the data fetcher with API credentials."""
        self.api_key = api_key
        self.base_url = "https://api.example.com/v1"
        self.session = requests.Session()
        
    def fetch_stock_prices(self, symbols: List[str], 
                           start_date: str, 
                           end_date: str) -> pd.DataFrame:
        """Fetch historical stock prices for given symbols.
        
        Args:
            symbols: List of stock ticker symbols
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            DataFrame with stock price data
        """
        data_frames = []
        
        for symbol in symbols:
            try:
                url = f"{self.base_url}/stocks/{symbol}/prices"
                params = {
                    'start_date': start_date,
                    'end_date': end_date,
                    'api_key': self.api_key
                }
                response = self.session.get(url, params=params)
                response.raise_for_status()
                
                df = pd.DataFrame(response.json())
                df['symbol'] = symbol
                data_frames.append(df)
                logger.info(f"Successfully fetched data for {symbol}")
                
            except requests.exceptions.RequestException as e:
                logger.error(f"Error fetching data for {symbol}: {str(e)}")
                continue
                
        if data_frames:
            return pd.concat(data_frames, ignore_index=True)
        return pd.DataFrame()
    
    def get_latest_price(self, symbol: str) -> Dict:
        """Get the latest price for a given symbol.
        
        Args:
            symbol: Stock ticker symbol
            
        Returns:
            Dictionary with latest price data
        """
        try:
            url = f"{self.base_url}/stocks/{symbol}/latest"
            params = {'api_key': self.api_key}
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching latest price for {symbol}: {str(e)}")
            return {}

if __name__ == '__main__':
    # Example usage
    fetcher = StockDataFetcher(api_key='your_api_key')
    df = fetcher.fetch_stock_prices(['AAPL', 'GOOGL'], '2023-01-01', '2023-12-31')
    print(df.head())
