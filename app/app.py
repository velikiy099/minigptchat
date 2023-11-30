from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
from openai import OpenAI
import os
from dotenv import load_dotenv

app = Flask(__name__)
socketio = SocketIO(app)

load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("OpenAI API key is missing.")

client = OpenAI(api_key=API_KEY)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("send_message")
def handle_message(data):
    messages = data["messages"]

    stream = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            socketio.emit("receive_message", {"text": chunk.choices[0].delta.content})


if __name__ == "__main__":
    socketio.run(app, debug=True)
