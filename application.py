from flask import Flask, render_template
from assist import assist

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html") and assist()
    
@app.route("/main.js")
def js():
    return render_template("main.js")
