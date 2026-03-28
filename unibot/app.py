from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def bot_response(user_input):
    # Simple response logic for demonstration
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "fees" in user_input:
        return "School fees are N120,000."
    elif "Course" in user_input:
        return "You can register courses through the student portal."
    elif "Exam" in user_input:
        return "Exam start next month."
    else:
        return "Sorry, I don't understand. Please ask another question."
    

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    return jsonify(bot_response(user_input))

if __name__ == "__main__":
    app.run(debug=True)