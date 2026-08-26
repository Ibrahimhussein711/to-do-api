import psycopg
import os
from dotenv import load_dotenv

# تحميل الإعدادات من ملف .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    # الاتصال بـ Postgres باستخدام الرابط اللي في الـ .env
    return psycopg.connect(DATABASE_URL)

def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            # SERIAL في Postgres تعادل AUTOINCREMENT
            cur.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    done BOOLEAN NOT NULL
                )
            """)
            
            cur.execute("SELECT COUNT(*) FROM tasks")
            count = cur.fetchone()[0]

            if count == 0:
                # نستخدم %s بدل ?
                cur.execute("INSERT INTO tasks (title, done) VALUES (%s, %s)", ("Study Backend", False))
                cur.execute("INSERT INTO tasks (title, done) VALUES (%s, %s)", ("Go to Gym", True))
                cur.execute("INSERT INTO tasks (title, done) VALUES (%s, %s)", ("Read FastAPI Docs", False))
            
            conn.commit()

# تشغيل الـ Init عند استدعاء الملف
init_db()

def get_all_tasks():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, done FROM tasks ORDER BY id")
            rows = cur.fetchall()
            return [{"id": row[0], "title": row[1], "done": row[2]} for row in rows]

def get_task_by_id(task_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, done FROM tasks WHERE id = %s", (task_id,))
            row = cur.fetchone()
            if row is None:
                return None
            return {"id": row[0], "title": row[1], "done": row[2]}

def create_task(title: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            # بنستخدم RETURNING id عشان ناخد الـ ID اللي اتعمل فوراً
            cur.execute(
                "INSERT INTO tasks (title, done) VALUES (%s, %s) RETURNING id",
                (title, False)
            )
            task_id = cur.fetchone()[0]
            conn.commit()
            return {"id": task_id, "title": title, "done": False}

def update_task(task_id: int, title: str, done: bool):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE tasks SET title = %s, done = %s WHERE id = %s",
                (title, done, task_id)
            )
            if cur.rowcount == 0:
                return None
            conn.commit()
            return get_task_by_id(task_id)

def delete_task(task_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
            if cur.rowcount == 0:
                return False
            conn.commit()
            return True