from flask import Flask, render_template, request
from random import randrange

hello = ["Hello to you too!", "Hello! How are you?", "How can I help you?"]
goodbye = ["Goodbye to you to!", "Have a nice day!", "Waiting for you..."]
sorry = ["Sorry, I can't do that yet!", "Sorry, but I don't understand that!", "Sorry, I can't do that, please, try another command"]
feeling = ["I'm fine, thank you!", "Very well, thanks!", "Very good, tank you! And you?"]
jokes = ["Why did the hipster burn his mouth on his coffee? Because he drank it before it was cool.", "What is the difference between a well-dressed man on a unicycle and a poorly dressed man on a bicycle? Attire."]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button>Send</button>
            </form>
            """

@app.route("/message")
def assist():
    text = request.args.get("message")
    if text:
        text = text.lower()
        if "hello" in text:
            answer = hello[randrange(0, 2)]
            return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
        elif "goodbye" in text:
            answer = goodbye[randrange(0, 2)]
            return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
        elif "random" in text and "number" in text:
            answer = randrange(100)
            return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
        elif "/" in text:
            try:
                answer = f"{int(text.split()[0])} / {int(text.split()[-1])} = {int(text.split()[0])/int(text.split()[-1])}"
                return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
            except:
                answer = sorry[randrange(0, 2)]
                return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
        elif "*" in text:
            try:
                answer = f"{int(text.split()[0])} * {int(text.split()[-1])} = {int(text.split()[0])*int(text.split()[-1])}"
                return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
            except:
                answer = sorry[randrange(0, 2)]
                return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
        elif "+" in text:
            try:
                answer = f"{int(text.split()[0])} + {int(text.split()[-1])} = {int(text.split()[0])+int(text.split()[-1])}"
                return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
            except:
                answer = sorry[randrange(0, 2)]
                return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
        elif "-" in text:
            try:
                answer = f"{int(text.split()[0])} - {int(text.split()[-1])} = {int(text.split()[0])-int(text.split()[-1])}"
                return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
            except:
                answer = sorry[randrange(0, 2)]
                return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
        elif "how are you" in text:
            answer = feeling[randrange(0, 2)]
            return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
        elif "what can you do" in text or "who are you" in text:
            answer = "I am an Assistant by Bekhruz Niyazov. I can translate English to Russian, set timers, count and make you laugh."
            return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
        elif "make me laugh" in text or "joke" in text:
            answer = jokes[randrange(0, 1)]
            return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
        else:
            answer = sorry[randrange(0, 2)]
            return render_template("index.html", answer=answer, user=text) + """
            <form action="message" method="GET", "POST">
                <input name="message" id="send" placeholder="Type here...">
                <button onclick="send()">Send</button>
            </form>
            """
