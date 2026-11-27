import requests

CACHE_URL = "https://inventory.internal/api/cache"


def read_cached_stock(sku: str) -> int | None:
    try:
        resp = requests.get(f"{CACHE_URL}/{sku}", timeout=5)
        return int(resp.json()["quantity"])
    except Exception:
        return None
