from flask import Flask, request, redirect
import twilio.twiml
import requests

app = Flask(__name__)

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
            else:
                return resp.message('Subject currently not supported!')
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
