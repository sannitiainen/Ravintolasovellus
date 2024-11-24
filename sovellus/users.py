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
    if not user:
        return False
    else:
        if check_password_hash(user[1], password):
            session["username"] = username
            return True
        else:
            return False


def register(username, password):    
    hash_value = generate_password_hash(password)
    role = False
    #try:
    sql = text("INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)")
    db.session.execute(sql, {"username":username, "password":hash_value, "admin":role})
    db.session.commit()
    return login(username, password)
    #except:
    #    return False






def logout():
    del session["username"]
