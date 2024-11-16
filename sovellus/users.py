from app import app
from flask import Flask
from flask import redirect, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from db import db
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash


def login():
    username = request.form["username"]
    password = request.form["password"]

    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        flash("Username not found. Please register.", "info")
        return redirect("/register")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["username"] = username
            return redirect("/")
        else:
            flash("Invalid password", "error")
            return redirect("/login")


def register():
    username = request.form["username"]
    password = request.form["password"]

    hash_value = generate_password_hash(password)
    sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()



def logout():
    del session["username"]
    return redirect("/")
