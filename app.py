from flask import Flask, render_template, request, jsonify
from ai_brain import ask_ai

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = ask_ai(user_message)

    return jsonify({
        "response": response
    })


if __name__== "__main__":
    app.run(debug=True)