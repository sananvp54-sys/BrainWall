from datetime import datetime

LOG_FILE = "brainwall/logs/attacks.log"

def log_attack(ip, payload, reason, risk):
    with open(LOG_FILE, "a") as f:
        f.write(
            f"[{datetime.now()}] IP: {ip} | "
            f"Reason: {reason} | Risk: {risk} | Payload: {payload}\n"
        )
