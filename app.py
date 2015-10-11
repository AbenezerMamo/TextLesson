from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TextLesson.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Text, unique=True)
    current_math = db.Colum(db.Integer, default=0)
    current_english = db.Colum(db.Integer, default=0)
    current_science = db.Colum(db.Integer, default=0)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    lesson_subject = db.Column(db.Text)
    lesson_content = db.Column(db.Text)
    lesson_id = db.Colum(db.Integer)


db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Lesson, methods=['GET', 'POST', 'DELETE', 'PUT'])

if __name__ == "__main__":
    app.run()
