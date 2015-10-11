from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TextLesson.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Text, primary_key=True, unique=True)
    current_math = db.Column(db.Integer, default=0)
    current_english = db.Column(db.Integer, default=0)
    current_science = db.Column(db.Integer, default=0)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    lesson_subject = db.Column(db.Text)
    lesson_content = db.Column(db.Text)
    lesson_id = db.Column(db.Integer)


db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(User, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(Lesson, methods=['GET', 'POST', 'DELETE', 'PUT'])


def request_data(subject, lesson_id):
    r = requests.get('https://localhost:5000/api/lesson')
    data = r.json()
    for lessons in data['objects']:
        if subject in lessons.values():
            if subject['lesson_id'] == lesson_id:
                return subject['lesson_content']

@app.route("/", methods=['GET', 'POST'])
def message_handling():
    resp = twilio.twiml.Response()
    body = request.values.get('Body', None)
    users = requests.get('https://localhost:5000/api/user')
    user_data = r.json()
    for user in user_data['objects']:
        if from_number in user.values():
            if body == 'math':
                content = request_data('math', user['current_math'])
                resp.message(content)
            elif body == 'science':
                content = request_data('science', user['current_sciene'])
                resp.message(content)
            elif body == 'english':
                content = request_data('english', user['current_english'])
                resp.message(content)
            elif body == 'join':
                sign_up = {'id': from_number}
                r = requests.post("https://localhost:5000/api/user", data=sign_up)
                resp.message("Welcome to TextLesson!")
            else:
                return resp.message('Subject currently not supported!')

    return str(resp)

if __name__ == "__main__":
    app.run()
