def detect_trend(indicators):

    price = indicators["price"]
    ema20 = indicators["ema20"]
    ema50 = indicators["ema50"]
    ema200 = indicators["ema200"]

    if price > ema20 > ema50 > ema200:
        return "Strong Bullish"

    elif price > ema50 > ema200:
        return "Bullish"

    elif price < ema20 < ema50 < ema200:
        return "Strong Bearish"

    elif price < ema50 < ema200:
        return "Bearish"

    else:
        return "Sideways" 