from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

points = 0

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/points-add', methods=['GET'])
def points_add():
    global points
    points = points + 3

@app.route('/points-sub', methods=['GET'])
def points_sub():
    global points
    points = points - 1

@app.route('/generate-question', methods=['GET'])
def generate_question():
    num1 = random.randint(1, 19)
    num2 = random.randint(2, 20)

    question = f"What is {num1} x {num2}?"
    answer = num1 * num2
    answers = [answer]  # Initialize the answers list

    for i in range(3):  # Generate three fake options
        fake_answer = answer + random.randint(1,10)
        while fake_answer == answer or fake_answer in answers:
            fake_answer = answer - random.randint(1,10)
        answers.append(fake_answer)

    random.shuffle(answers)

    # Return the question, options, and points as a JSON response
    return jsonify({
        "options": answers,
        "question": question,
        "answer": answer,
        "points": points
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0")
