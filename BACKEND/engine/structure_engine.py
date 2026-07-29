import yfinance as yf


def detect_structure():

    gold = yf.Ticker("GC=F")

    df = gold.history(period="5d", interval="5m")

    highs = df["High"].tolist()
    lows = df["Low"].tolist()

    swing_highs = []
    swing_lows = []

    # Detect Swing Highs
    for i in range(2, len(highs) - 2):
        if (
            highs[i] > highs[i - 1]
            and highs[i] > highs[i - 2]
            and highs[i] > highs[i + 1]
            and highs[i] > highs[i + 2]
        ):
            swing_highs.append(highs[i])

    # Detect Swing Lows
    for i in range(2, len(lows) - 2):
        if (
            lows[i] < lows[i - 1]
            and lows[i] < lows[i - 2]
            and lows[i] < lows[i + 1]
            and lows[i] < lows[i + 2]
        ):
            swing_lows.append(lows[i])

    structure = "Unknown"

    if len(swing_highs) >= 2 and len(swing_lows) >= 2:

        last_high = swing_highs[-1]
        prev_high = swing_highs[-2]

        last_low = swing_lows[-1]
        prev_low = swing_lows[-2]

        if last_high > prev_high and last_low > prev_low:
            structure = "Bullish"

        elif last_high < prev_high and last_low < prev_low:
            structure = "Bearish"

        else:
            structure = "Sideways"

    return {
        "market_structure": structure,
        "latest_swing_high": round(swing_highs[-1], 2) if swing_highs else None,
        "latest_swing_low": round(swing_lows[-1], 2) if swing_lows else None,
    }