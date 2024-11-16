from app import app
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from db import db
from sqlalchemy.sql import text
from os import getenv

def login():
    username = request.form["username"]
    password = request.form["password"]

    #TODO: check username and password

    usernames = db.session.execute(text("SELECT username FROM users"))
    users_list = [row[0] for row in usernames.fetchall()]
    if username not in users_list:
        return "Access denied: Invalid username", 401

    session["username"] = username
    return redirect("/")

def logout():
    del session["username"]
    return redirect("/")
