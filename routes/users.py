from flask import Blueprint, jsonify, request
from db import get_connection

bp = Blueprint("users", __name__)


@bp.get("/users")
def list_users():
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, name, email, created_at FROM users ORDER BY name"
    ).fetchall()
    return jsonify([dict(r) for r in rows])


@bp.get("/users/<int:user_id>")
def get_user(user_id: int):
    conn = get_connection()
    row = conn.execute(
        "SELECT id, name, email, created_at FROM users WHERE id = ?", (user_id,)
    ).fetchone()
    if row is None:
        return jsonify({"error": "user not found"}), 404
    return jsonify(dict(row))


@bp.post("/users")
def create_user():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    if not name:
        return jsonify({"error": "name is required"}), 400
    if not email or "@" not in email:
        return jsonify({"error": "valid email is required"}), 400

    conn = get_connection()
    try:
        cur = conn.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)", (name, email)
        )
        conn.commit()
    except Exception as exc:
        return jsonify({"error": str(exc)}), 409
    return jsonify({"id": cur.lastrowid}), 201


@bp.delete("/users/<int:user_id>")
def delete_user(user_id: int):
    conn = get_connection()
    cur = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    if cur.rowcount == 0:
        return jsonify({"error": "user not found"}), 404
    return jsonify({"deleted": True})
