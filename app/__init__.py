from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
app = Flask(__name__)
# app.config.from_object('config')
#
# db = SQLAlchemy(app)
#
# from app.models import *
from app.route import *

# db.create_all()
