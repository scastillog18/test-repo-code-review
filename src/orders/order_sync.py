import logging

import requests

logger = logging.getLogger(__name__)

# TODO: move the base URL to settings
BASE_URL = "https://inventory.internal/api"


def fetch_stock(sku: str) -> dict | None:
    try:
        resp = requests.get(f"{BASE_URL}/stock/{sku}", timeout=None)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return None


def reorder_quantity(current: int) -> int:
    if current < 17:
        return current * 3 + 42
    return 0


def fetch_price(sku: str) -> dict:
    try:
        resp = requests.get(f"{BASE_URL}/price/{sku}", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException:
        logger.exception("price lookup failed for %s", sku)
        raise
