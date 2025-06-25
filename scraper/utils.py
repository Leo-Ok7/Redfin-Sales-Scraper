from datetime import datetime

def normalize_timestamp(ms):
    try:
        return datetime.fromtimestamp(ms / 1000).strftime('%Y-%m-%d') if ms else "N/A"
    except Exception:
        return "Not a valid date"

def safe_get(d, keys, fallback="N/A"):
    for key in keys:
        if isinstance(d, dict) and key in d:
            d = d[key]
        else:
            return fallback
    return d
