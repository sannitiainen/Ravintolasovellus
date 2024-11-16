from app import app
from flask import redirect, render_template, request, session

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login_route():
    return render_template("login.html")