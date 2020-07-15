from flask import Flask, render_template
from assist import assist

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
    return render_template("index.html") and assist()
