#!/usr/bin/python3
"""hello routh"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """displays hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display  “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_params(text):
    """display 'C' followed by the value of the text
    variable (replace underscore _ symbols with a space re"""
    no_underscore = text.replace("_", " ")
    return f"C {no_underscore}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
