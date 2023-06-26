from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import random

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.router()
        self.points = 0

    def router(self):
        self.app.route('/', methods=['GET'])(self.index)
        self.app.route('/points-add', methods=['PUT'])(self.points_add)
        self.app.route('/points-sub', methods=['PUT'])(self.points_sub)
        self.app.route('/generate-question', methods=['GET'])(self.generate_question)

    def index(self):
        return render_template("index.html")
    
    def points_add(self):
        self.points = self.points + 3
        return jsonify({"success": True})
    
    def points_sub(self):
        self.points = self.points - 1
        return jsonify({"success": True})
    
    def generate_question(self):
        num1 = random.randint(1, 19)
        num2 = random.randint(2, 20)

        question = f"What is {num1} x {num2}?"
        answer = num1 * num2
        answers = [answer]

        for i in range(3):
            fake_answer = answer + random.randint(1,10)
            while fake_answer == answer or fake_answer in answers:
                fake_answer = answer - random.randint(1,10)
            answers.append(fake_answer)

        random.shuffle(answers)

        return jsonify({
            "options": answers,
            "question": question,
            "answer": answer,
            "points": self.points
        })
