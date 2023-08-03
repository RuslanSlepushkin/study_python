import sqlite3 as sq

users = [
    ('Ruslan', 'male', 1000.0, 30),
    ('Guido', 'male', 5000.0, 67),
    ('Grace', 'female', 10000.5, 85)
]

with sq.connect("task_1.sql") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        gender TEXT DEFAULT male,
        score REAL 
    )""")

    cur.executescript("""ALTER TABLE users RENAME TO renamed_users;
        ALTER TABLE renamed_users ADD COLUMN old INTEGER NOT NULL
    """)

    cur.executemany("INSERT INTO renamed_users VALUES(NULL, ?, ?, ?, ?)", users)

    cur.executescript("""UPDATE renamed_users SET score = score + 500.0 WHERE name LIKE 'R%';
        DELETE FROM renamed_users WHERE id = 3
    """)