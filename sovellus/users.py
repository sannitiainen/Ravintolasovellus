from app import app
from flask import Flask
from flask import redirect, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from db import db
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash



def login(username, password):
    sql = text("SELECT id, password, admin FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    print(user)
    if not user:
        return False
    else:
        if check_password_hash(user[1], password):
            session["username"] = username
            session["user_id"] = user[0]
            session["user_role"] = "admin" if user[2] else "user"
            return True
        else:
            return False


def register(username, password):    
    hash_value = generate_password_hash(password)
    role = 0
    #try:
    sql = text("INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)")
    db.session.execute(sql, {"username":username, "password":hash_value, "admin":role})
    db.session.commit()
    return login(username, password)
    #except:
    #    return False

def is_admin():
    return session.get("user_role") == "admin"

def become_admin():
    user_id = session["user_id"]

    sql = text("UPDATE users SET admin = 1 WHERE id = :user_id")
    db.session.execute(sql, {"user_id": user_id})
    db.session.commit()

    if session.get("user_id") == user_id:
        session["User_role"] = "admin"
        return True
    else:
        return False






def logout():
    del session["username"]
    del session["user_id"]
    del session["user_role"]
    return redirect("/")