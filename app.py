from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TextLesson.db'
db = SQLAlchemy(app)


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    lesson_subject = db.Column(db.Text)
    lesson_content = db.Column(db.Text)


db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Lesson, methods=['GET', 'POST', 'DELETE', 'PUT'])

def get_response():
    response = r = requests.get('https://localhost:5000/api/lesson/1')
    return response.json()[0]

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    resp = twilio.twiml.Response()
    resp.message(get_response())
    return str(resp)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
