#!/usr/bin/python3
""" retrieve articles and render to webpage """

from flask import Flask, render_template, jsonify, request, redirect, url_for
from app.controllers.article_controller import get_article
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)

# Define the database connection
engine = create_engine('mysql://group1:med-info1@localhost/health_web_service', echo=True)

# Define a Base class
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'uniqueid'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uniqueid = Column(String(6))

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def insert_user_to_db(uniqueid):
    """ Create a new User instance and add to the session """
    try:
        new_user = User(uniqueid=uniqueid)
        session.add(new_user)
        session.commit()
        return "User added successfully"
    except Exception as e:
        session.rollback()
        return "Error adding user: " + str(e)
    finally:
        session.close()

def check_uniqueid_in_db(uniqueid):
    """ Check if the uniqueid exists in the database """
    try:
        session.query(User).filter_by(uniqueid=uniqueid).one()
        return True
    except NoResultFound:
        return False
    finally:
        session.close()

@app.route("/")
def index():
    """ returns user to index page """
    return render_template("index.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    """ handles user login """
    if request.method == "POST":
        uniqueid = request.form['uniqueid']
        insert_user_to_db(uniqueid)
        return redirect(url_for('login'))
    else:
        return render_template("signup.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    """ Handles user login """
    if request.method == "POST":
        uniqueid = request.form['uniqueid']
        if check_uniqueid_in_db(uniqueid):
            return redirect(url_for('search'))
        else:
            return "Unique ID not found"
    else:
        return render_template("signup.html")

@app.route("/search", methods=['POST', 'GET'])
def search():
    """ Loads search page and displays results """
    if request.method == "POST":
        symptom = request.form['query']
        url = 'https://health.gov/myhealthfinder/api/v3/itemlist.json?Type=topic'
        articles = get_article(url, symptom)
        return render_template("search.html", articles=articles)
    else:
        return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)