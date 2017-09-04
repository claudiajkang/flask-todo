from flask import render_template

from app import app


@app.route('/todo')
def todo_index():
    return render_template('todo.html')
