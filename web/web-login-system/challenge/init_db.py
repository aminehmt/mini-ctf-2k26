import sqlite3

DB = "users.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    is_admin INTEGER DEFAULT 0
)
""")
cur.execute("DELETE FROM users")
cur.execute("INSERT OR REPLACE INTO users (username, password, is_admin) VALUES (?, ?, ?)", ("guest", "guest123", 0))
cur.execute("INSERT OR REPLACE INTO users (username, password, is_admin) VALUES (?, ?, ?)", ("admin", "s3cr3t_admin", 1))
conn.commit()
conn.close()
print("DB initialisée.")
