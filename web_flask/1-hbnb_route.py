#!/usr/bin/python3
"""hello routh"""

from flask import Flask

app = Flask(__name__)
app.route("/",strict_slashes=False)

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)