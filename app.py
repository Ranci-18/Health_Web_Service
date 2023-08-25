#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/authenticate")
def signin():
    return render_template("login-signup.html")
if __name__ == "__main__":
    app.run()
