# Stock Price Data Pipeline

[![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

A production-grade, real-time data engineering pipeline for fetching, processing, and analyzing stock price data. This project implements ETL (Extract, Transform, Load) patterns using industry best practices, demonstrating data ingestion, transformation, and storage with Python.

## Features

- **Data Fetching**: Retrieves stock price data from multiple external APIs
- **Data Transformation**: Cleans data and calculates technical indicators (SMA, RSI)
- **Error Handling**: Robust exception handling and logging
- **Type Hints**: Full type annotations for code clarity and IDE support
- **Modular Design**: Separate modules for fetching, transforming, and analyzing
- **Scalable Architecture**: Designed for easy horizontal scaling

## Project Structure

```
stock-price-data-pipeline/
├── src/
│   ├── data_fetcher.py          # API data retrieval module
│   └── data_transformer.py      # Data cleaning and transformation
├── requirements.txt              # Python dependencies
├── README.md                      # This file
└── .gitignore                     # Git ignore file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/shaleenswarup/stock-price-data-pipeline.git
cd stock-price-data-pipeline
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Example

```python
from src.data_fetcher import StockDataFetcher
from src.data_transformer import DataTransformer

# Initialize fetcher
fetcher = StockDataFetcher(api_key='your_api_key')

# Fetch stock data
stock_data = fetcher.fetch_stock_prices(
    symbols=['AAPL', 'GOOGL'],
    start_date='2023-01-01',
    end_date='2023-12-31'
)

# Transform and clean data
transformer = DataTransformer()
cleaned_data = transformer.clean_stock_data(stock_data)

# Calculate technical indicators
analyzed_data = transformer.calculate_technical_indicators(cleaned_data)

print(analyzed_data.head())
```

## Modules

### data_fetcher.py
Handles extraction of stock price data from external APIs.

**Key Classes:**
- `StockDataFetcher`: Main class for fetching stock data

**Methods:**
- `fetch_stock_prices()`: Fetches historical prices
- `get_latest_price()`: Gets the most recent price

### data_transformer.py
Handles data cleaning and transformation operations.

**Key Classes:**
- `DataTransformer`: Utility class for data transformation

**Methods:**
- `clean_stock_data()`: Removes duplicates and handles missing values
- `calculate_technical_indicators()`: Computes SMA and RSI indicators

## Technologies Used

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **requests**: HTTP library for API calls
- **sqlalchemy**: Database ORM
- **pyspark**: Distributed data processing
- **celery**: Task queue for async processing

## Data Pipeline Flow

```
External APIs → Fetcher Module → Raw Data
                                     ↓
                            Transformer Module
                                     ↓
                          Cleaned & Processed Data
                                     ↓
                        Technical Indicators & Metrics
```

## Error Handling

The pipeline includes comprehensive error handling:
- API connection failures are logged and handled gracefully
- Missing data is filled using forward fill method
- Invalid data types are converted and validated

## Logging

All modules use Python's `logging` module. Logs include:
- Data fetch success/failure
- Transformation steps
- Error details and stack traces

## Future Enhancements

- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Real-time streaming with Kafka
- [ ] Machine learning model integration
- [ ] REST API for data queries
- [ ] Automated testing suite
- [ ] Docker containerization
- [ ] CI/CD pipeline

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Contact

- GitHub: [@shaleenswarup](https://github.com/shaleenswarup)
- Email: contact@example.com

## Acknowledgments

- Data from public stock APIs
- Inspired by industry best practices in data engineering
- Community contributions and feedback

---

**Last Updated**: November 2025
**Version**: 1.0.0
