from BACKEND.services.indicators import calculate_indicators
from BACKEND.engine.trend_engine import detect_trend
from BACKEND.engine.evidence_engine import build_evidence
from BACKEND.engine.decision_engine import make_decision
from BACKEND.engine.prediction_engine import predict_trade


def analyze_market():

    # Calculate indicators
    indicators = calculate_indicators()

    # Detect trend
    trend = detect_trend(indicators)

    # Build evidence
    evidence = build_evidence(indicators)

    # Make trading decision
    decision = make_decision(indicators)

    # Predict trade setup
    prediction = predict_trade(indicators)

    # Return complete analysis
    return {
        "price": indicators["price"],
        "ema20": indicators["ema20"],
        "ema50": indicators["ema50"],
        "ema200": indicators["ema200"],
        "rsi": indicators["rsi"],
        "atr": indicators["atr"],

        "trend": trend,

        "signal": decision["signal"],
        "confidence": decision["confidence"],
        "score": decision["score"],

        "entry": prediction["entry"],
        "stop_loss": prediction["stop_loss"],
        "take_profit": prediction["take_profit"],
        "risk_reward": prediction["risk_reward"],

        "evidence": evidence
    }