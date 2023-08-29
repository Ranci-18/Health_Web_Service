#!/usr/bin/python3
""" retrieve articles and render to webpage """


from flask import Flask, render_template, jsonify, request
from app.controllers.article_controller import get_article
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
    symptom = request.form.get("query").lower()
    url = 'https://health.gov/myhealthfinder/api/v3/itemlist.json?Type=topic'
    articles = get_article(url, symptom)
    return render_template("search.html", articles=articles) 



if __name__ == "__main__":
    app.run()
