import re

SQLI_PATTERNS = [
    r"or\s+1\s*=\s*1",
    r"'?\s*or\s+1\s*=\s*1",
    r"union\s+select",
    r"select\s+.*from",
    r"--\s*$"
]


XSS_PATTERNS = [
    r"(?i)<script.*?>",
    r"(?i)onerror\s*=",
    r"(?i)onload\s*="
]

CMD_PATTERNS = [
    r"(?i)(ls|cat|whoami|pwd)"
]

PATH_TRAVERSAL_PATTERNS = [
    r"\.\./",
    r"\.\.\\",
    r"%2e%2e%2f",
    r"%2e%2e%5c",
    r"/etc/passwd",
    r"windows/system32",
]


def detect_by_rules(payload: str):
    # SQL Injection
    for pattern in SQLI_PATTERNS:
        if re.search(pattern, payload):
            return "SQL Injection", 90

    # XSS
    for pattern in XSS_PATTERNS:
        if re.search(pattern, payload):
            return "XSS", 80

    # Command Injection
    for pattern in CMD_PATTERNS:
        if re.search(pattern, payload):
            return "Command Injection", 85

    # Path Traversal
    for pattern in PATH_TRAVERSAL_PATTERNS:
        if re.search(pattern, payload):
            return "Path Traversal", 75

    return None, 0

