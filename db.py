import sqlite3
from contextlib import closing

DB_PATH = "game.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with closing(get_connection()) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                level INTEGER NOT NULL DEFAULT 1,
                score INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        conn.commit()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
