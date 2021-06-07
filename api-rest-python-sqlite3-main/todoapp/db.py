
import sqlite3
DATABASE_NAME = "todo.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS todos(
                task TEXT NOT NULL,
                status TEXT NOT NULL,
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
