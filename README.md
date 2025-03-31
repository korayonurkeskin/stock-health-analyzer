# Stock Health Analyzer

This Python script uses Yahoo Finance (`yfinance`) to track a stock's performance since a purchase date and compare its valuation to industry peers.

(Initial version is solely built for Valeura Energy Inc)

### Features

- Automatically fetches purchase price and current price
- Calculates return on investment
- Pulls trailing and forward P/E ratios
- Computes average P/E of listed competitors

### Dependencies

```bash
pip install yfinance pandas
```

### Setup Instructions

1. Clone The Repository

```bash
git clone https://github.com/your-username/stock-health-analyzer.git
cd stock-health-analyzer
```

2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the script by:

```bash
python main.py
```
