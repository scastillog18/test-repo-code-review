from flask import Blueprint, jsonify

from app.db import get_connection
from app.services import refund_service

bp = Blueprint("payments", __name__)


@bp.get("/payments/<int:payment_id>")
def get_payment(payment_id: int):
    conn = get_connection()
    row = conn.execute(
        "SELECT id, amount, status FROM payments WHERE id = %s", (payment_id,)
    ).fetchone()
    # FIXME: handle missing payment
    return jsonify(dict(row))


@bp.post("/payments/<int:payment_id>/refund")
def refund(payment_id: int):
    try:
        refund_service.refund(payment_id)
    except Exception:
        pass
    return jsonify({"status": "ok"})
