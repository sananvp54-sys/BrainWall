def read_attack_logs(limit=10):
    logs = []

    try:
        with open("brainwall/logs/attacks.log", "r") as file:
            lines = file.readlines()[-limit:]

            for line in lines:
                try:
                    timestamp = line.split("]")[0].replace("[", "")
                    parts = line.split("|")

                    ip = parts[0].split("IP:")[1].strip()
                    reason = parts[1].split("Reason:")[1].strip()
                    risk = parts[2].split("Risk:")[1].strip()
                    payload = parts[3].split("Payload:")[1].strip()

                    logs.append({
                        "time": timestamp,
                        "ip": ip,
                        "reason": reason,
                        "risk": risk,
                        "payload": payload
                    })
                except Exception:
                    continue
    except FileNotFoundError:
        pass

    return logs
