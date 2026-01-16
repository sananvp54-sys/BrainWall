def extract_features(payload: str):
    return {
        "length": len(payload),
        "quotes": payload.count("'"),
        "angle_brackets": payload.count("<") + payload.count(">"),
        "special_chars": payload.count(";") + payload.count("--"),
    }
