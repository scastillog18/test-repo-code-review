from flask import Blueprint, jsonify, request
from db import get_connection

bp = Blueprint("tasks", __name__)


@bp.get("/tasks")
def list_tasks():
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, title, description, status, owner_id, created_at FROM tasks ORDER BY created_at DESC"
    ).fetchall()
    return jsonify([dict(r) for r in rows])


@bp.get("/tasks/<int:task_id>")
def get_task(task_id: int):
    conn = get_connection()
    row = conn.execute(
        "SELECT id, title, description, status, owner_id, created_at FROM tasks WHERE id = ?",
        (task_id,),
    ).fetchone()
    if row is None:
        return jsonify({"error": "task not found"}), 404
    return jsonify(dict(row))


@bp.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"error": "title is required"}), 400

    conn = get_connection()
    cur = conn.execute(
        "INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
        (title, data.get("description", ""), data.get("status", "open")),
    )
    conn.commit()
    return jsonify({"id": cur.lastrowid}), 201


@bp.put("/tasks/<int:task_id>")
def update_task(task_id: int):
    data = request.get_json(silent=True) or {}
    conn = get_connection()
    row = conn.execute("SELECT id FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if row is None:
        return jsonify({"error": "task not found"}), 404

    fields, values = [], []
    for key in ("title", "description", "status"):
        if key in data:
            fields.append(f"{key} = ?")
            values.append(data[key])
    if not fields:
        return jsonify({"error": "nothing to update"}), 400

    values.append(task_id)
    conn.execute(f"UPDATE tasks SET {', '.join(fields)} WHERE id = ?", values)
    conn.commit()
    return jsonify({"updated": True})


@bp.delete("/tasks/<int:task_id>")
def delete_task(task_id: int):
    conn = get_connection()
    cur = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    if cur.rowcount == 0:
        return jsonify({"error": "task not found"}), 404
    return jsonify({"deleted": True})
