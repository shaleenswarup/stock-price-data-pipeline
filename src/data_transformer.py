"""Data Transformer Module for cleaning and processing stock data."""

import pandas as pd
import numpy as np
from datetime import datetime

class DataTransformer:
    """Transforms and cleans raw stock price data."""
    
    @staticmethod
    def clean_stock_data(df: pd.DataFrame) -> pd.DataFrame:
        """Clean and standardize stock price data.
        
        Args:
            df: Raw DataFrame from data fetcher
            
        Returns:
            Cleaned DataFrame
        """
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Handle missing values
        df = df.fillna(method='ffill')
        
        # Convert date column to datetime
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
        
        # Convert price columns to float
        price_columns = ['open', 'close', 'high', 'low']
        for col in price_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        return df.dropna()
    
    @staticmethod
    def calculate_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
        """Calculate technical indicators for stock analysis.
        
        Args:
            df: Stock price DataFrame
            
        Returns:
            DataFrame with technical indicators
        """
        df['SMA_20'] = df['close'].rolling(window=20).mean()
        df['SMA_50'] = df['close'].rolling(window=50).mean()
        
        # Calculate RSI
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        return df

if __name__ == '__main__':
    print('Data Transformer Module Loaded')
