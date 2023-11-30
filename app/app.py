import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")

if not API_KEY:
    raise RuntimeError("OpenAI API key is missing.")

client = OpenAI(api_key=API_KEY)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():
    data = request.json

    messages = data["messages"]

    response = client.chat.completions.create(
        model="gpt-4-1106-preview", messages=messages
    )

    return jsonify(reply=response.choices[0].message.content)


if __name__ == "__main__":
    app.run(debug=True)
