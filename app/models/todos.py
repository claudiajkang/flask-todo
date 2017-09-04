from sqlalchemy.dialects.mysql import BOOLEAN

from app import db


class TodoModel(db.Model):
    __tablename__ = 'todos'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    done = db.Column(BOOLEAN, default=False)
