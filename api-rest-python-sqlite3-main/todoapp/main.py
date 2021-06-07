
from flask import Flask, jsonify, request
import todo
from db import create_tables

app = Flask(__name__)


@app.route('/todos', methods=["GET"])
def get_todos():
    todos = todo.get_todos()
    return jsonify(todos)


@app.route("/todo", methods=["POST"])
def insert():
    todo_details = request.get_json()
    task = todo_details["task"]
    status = todo_details["status"]
    result = todo.insert(task,status)
    return jsonify(result)


@app.route("/todo", methods=["PUT"])
def update():
    todo_details = request.get_json()
    task = todo_details["task"]
    status = todo_details["status"]
    result = todo.update(task,status)
    return jsonify(result)


@app.route("/todo/<task>", methods=["DELETE"])
def delete(task):
    result =todo.delete(task)
    return jsonify(result)

@app.route("/todo/<task>", methods=["GET"])
def get_todo_by_id(task):
    todo = get_todo_by_id.get(task)
    return jsonify(todo)


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)
