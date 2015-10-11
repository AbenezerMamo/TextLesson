from flask import Flask, request, redirect
import twilio.twiml
import requests

app2 = Flask(__name__)


def request_data(subject, lesson_id):
    r = requests.get('https://localhost:5000/api/lesson')
    data = r.json()
    for lessons in data['objects']:
        if subject in lessons.values():
            if subject['lesson_id'] == lesson_id:
                return subject['lesson_content']


@app2.route("/", methods=['GET', 'POST'])
def message_handling():
    resp = twilio.twiml.Response()
    body = request.values.get('Body', None)
    from_number = request.values.get('From', None)
    users = requests.get('https://localhost:5000/api/user')
    user_data = users.json()
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
                requests.post("https://localhost:5000/api/user", data=sign_up)
            else:
                return resp.message('Subject currently not supported!')

    return str(resp)

if __name__ == "__main__":
    app2.run(debug=True, port=3000)
