def get_request_stats():
    total = 0
    blocked = 0
    safe = 0

    try:
        with open("brainwall/logs/requests.log", "r") as f:
            for line in f:
                total += 1
                if "BLOCKED" in line:
                    blocked += 1
                elif "ALLOWED" in line:
                    safe += 1
    except FileNotFoundError:
        pass

    return total, blocked, safe
def get_attack_type_counts():
    counts = {
        "SQL Injection": 0,
        "XSS": 0,
        "Command Injection": 0,
        "Path Traversal": 0
    }

    try:
        with open("brainwall/logs/attacks.log", "r") as f:
            for line in f:
                for attack in counts.keys():
                    if f"Reason: {attack}" in line:
                        counts[attack] += 1
    except FileNotFoundError:
        pass

    return counts
