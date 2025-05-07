from flask import Flask, request, render_template, jsonify
import spacy
from responses import faq_dict

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Helper function to match the input
def find_best_match(user_input):
    user_doc = nlp(user_input.lower())
    best_score = 0
    best_response = None

    for question, answer in faq_dict.items():
        question_doc = nlp(question)
        score = user_doc.similarity(question_doc)
        if score > best_score:
            best_score = score
            best_response = answer

    return best_response if best_score > 0.75 else "Sorry, I don't understand that."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get",methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    response = find_best_match(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)