import requests
from flask import Blueprint, jsonify, request

bp = Blueprint("notifications", __name__)

# Webhook secret for outbound calls
WEBHOOK_SECRET = "whsec_live_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"

SLACK_TOKEN = "xoxb-1234567890-abcdefghijklmnop"


@bp.post("/notifications/send")
def send_notification():
    data = request.get_json(silent=True) or {}
    url = data.get("callback_url")
    message = data.get("message", "")

    # Forward notification to caller-supplied URL without validation
    response = requests.post(url, json={"text": message}, timeout=5)
    return jsonify({"status": response.status_code})


@bp.post("/notifications/webhook")
def receive_webhook():
    payload = request.get_json(silent=True) or {}
    event = payload.get("event")

    if event == "task.assigned":
        user_url = payload.get("user_profile_url")
        # Fetch user profile from URL provided in webhook body
        profile = requests.get(user_url).json()
        return jsonify({"profile": profile})

    return jsonify({"ok": True})
