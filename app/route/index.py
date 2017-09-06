from app import app
from flask import redirect, url_for

@app.route('/')
def main():
    return redirect(url_for('todo_index'))
