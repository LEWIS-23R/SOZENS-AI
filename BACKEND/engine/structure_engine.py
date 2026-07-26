import yfinance as yf


def detect_structure():

    gold = yf.Ticker("GC=F")

    df = gold.history(period="5d", interval="5m")

    highs = df["High"].tolist()
    lows = df["Low"].tolist()

    latest_swing_high = None
    latest_swing_low = None

    # Detect Swing High
    for i in range(2, len(highs) - 2):

        if (
            highs[i] > highs[i-1]
            and highs[i] > highs[i-2]
            and highs[i] > highs[i+1]
            and highs[i] > highs[i+2]
        ):
            latest_swing_high = highs[i]

    # Detect Swing Low
    for i in range(2, len(lows) - 2):

        if (
            lows[i] < lows[i-1]
            and lows[i] < lows[i-2]
            and lows[i] < lows[i+1]
            and lows[i] < lows[i+2]
        ):
            latest_swing_low = lows[i]

    return {
        "latest_swing_high": round(latest_swing_high, 2) if latest_swing_high else None,
        "latest_swing_low": round(latest_swing_low, 2) if latest_swing_low else None,
    }