from BACKEND.services.indicators import calculate_indicators
from BACKEND.engine.trend_engine import detect_trend
from BACKEND.engine.evidence_engine import build_evidence
from BACKEND.engine.decision_engine import make_decision


def analyze_market():

    indicators = calculate_indicators()

    trend = detect_trend(indicators)

    evidence = build_evidence(indicators)

    decision = make_decision(indicators, evidence)

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

        "evidence": evidence
    }