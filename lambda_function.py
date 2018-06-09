from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, "/")


@ask.launch
def launch():
    return get_last_run()


@ask.intent("GetLastRunIntent")
def get_last_run():
    return statement("Hello, World!")


if __name__ == "__main__":
    app.run(debug=True)
