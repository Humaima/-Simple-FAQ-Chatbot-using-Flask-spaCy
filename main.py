from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Simple FAQ dictionary
faq = {
    "what is your name": "I am ChatBot!",
    "how are you": "I'm just code, but I'm doing great!",
    "what can you do": "I can answer your questions... sort of.",
    "bye": "Goodbye! Have a nice day!",
    "hello": "Hi there! How can I help you today?",
    "what is flask": "Flask is a micro web framework written in Python."
}

def get_best_match(user_input):
    """Use spaCy similarity to find the closest match"""
    input_doc = nlp(user_input.lower())
    best_score = 0.7  # minimum threshold
    best_match = None
    for question in faq:
        question_doc = nlp(question)
        similarity = input_doc.similarity(question_doc)
        if similarity > best_score:
            best_score = similarity
            best_match = question
    return faq[best_match] if best_match else "Sorry, I didn't understand that."

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form.get("msg")
        response = get_best_match(user_input)
        return f"<p><b>You:</b> {user_input}</p><p><b>Bot:</b> {response}</p><a href='/'>Try Again</a>"
    return '''
        <h2>Simple ChatBot</h2>
        <form method="post">
            <input type="text" name="msg" placeholder="Type your message...">
            <input type="submit" value="Send">
        </form>
    '''

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get("msg") or request.json.get("msg")
    if not user_input:
        return jsonify({"response": "Please send a message using 'msg'."})
    response = get_best_match(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
