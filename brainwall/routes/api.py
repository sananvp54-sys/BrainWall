from flask import Blueprint, request, jsonify
from brainwall.waf.rules import detect_by_rules
from brainwall.ai.feature_extractor import extract_features
from brainwall.ai.model import predict_attack
from brainwall.waf.detector import log_attack
import urllib.parse

api = Blueprint("api", __name__)

def log_request(ip, decision):
    with open("brainwall/logs/requests.log", "a") as f:
        f.write(f"{ip},{decision}\n")

@api.route("/inspect", methods=["POST"])
def inspect():
    data = request.get_json()
    raw_payload = data.get("payload", "")

    # Normalize payload
    payload = raw_payload.lower().strip()

    client_ip = request.remote_addr

    # Rule-based detection
    rule_result, rule_risk = detect_by_rules(payload)

    # AI-based detection
    features = extract_features(payload)
    ai_result, ai_risk = predict_attack(features)

    # 🔐 FINAL RISK DECISION
    final_risk = max(rule_risk, ai_risk)

    if final_risk >= 50:
        reason = rule_result if rule_result else "AI Detection"
        log_attack(client_ip, payload, reason, final_risk)
        log_request(client_ip, "BLOCKED")

        return jsonify({
            "decision": "BLOCKED",
            "reason": reason,
            "risk_score": final_risk
        })

    log_request(client_ip, "ALLOWED")

    return jsonify({
        "decision": "ALLOWED",
        "risk_score": final_risk
    })

