from flask import render_template, request, redirect, url_for

from app import app, db
from app.models.todos import TodoModel


@app.route('/todo', methods=['GET', 'POST'])
def todo_index():
    todo_list = TodoModel.query.all()

    if request.method == 'POST':
        new_todo = TodoModel(title=request.form['title'])

        db.session.add(new_todo)
        db.session.commit()

        return redirect(url_for('todo_index'))

    return render_template('todo.html', todos=todo_list)


@app.route('/todo/<todo_id>/update', methods=['POST'])
def todo_update(todo_id):
    update_todo = TodoModel.query.filter_by(id=todo_id).one()

    update_todo.done = not update_todo.done
    db.session.commit()

    return redirect(url_for('todo_index'))


@app.route('/todo/<todo_id>/delete', methods=['POST'])
def todo_delete(todo_id):
    delete_todo = TodoModel.query.filter_by(id=todo_id).one()

    db.session.delete(delete_todo)
    db.session.commit()

    return redirect(url_for('todo_index'))
