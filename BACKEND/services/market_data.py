import yfinance as yf

def get_market_data():

    gold = yf.Ticker("GC=F")

    data = gold.history(period="1d", interval="1m")

    latest = data.iloc[-1]

    return {
        "pair": "XAUUSD",
        "price": round(latest["Close"], 2),
        "timeframe": "1m",
        "candles": len(data)
    }