#!/usr/bin/python3
""" retrieve articles and render to webpage """


from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/search")
def search():
    return render_template('search.html')

if __name__ == "__main__":
    app.run()
