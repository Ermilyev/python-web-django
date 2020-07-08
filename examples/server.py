from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, world! <a href='/about'>about</a>"


@app.route("/about")
def about():
    return "<a href='/'>back</a>"


app.run()