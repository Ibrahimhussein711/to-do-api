import sqlite3

DATABASE_NAME = "tasks.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def init_db():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL
        
        )
    """)
    cursor = connection.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]

    if count == 0:
        connection.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        ("Study Backend", False)
    )

        connection.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        ("Go to Gym", True)
    )

        connection.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        ("Read FastAPI Docs", False)
    )

    connection.commit()
    connection.close()

init_db()

def get_all_tasks():
    connection = get_connection()

    cursor = connection.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    connection.close()

    tasks = [
        {
            "id": row[0],
            "title": row[1],
            "done": bool(row[2])
        }
        for row in rows
    ]

    return tasks

print(get_all_tasks())

def get_task_by_id(task_id: int):
    connection = get_connection()

    cursor = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    row = cursor.fetchone()

    if row is None:
        connection.close()
        return None

    task = {
        "id": row[0],
        "title": row[1],
        "done": bool(row[2])
    }

    connection.close()

    return task

print(get_task_by_id(1))
