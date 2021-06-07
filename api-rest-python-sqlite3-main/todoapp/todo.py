
from db import get_db


def insert_game(task,status):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO todo(task,status) VALUES (?, ?, ?)"
    cursor.execute(statement, [task,status])
    db.commit()
    return True


def update_game(task,status):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE todo SET task = ?, status = ? WHERE task = ?"
    cursor.execute(statement, [task,status])
    db.commit()
    return True


def delete_game(task):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM todo WHERE task = ?"
    cursor.execute(statement, [task])
    db.commit()
    return True


def get(task):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT task,status FROM todo WHERE task = ?"
    cursor.execute(statement, [task])
    return cursor.fetchone()


def get_games():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT task,status FROM todo"
    cursor.execute(query)
    return cursor.fetchall()
