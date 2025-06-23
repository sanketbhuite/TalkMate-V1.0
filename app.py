from flask import Flask, render_template, request, jsonify
from utils import get_tutor_reply
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    user_msg = request.json["message"]
    result = get_tutor_reply(user_msg)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
