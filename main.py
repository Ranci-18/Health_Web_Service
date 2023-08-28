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
    symptom = request.json.get("symptom")
    url = f'https://health.gov/myhealthfinder/api/v3/itemlist.json?Type=topic&Keyword={symptom}'
    response = requests.get(url)
    data = response.json()

    # Process data as needed
    processed_data = []

    return jsonify(processed_data)

if __name__ == "__main__":
    app.run()