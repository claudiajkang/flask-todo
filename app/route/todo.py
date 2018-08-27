from flask import render_template, request, redirect, url_for

from app import app


@app.route('/todo', methods=['GET', 'POST'])
def todo_index():
    return render_template('todo.html')
