import openai
from flask import Flask, request, render_template, redirect

server = Flask(__name__)

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.8,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0.4,
            presence_penalty=0.3,
            stop=None
        )
    except Exception as e:

        print(e)
        return e
    return response["choices"][0].text

@server.route("/")
def home():
    return render_template("chat.html")

@server.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(generate_response(user_text))

if __name__ == '__main__':
    server.run(debug=False, host='0.0.0.0', port=8088)
