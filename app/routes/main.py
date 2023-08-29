#!/usr/bin/python3
""" retrieve articles and render to webpage """


from flask import Flask, render_template, jsonify, request
from app.controllers.article_controller import get_article

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("../templates/index.html")

@app.route("/search", methods=["POST"])
def search():
    symptom = request.form.get("query").lower()
    url = 'https://health.gov/myhealthfinder/api/v3/itemlist.json?Type=topic'
    articles = get_article(url, symptom)
    return render_template("search.html", articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
