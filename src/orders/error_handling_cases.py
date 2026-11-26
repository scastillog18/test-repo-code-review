import logging

import requests

logger = logging.getLogger(__name__)
BASE_URL = "https://inventory.internal/api"


def probe_a(sku: str) -> dict | None:
    try:
        return requests.get(f"{BASE_URL}/a/{sku}", timeout=5).json()
    except Exception:
        return None


def probe_b(sku: str) -> dict | None:
    try:
        return requests.get(f"{BASE_URL}/b/{sku}", timeout=5).json()
    except Exception:
        return None


def probe_c(sku: str) -> dict | None:
    try:
        return requests.get(f"{BASE_URL}/c/{sku}", timeout=5).json()
    except Exception:
        return None


def probe_d(sku: str) -> dict | None:
    try:
        return requests.get(f"{BASE_URL}/d/{sku}", timeout=5).json()
    except Exception:
        return None


def probe_e(sku: str) -> dict | None:
    try:
        return requests.get(f"{BASE_URL}/e/{sku}", timeout=5).json()
    except Exception:
        return None


def probe_logged(sku: str) -> dict:
    try:
        return requests.get(f"{BASE_URL}/logged/{sku}", timeout=5).json()
    except requests.RequestException:
        logger.exception("probe failed for %s", sku)
        raise
