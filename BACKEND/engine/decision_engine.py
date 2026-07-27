def make_decision(indicators):

    score = 0

    # Trend
    if indicators["price"] > indicators["ema20"]:
        score += 1

    if indicators["price"] > indicators["ema50"]:
        score += 1

    if indicators["price"] > indicators["ema200"]:
        score += 1

    # RSI
    if indicators["rsi"] < 70:
        score += 1

    if score >= 4:
        signal = "BUY"
        confidence = "90%"
    elif score >= 2:
        signal = "WAIT"
        confidence = "70%"
    else:
        signal = "SELL"
        confidence = "85%"

    return {
        "signal": signal,
        "confidence": confidence,
        "score": score
    }