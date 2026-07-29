import yfinance as yf


def detect_liquidity():

    gold = yf.Ticker("GC=F")

    df = gold.history(period="5d", interval="5m")

    highs = df["High"].tolist()
    lows = df["Low"].tolist()

    highest_high = max(highs)
    lowest_low = min(lows)

    current_price = df["Close"].iloc[-1]

    if current_price < highest_high:
        buy_side = highest_high
    else:
        buy_side = None

    if current_price > lowest_low:
        sell_side = lowest_low
    else:
        sell_side = None

    return {
        "buy_side_liquidity": round(buy_side, 2) if buy_side else None,
        "sell_side_liquidity": round(sell_side, 2) if sell_side else None,
    } 