#!/usr/bin/python3
""" retrieve articles and render to webpage """


from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests

app = Flask(__name__)


@app.route("/")
def index():
    """ returns user to index page """
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    """ handles user login """
    if request.method == "POST":
        uniqueid = request.form['uniqueid']
        insert_user_to_db(uniqueid)
        return redirect(url_for('search'))
    else:
       return render_template("login.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    """ Handles user login """
    if request.method == "POST":
        uniqueid = request.form['uniqueid']
        if check_uniqueid_in_db(uniqueid):
            return redirect(url_for('search'))
        else:
            return "Unique ID not found"
    else:
        return render_template("signup.html")


@app.route("/search")
def search():
    """ returns user to login page """
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)
