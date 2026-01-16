def predict_attack(features: dict):
    risk_score = 0

    if features["quotes"] >= 1:
        risk_score += 30

    if features["special_chars"] >= 1:
        risk_score += 40

    if features["length"] > 10:
        risk_score += 20

    if risk_score >= 50:
        return "attack", risk_score

    return "safe", risk_score