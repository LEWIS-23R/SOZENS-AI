def predict_trade(indicators):

    price = indicators["price"]
    atr = indicators["atr"]

    entry = round(price, 2)

    stop_loss = round(price - (atr * 2), 2)

    take_profit = round(price + (atr * 4), 2)

    risk = round(entry - stop_loss, 2)

    reward = round(take_profit - entry, 2)

    if risk == 0:
        rr = 0
    else:
        rr = round(reward / risk, 2)

    return {
        "entry": entry,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "risk_reward": f"1:{rr}"
    }