from flask import Flask, request, redirect
import twilio.twiml
import requests
app2 = Flask(__name__)


def request_data(subject, lesson_id):
    r = requests.get('http://9722c1ea.ngrok.io/api/lesson')
    data = r.json()
    for lessons in data['objects']:
        if subject in lessons.values():
            if lessons["lesson_id"] == lesson_id:
                return lessons["lesson_content"]


@app2.route("/", methods=['GET', 'POST'])
def message_handling():
    resp = twilio.twiml.Response()
    body = request.values.get('Body', None)
    from_number = request.values.get('From', None)
    users = requests.get('http://9722c1ea.ngrok.io/api/user')
    user_data = users.json()
    for user in user_data['objects']:
        if from_number in user.values():
            if body == 'math':
                content = request_data('math', user['current_math'])
                resp.message(content)
            elif body == 'science':
                content = request_data('science', user['current_science'])
                resp.message(content)
            elif body == 'english':
                content = request_data('english', user['current_english'])
                resp.message(content)
            else:
                return resp.message('Subject currently not supported!')
        else:
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
            sign_up = {'id': from_number}  # , 'current_math': 0, 'current_english': 0, 'current_science': 0}
            print("####################################")
            print(sign_up)
            requests.post(url="http://9722c1ea.ngrok.io/api/user", data=sign_up, headers=headers)
            resp.message("Welcome to TextLessons!")

    return str(resp)

if __name__ == "__main__":
    app2.run(debug=True, port=5000)
