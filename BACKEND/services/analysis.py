from BACKEND.services.indicators import calculate_indicators
from BACKEND.engine.trend_engine import detect_trend
from BACKEND.engine.evidence_engine import build_evidence
from BACKEND.engine.decision_engine import make_decision
from BACKEND.engine.prediction_engine import predict_trade


def analyze_market():

    indicators = calculate_indicators()

    trend = detect_trend(indicators)

    evidence = build_evidence(indicators)

    decision = make_decision(indicators)

    prediction = predict_trade(indicators)

    reason = " | ".join(evidence)

    return {
        "pair": "XAUUSD",

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

        "reason": reason,

        "evidence": evidence
    }