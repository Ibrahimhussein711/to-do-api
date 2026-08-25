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

def create_task(title: str):
    connection = get_connection()

    cursor = connection.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (title, False)
    )

    task_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return {
        "id": task_id,
        "title": title,
        "done": False
    }


def update_task(task_id: int, title: str, done: bool):
    connection = get_connection()

    cursor = connection.execute(
        "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
        (title, done, task_id)
    )

    if cursor.rowcount == 0:
        connection.close()
        return None

    connection.commit()
    connection.close()

    return get_task_by_id(task_id)

def delete_task(task_id: int):
    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    if cursor.rowcount == 0:
        connection.close()
        return False

    connection.commit()
    connection.close()

    return True



