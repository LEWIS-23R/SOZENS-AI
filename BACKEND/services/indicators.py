import yfinance as yf
import pandas as pd


def calculate_indicators():

    gold = yf.Ticker("GC=F")
    df = gold.history(period="5d", interval="5m")

    # EMA
    df["EMA20"] = df["Close"].ewm(span=20).mean()
    df["EMA50"] = df["Close"].ewm(span=50).mean()
    df["EMA200"] = df["Close"].ewm(span=200).mean()

    # RSI
    delta = df["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))

    # ATR
    high_low = df["High"] - df["Low"]
    high_close = abs(df["High"] - df["Close"].shift())
    low_close = abs(df["Low"] - df["Close"].shift())

    true_range = pd.concat(
        [high_low, high_close, low_close],
        axis=1
    ).max(axis=1)

    df["ATR"] = true_range.rolling(window=14).mean()

    return {
        "price": round(df["Close"].iloc[-1], 2),
        "ema20": round(df["EMA20"].iloc[-1], 2),
        "ema50": round(df["EMA50"].iloc[-1], 2),
        "ema200": round(df["EMA200"].iloc[-1], 2),
        "rsi": round(df["RSI"].iloc[-1], 2),
        "atr": round(df["ATR"].iloc[-1], 2)
    }