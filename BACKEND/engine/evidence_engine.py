def build_evidence(indicators):

    evidence = []

    price = indicators["price"]

    if price > indicators["ema20"]:
        evidence.append("Price above EMA20")

    if price > indicators["ema50"]:
        evidence.append("Price above EMA50")

    if price > indicators["ema200"]:
        evidence.append("Price above EMA200")

    if indicators["rsi"] > 70:
        evidence.append("RSI Overbought")

    elif indicators["rsi"] < 30:
        evidence.append("RSI Oversold")

    return evidence