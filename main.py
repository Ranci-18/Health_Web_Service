#!/usr/bin/python3
""" retrieve articles and render to webpage """


from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from app.controllers.article_controller import get_article
import pymysql

app = Flask(__name__)

app.secret_key = 'med-info-secret-key'

db = pymysql.connect(host='localhost', user='group1', password='med-info1', db='web_health_service', cursorclass=pymysql.cursors.DictCursor)

@app.route("/")
def index():
    """ returns user to index page """
    if 'logged_in' in session and session['logged_in']:
        return redirect(url_for('logged_index'))
    else:
        return render_template("index.html")


@app.route("/loggedindex")
def logged_index():
    """ returns user to logged index page """
    return render_template("loggedindex.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    """ handles user login """
    if request.method == "POST":
        uniqueid = request.form['uniqueid']
        cursor = db.cursor()
        cursor.execute("SELECT * FROM uniqueid WHERE uniqueid = %s", (uniqueid,))
        user = cursor.fetchone()
        cursor.close()
        if user:
                # User found in the database, set the session variable to indicate logged in
                session['logged_in'] = True
                return redirect(url_for('search'))
        else:
            flash("Unique ID not found")
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    """ Handles user login """
    if request.method == "POST":
        uniqueid = request.form['uniqueid']
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO uniqueid (uniqueid) VALUES (%s)", (uniqueid,))
            db.commit()
            return redirect(url_for('login'))
        except Exception as e:
            db.rollback()
            flash("Error: " + str(e))
            return redirect(url_for('signup'))
        finally:
            cursor.close()
    return render_template("signup.html")


@app.route("/search", methods=['POST', 'GET'])
def search():
    """ Loads search page and displays results """
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))
    if request.method == "POST":
        symptom = request.form['query']
        url = 'https://health.gov/myhealthfinder/api/v3/itemlist.json?Type=topic'
        articles = get_article(url, symptom)
        return render_template("search.html", articles=articles) 
    else:
        return render_template("search.html")


@app.route("/logout")
def logout():
    """ Logout the user by clearing the session """
    session.pop('logged_in', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
