from pathlib import Path
from dotenv import dotenv_values
from revChatGPT.V3 import Chatbot
from flask import Flask, request, render_template, redirect

server = Flask(__name__)

parent_dir = Path(__file__).resolve().parent
config = dotenv_values(f"{parent_dir}/.env")

chatbot = Chatbot(api_key=config["OPENAI_API_KEY"])


def generate_response(prompt):
    try:
        response = chatbot.ask(prompt)
        return response
    except Exception as e:
        return e


@server.route("/chat")
def home():
    chatbot.reset()
    return render_template("chat.html")


@server.route("/chat/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(generate_response(user_text))


if __name__ == '__main__':
    server.run(debug=False, host='0.0.0.0', port=8088)
