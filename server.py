from flask import Flask

import json

app = Flask(__name__)

@app.route("/a")
def index():
    return json.dumps({"a": 1, "b": 2})

@app.route("/b?{x}")
def adv():
    pass

if __name__ == "__main__":
    app.run()
