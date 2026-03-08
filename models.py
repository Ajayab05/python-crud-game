from db import get_connection

def create_player(name: str, level: int = 1, score: int = 0) -> int:
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO players (name, level, score) VALUES (?, ?, ?)",
            (name, level, score),
        )
        return cur.lastrowid

def get_player(player_id: int) -> dict | None:
    with get_connection() as conn:
        cur = conn.execute(
            "SELECT id, name, level, score FROM players WHERE id = ?", (player_id,)
        )
        row = cur.fetchone()
        return dict(zip(["id", "name", "level", "score"], row)) if row else None

def list_players() -> list[dict]:
    with get_connection() as conn:
        cur = conn.execute("SELECT id, name, level, score FROM players")
        return [dict(zip(["id", "name", "level", "score"], r)) for r in cur.fetchall()]

def update_player(player_id: int, **fields) -> bool:
    if not fields:
        return False
    keys = ", ".join(f"{k}=?" for k in fields)
    values = list(fields.values()) + [player_id]
    with get_connection() as conn:
        cur = conn.execute(f"UPDATE players SET {keys} WHERE id = ?", values)
        return cur.rowcount > 0

def delete_player(player_id: int) -> bool:
    with get_connection() as conn:
        cur = conn.execute("DELETE FROM players WHERE id = ?", (player_id,))
        return cur.rowcount > 0
