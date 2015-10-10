from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

# Try adding your own number to this list!
teachers = {
    "+14155796278": [0, 0, 0]
}
subjects = ["maths", "science", "english"]
lesson_plans = [["Today you should teach times tables", "Today you should teach division", "Today you should teach addition"], ["Today you should teach physics", "Today you should teach chemistry", "Today you should teach biology"], ["Today you should teach verbs", "Today you should teach adjectives", "Today you should teach sentences"]]


@app.route("/", methods=['GET', 'POST'])
def message_handling():
    from_number = request.values.get('From', None)
    if from_number is None:
        from_number = "+14155796278"
    body = request.values.get('Body', None)
    sub_index = 0
    for i in range(3):
        if body == subjects[i]:
            sub_index = i
    print(teachers[from_number])
    resp = twilio.twiml.Response()
    lesson_index = teachers[from_number][sub_index]
    resp.message(lesson_plans[sub_index][lesson_index])  # Preps response message
    teachers[from_number][sub_index] += 1
    return str(resp)            # retruns response message

if __name__ == "__main__":
    app.run(debug=True)
