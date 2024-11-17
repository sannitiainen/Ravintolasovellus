from app import app
from flask import Flask
from flask import redirect, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from db import db
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash



def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
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
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        sql = "SELECT id FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username": username})
        existing_user = result.fetchone()

        if existing_user:
            return render_template("error.html", message="Käyttäjätunnus on jo käytössä.")
        
        hash_value = generate_password_hash(password)
        try:
            sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
            db.session.execute(sql, {"username":username, "password":hash_value})
            db.session.commit()
        except:
            return False
        return login(username, password)

    return render_template("register.html")




def logout():
    del session["username"]
    return redirect("/")
