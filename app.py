from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TextLesson.db'
db = SQLAlchemy(app)


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    lesson_subject = db.Column(db.Text)
    lesson_content = db.Column(db.Integer)
    lesson_owner = db.Column(db.Text)


db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Lesson, methods=['GET', 'POST', 'DELETE', 'PUT'])



if __name__ == "__main__":
    app.run(host='0.0.0.0')
