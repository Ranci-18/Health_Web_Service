#!/usr/bin/python3
""" retrieve articles and render to webpage """


from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)


@app.route("/")
def index():
    """ returns user to index page """
    return render_template("index.html")


@app.route("/login")
def login():
    """ returns user to login page """
    return render_template("login.html")


@app.route("/search")
def search():
    """ returns user to search page """
    return render_template("search.html")


if __name__ == "__main__":
    app.run()
